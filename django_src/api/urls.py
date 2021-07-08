from django.urls import path

from api.views import SignInAPIView, SubscriptionUpdate

urlpatterns = [
    path('auth/', SignInAPIView.as_view()),
    path('users/update/', SubscriptionUpdate.as_view())
]