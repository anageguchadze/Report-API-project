from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'users')


urlpatterns = [
    path('', include(router.urls))
]