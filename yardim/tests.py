from django.test import TestCase, Client
from django.urls import reverse
from .models import HelpRequest, User, Category
from .forms import HelpRequestForm
from django.utils import timezone
from django.contrib.auth import get_user_model


class HelpRequestTests(TestCase):
    def setUp(self):
        # Test verilerini oluştur
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name="Test Category")
        self.help_request = HelpRequest.objects.create(
            user=self.user,
            title="Test Help Request",
            description="Test Description",
            category=self.category,
            help_date=timezone.now().date(),
            is_urgent=False
        )

    def test_help_request_list_view(self):
        # İlan listesi görünümünün doğru çalıştığını test et
        response = self.client.get(reverse('help_request_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Help Request")

    def test_create_help_request_view(self):
        # İlan oluşturma görünümünün doğru çalıştığını test et
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_help_request'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], HelpRequestForm)

        # Geçerli bir ilan oluşturmayı test et
        form_data = {
            'title': 'New Help Request',
            'description': 'New Description',
            'category': self.category.id,
            'help_date': timezone.now().date(),
            'is_urgent': False,
        }
        response = self.client.post(reverse('create_help_request'), form_data)
        self.assertEqual(response.status_code, 302)  # Yönlendirme bekliyoruz
        self.assertEqual(HelpRequest.objects.count(), 2)  # Bir ilan daha oluştu mu?

    def test_update_help_request_view(self):
        # İlan güncelleme görünümünün doğru çalıştığını test et
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('update_help_request', args=[self.help_request.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], HelpRequestForm)
        self.assertEqual(response.context['help_request'], self.help_request)

        # İlanı güncellemeyi test et
        form_data = {
            'title': 'Updated Help Request',
            'description': 'Updated Description',
            'category': self.category.id,
            'help_date': timezone.now().date(),
            'is_urgent': True,
        }
        response = self.client.post(reverse('update_help_request', args=[self.help_request.id]), form_data)
        self.assertEqual(response.status_code, 302)  # Yönlendirme bekliyoruz
        self.help_request.refresh_from_db()  # Veritabanından güncel veriyi al
        self.assertEqual(self.help_request.title, 'Updated Help Request')
        self.assertEqual(self.help_request.description, 'Updated Description')
        self.assertEqual(self.help_request.is_urgent, True)

    def test_delete_help_request_view(self):
        # İlan silme görünümünün doğru çalıştığını test et
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('delete_help_request', args=[self.help_request.id]))
        self.assertEqual(response.status_code, 200)

        # İlanı silmeyi test et
        response = self.client.post(reverse('delete_help_request', args=[self.help_request.id]))
        self.assertEqual(response.status_code, 302)  # Yönlendirme bekliyoruz
        self.assertEqual(HelpRequest.objects.count(), 0)  # İlan silindi mi?
