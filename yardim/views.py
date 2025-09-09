
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm, HelpRequestForm, ProfileForm, CommentForm
from .models import Profile, HelpRequest, Category, Comment
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import csv
from django.http import HttpResponse
from .models import Message
from .forms import MessageForm 
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django import forms
import random

# ANA GİRİŞ SAYFASI
def home(request):
    return render(request, "yardim/home.html")

# Kayıt İşlemi
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get("role")
            user.profile.role = role
            user.profile.save()
            messages.success(request, "Kayıt başarılı! Giriş yapabilirsiniz.")
            return redirect("login")
        else:
            messages.error(request, "Kayıt başarısız. Lütfen bilgilerinizi kontrol edin.")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

# Giriş İşlemi
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Hoş geldiniz, {username}!")
                return redirect("help_request_list")
            else:
                messages.error(request, "Geçersiz kullanıcı adı veya şifre.")
        else:
            messages.error(request, "Geçersiz kullanıcı adı veya şifre.")
    form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})

# Çıkış İşlemi
def logout_request(request):
    logout(request)
    messages.info(request, "Başarıyla çıkış yaptınız.")
    return redirect("home")  # Ana giriş sayfasına yönlendir

# İlanları Listeleme (Read)
@login_required
def help_request_list(request):
    help_requests = HelpRequest.objects.all().order_by('-created_at')
    paginator = Paginator(help_requests, 4)  # Sayfa başına 4 ilan
    page = request.GET.get('page')
    try:
        help_requests = paginator.page(page)
    except PageNotAnInteger:
        help_requests = paginator.page(1)
    except EmptyPage:
        help_requests = paginator.page(paginator.num_pages)
    categories = Category.objects.exclude(name="Test Kategorisi")

    # Rastgele hava durumu ve mahalle hatırlatması
    hava_durumu_listesi = [
        "Bugün hava güneşli ve sıcak.",
        "Bugün yağmur yağacak, şemsiyeni unutma!",
        "Hava parçalı bulutlu, serin bir gün.",
        "Bugün rüzgarlı, dikkatli ol.",
        "Akşam saatlerinde hafif yağmur bekleniyor."
    ]
    mahalle_hatirlatmalari = [
        "Çöp toplama günü, çöpünü dışarı çıkarmayı unutma.",
        "Bugün pazar kuruldu, taze sebzeler var.",
        "Akşam komşuluk buluşması var, katılmayı unutma!",
        "Sokakta bakım çalışması var, dikkatli ol.",
        "Bugün mahallede elektrik kesintisi olabilir."
    ]
    hava_durumu = random.choice(hava_durumu_listesi)
    mahalle_hatirlatma = random.choice(mahalle_hatirlatmalari)

    # Eksik template değişkenleri için geçici çözümler
    mahalle_guncellemeleri = []  # Bu özellik için ayrı model oluşturulabilir
    paylasilan_esyalar = []      # Bu özellik için ayrı model oluşturulabilir
    
    context = {
        "help_requests": help_requests,
        "categories": categories,
        "hava_durumu": hava_durumu,
        "mahalle_hatirlatma": mahalle_hatirlatma,
        "mahalle_guncellemeleri": mahalle_guncellemeleri,
        "paylasilan_esyalar": paylasilan_esyalar,
    }
    return render(request, "yardim/help_request_list.html", context)

# İlan Detay ve Yorumlar
@login_required
def help_request_detail(request, id):
    help_request = get_object_or_404(HelpRequest, id=id)
    comments = help_request.comments.all().order_by('-created_at')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.help_request = help_request
            comment.save()
            messages.success(request, "Yorumunuz eklendi.")
            return redirect('help_request_detail', id=help_request.id)
    else:
        form = CommentForm()
    return render(request, "yardim/help_request_detail.html", {
        "help_request": help_request,
        "comments": comments,
        "form": form
    })

# İlan Oluşturma (Create)
@login_required
def create_help_request(request):
    if request.user.profile.role == 'yardim_isteyen':
        if request.method == "POST":
            form = HelpRequestForm(request.POST)
            if form.is_valid():
                help_request = form.save(commit=False)
                help_request.user = request.user
                help_request.save()
                messages.success(request, "İlan başarıyla oluşturuldu.")
                return redirect("help_request_list")
            else:
                messages.error(request, "İlan oluşturulamadı. Lütfen bilgilerinizi kontrol edin.")
        else:
            form = HelpRequestForm()
        return render(request, "yardim/create_help_request.html", {"form": form, 'categories': Category.objects.all()})
    else:
        messages.error(request, "Bu işlem için yetkiniz yok.")
        return redirect("help_request_list")

