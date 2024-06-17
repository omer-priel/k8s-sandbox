from django.urls import path

from app.views import view_root

urlpatterns = [
    path('', view_root),
]
