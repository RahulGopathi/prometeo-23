from django.urls import path,include
from .views import *
from rest_framework import routers
# from users.views import SignUpViewSet
from django.contrib import admin
from django.urls import path, include
from .views import ExtendedUserViewSet, MyObtainTokenPairView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register("sponsors",SponsorsViewSet)

router.register("events",EventViewSet)

router.register("brochure",BrochureViewSet)

router.register("gallery",GalleryViewSet)

router.register("theme",ThemeViewSet)

router.register("news",NewsViewSet)

router.register("eventsponsors",EventSponsorsViewSet)

router.register("preregistration",PreRegistrationViewSet)

router.register("signup",ExtendedUserViewSet)

# router.register("login",MyObtainTokenPairView, basename='login')

urlpatterns=[
    path(r'',include(router.urls)), 
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', MyObtainTokenPairView.as_view(), name='login'),
]