# İlan Güncelleme (Update)
@login_required
def update_help_request(request, id):
    help_request = get_object_or_404(HelpRequest, id=id)
    if request.user == help_request.user:
        if request.method == "POST":
            form = HelpRequestForm(request.POST, instance=help_request)
            if form.is_valid():
                form.save()
                messages.success(request, "İlan başarıyla güncellendi.")
                return redirect("help_request_list")
            else:
                messages.error(request, "İlan güncellenemedi. Lütfen bilgilerinizi kontrol edin.")
        else:
            form = HelpRequestForm(instance=help_request)
        return render(request, "yardim/update_help_request.html", {
            "form": form,
            "help_request": help_request,
            'categories': Category.objects.all()
        })
    else:
        messages.error(request, "Bu ilanı güncelleme yetkiniz yok.")
        return redirect("help_request_list")

# İlan Silme (Delete)
@login_required
@require_POST
def delete_help_request(request, id):
    help_request = get_object_or_404(HelpRequest, id=id)
    if request.user == help_request.user:
        help_request.delete()
        messages.success(request, "İlan başarıyla silindi.")
    else:
        messages.error(request, "Bu ilanı silme yetkiniz yok.")
    return redirect("help_request_list")

# Arama İşlemi
def search_help_requests(request):
    title = request.GET.get('title')
    category_id = request.GET.get('category')
    help_date_str = request.GET.get('help_date')
    is_urgent = request.GET.get('is_urgent')

    help_requests = HelpRequest.objects.all()

    if title:
        help_requests = help_requests.filter(title__icontains=title)

    if category_id:
        help_requests = help_requests.filter(category_id=category_id)

    if help_date_str:
        try:
            help_date = timezone.datetime.strptime(help_date_str, '%Y-%m-%d').date()
            help_requests = help_requests.filter(help_date__date=help_date)
        except ValueError:
            messages.error(request, "Geçersiz tarih formatı. Lütfen YYYY-MM-DD formatında bir tarih girin.")
            return render(request, 'yardim/search_results.html', {
                'help_requests': [],
                'categories': Category.objects.all(),
                'title': title,
                'category_id': category_id,
                'help_date': help_date_str,
                'is_urgent': is_urgent,
            })

    if is_urgent:
        help_requests = help_requests.filter(is_urgent=is_urgent == '1')

    categories = Category.objects.all()
    paginator = Paginator(help_requests, 10)
    page = request.GET.get('page')
    try:
        help_requests = paginator.page(page)
    except PageNotAnInteger:
        help_requests = paginator.page(1)
    except EmptyPage:
        help_requests = paginator.page(paginator.num_pages)

    # Rastgele hava durumu ve mahalle hatırlatması
    hava_durumu_listesi = [
        "Bugün hava güneşli ve sıcak.",
        "Bugün yağmur yağacak, şemsiyeni unutma!",
        "Hava parçalı bulutlu, serin bir gün.",
        "Bugün rüzgarlı, dikkatli ol.",
        "Akşam saatlerinde hafif yağmur bekleniyor."
    ]
    mahalle_hatirlatmalari = [
        "Çöp toplama günü, çöpünü dışarı çıkarmayı unutma.",
        "Bugün pazar kuruldu, taze sebzeler var.",
        "Akşam komşuluk buluşması var, katılmayı unutma!",
        "Sokakta bakım çalışması var, dikkatli ol.",
        "Bugün mahallede elektrik kesintisi olabilir."
    ]
    hava_durumu = random.choice(hava_durumu_listesi)
    mahalle_hatirlatma = random.choice(mahalle_hatirlatmalari)

    # Eksik template değişkenleri için geçici çözümler
    mahalle_guncellemeleri = []  # Bu özellik için ayrı model oluşturulabilir
    paylasilan_esyalar = []      # Bu özellik için ayrı model oluşturulabilir
    
    context = {
        'help_requests': help_requests,
        'categories': categories,
        'title': title,
        'category_id': category_id,
        'help_date': help_date_str,
        'is_urgent': is_urgent,
        "hava_durumu": hava_durumu,
        "mahalle_hatirlatma": mahalle_hatirlatma,
        "mahalle_guncellemeleri": mahalle_guncellemeleri,
        "paylasilan_esyalar": paylasilan_esyalar,
    }
    return render(request, 'yardim/search_results.html', context)

# CSV Dışa Aktarma
@login_required
def export_help_requests_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="yardim_ilanlari.csv"'
    writer = csv.writer(response)
    writer.writerow(['Başlık', 'Açıklama', 'Oluşturulma Tarihi', 'Konum', 'Yardım Tarihi', 'Acil Mi?'])

    help_requests = HelpRequest.objects.all()
    for help_request in help_requests:
        writer.writerow([
            help_request.title,
            help_request.description,
            help_request.created_at,
            help_request.location,
            help_request.help_date,
            help_request.is_urgent,
        ])
    return response

