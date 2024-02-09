from django.urls import path, include
from avto import views

urlpatterns = [
    path("posts/", views.PostListAPIView.as_view()),
    path("account/create/", views.AccountCreate.as_view())
    ]
