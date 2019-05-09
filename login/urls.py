from django.urls import path
from . import views

urlpatterns = [
	path('post/login/', views.login, name='login'),
	path('post/', views.get_name, name='post'),
	path('', views.index, name='landing'),
	path('post/api/attend/',views.apiattend, name= 'attendance'),
	path('post/api/moodle/', views.apimoodle, name="moodle"),
	path('post/api/assign/', views.apiassignment, name="assignment"),
	path('post/api/verifymood', views.verify_moodle, name='verificationmoodle'),
	path('post/api/verifyerp', views.verify_erp, name='verificationerp'),
	path('post/checkusername/', views.check_user, name='check'),
	path('post/signin/', views.signin, name="signin"),
]
