from django.urls import path

from users.views import WhoAmIView

urlpatterns = [
    path('whoami/', WhoAmIView.as_view()),
]