from django.urls import path
from blog.views import BlogTop

urlpatterns = [
    path('', BlogTop.as_view(), name="Top"),
]