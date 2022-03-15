from django.urls import path
from blog.views import BlogTop, BlogDetail

urlpatterns = [
    path('', BlogTop.as_view(), name="Top"),
    path('detail/<int:pk>/', BlogDetail.as_view(), name="Detail"),
]