from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("ilanlar/", views.help_request_list, name="help_request_list"),
    path("create/", views.create_help_request, name="create_help_request"),
    path("update/<int:id>/", views.update_help_request, name="update_help_request"),
    path("delete/<int:id>/", views.delete_help_request, name="delete_help_request"),
    path("search/", views.search_help_requests, name="search_help_requests"),
    path("export/", views.export_help_requests_csv, name="export_help_requests_csv"),
    path("import/", views.import_help_requests_csv, name="import_help_requests_csv"),
    path("import_export/", views.import_export, name="import_export"),
    path("profile/", views.view_profile, name="view_profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("profile/delete/", views.delete_profile, name="delete_profile"),
    path("ilan/<int:id>/", views.help_request_detail, name="help_request_detail"),
    path("inbox/", views.inbox, name="inbox"),
    path("mesaj-gonder/", views.send_message, name="send_message"),
    path("ilan/<int:id>/volunteer/", views.volunteer_for_request, name="volunteer_for_request"),
    path("received-offers/", views.received_offers, name="received_offers"),
]