# CSV İçe Aktarma
@login_required
def import_help_requests_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Lütfen bir CSV dosyası yükleyin.')
            return redirect('import_export')

        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            header = next(reader)

            if header != ['Başlık', 'Açıklama', 'Oluşturulma Tarihi', 'Konum', 'Yardım Tarihi', 'Acil Mi?']:
                messages.error(request, 'CSV dosyasının başlık satırı hatalı. Lütfen doğru formatta bir dosya yükleyin.')
                return redirect('import_export')
            
            for row in reader:
                try:
                    help_date = timezone.datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S') if row[4] else None
                    created_at = timezone.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S') if row[2] else timezone.now()
                    is_urgent = True if row[5].lower() == 'true' else False
                    HelpRequest.objects.create(
                        user=request.user,
                        title=row[0],
                        description=row[1],
                        created_at=created_at,
                        location=row[3],
                        help_date=help_date,
                        is_urgent=is_urgent,
                    )
                except ValueError as e:
                    messages.error(request, f'CSV dosyasında bir hata oluştu. Lütfen tarih formatını kontrol edin. Hata: {e}')
                    return redirect('import_export')
            messages.success(request, 'CSV dosyası başarıyla içe aktarıldı.')
            return redirect('help_request_list')
        except Exception as e:
            messages.error(request, f'CSV dosyasını okurken bir hata oluştu: {e}')
            return redirect('import_export')
    return render(request, 'yardim/import_export.html')

def import_export(request):
    return render(request, 'yardim/import_export.html')

@login_required
def view_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'yardim/view_profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profiliniz başarıyla güncellendi.')
            return redirect('view_profile')
        else:
            messages.error(request, "Profil güncellenemedi. Lütfen bilgilerinizi kontrol edin.")
    else:
        form = ProfileForm(instance=profile) 
        return render(request, 'yardim/edit_profile.html', {'form': form, 'profile': profile})

@login_required
def inbox(request):
    messages_in = Message.objects.filter(receiver=request.user).order_by('-created_at')
    messages_list = []
    for msg in messages_in:
        #   Mesajın üstünde hangi ilan olduğu yazsın
        content = msg.content
        title = ""
        try:
            if "bu ilana yardım etmek istiyor:" in content:
                title_part = content.split("bu ilana yardım etmek istiyor:")[1]
                title = title_part.split("\n")[0].strip()
        except Exception:
            title = ""
        messages_list.append({
            "id": msg.id,
            "sender": msg.sender,
            "content": msg.content,
            "created_at": msg.created_at,
            "title": title,
        })
    return render(request, "yardim/inbox.html", {"messages_in": messages_list})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, "Mesajınız gönderildi.")
            return redirect('inbox')
    else:
        initial = {}
        receiver_id = request.GET.get('receiver')
        title = request.GET.get('title')
        if receiver_id:
            initial['receiver'] = receiver_id
        if title:
            initial['content'] = f"Bu mesaj, '{title}' başlıklı ilana yanıt olarak gönderildi:\n"
        form = MessageForm(initial=initial)
        form.fields['receiver'].widget = forms.HiddenInput()
    return render(request, 'yardim/send_message.html', {'form': form})

@login_required
@require_POST
def delete_profile(request):
    user = request.user
    logout(request)
    user.delete()
    messages.success(request, "Profiliniz silindi.")
    return redirect("home")

@login_required
def volunteer_for_request(request, id):
    if request.user.profile.role == 'yardim_isteyen':
        messages.error(request, "Yardım isteyenler başkalarına yardım teklifi gönderemez.")
        return redirect('help_request_detail', id=id)
    help_request = get_object_or_404(HelpRequest, id=id)
    if request.method == "POST":
        message_content = request.POST.get("message", "")
        Message.objects.create(
            sender=request.user,
            receiver=help_request.user,
            content=f"{request.user.username} bu ilana yardım etmek istiyor: {help_request.title}\n\nMesaj: {message_content}"
        )
        messages.success(request, "Yardım teklifiniz iletildi!")
        return redirect('help_request_detail', id=id)
    return redirect('help_request_detail', id=id)

@login_required
def received_offers(request):
    raw_offers = Message.objects.filter(
        receiver=request.user, content__icontains="yardım etmek istiyor"
    ).order_by('-created_at')
    offers = []
    for offer in raw_offers:
        # Başlığı ve mesajı içerikten çıkarmaya çalışır
        # Format: "{username} bu ilana yardım etmek istiyor: {title}\n\nMesaj: {message}"
        content = offer.content
        title = ""
        message = ""
        try:
            if "bu ilana yardım etmek istiyor:" in content and "Mesaj:" in content:
                title_part = content.split("bu ilana yardım etmek istiyor:")[1]
                title = title_part.split("\n")[0].strip()
                message = content.split("Mesaj:")[1].strip()
            else:
                message = content
        except Exception:
            message = content
        offers.append({
            "sender": offer.sender,
            "title": title,
            "message": message,
            "created_at": offer.created_at,
        })
    return render(request, "yardim/received_offers.html", {"received_offers": offers})