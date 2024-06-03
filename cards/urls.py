from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cards.views import CardViewSet


router = DefaultRouter()
router.register(r'cards', CardViewSet, basename='card')

app_name = 'cards'
urlpatterns = [
    path('', include(router.urls)),
]
