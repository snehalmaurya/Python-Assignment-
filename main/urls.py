from django.urls import path
from . import views
urlpatterns = [
   path('', views.loginView, name='loginView'),
   path('stationsView/', views.stationsView, name='stationsView'),
   path('servicesView/', views.servicesView, name='servicesView'),
   path("deleteComp/<int:id>", views.deleteComp, name='deleteComp'),
   path("editComp/<int:id>", views.editComp, name='editComp'),
   path('aboutView/', views.aboutView, name='aboutView'),
   path('profileView', views.profileView, name='profileView'),
   
   path("registerView", views.registerView, name='registerView'),
   path("forgotpassword", views.forgotpassword, name='forgotpassword'),
   path('sendOtp/', views.sendOtp, name='sendOtp'),
   path('otpVerify/', views.otpVerify, name='otpVerify'),
   path('logout', views.logout, name='logout')
]