from . import views
from django.urls import path
app_name = 'alumni_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('feedback/', views.feedback, name='feedback'),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('Registration/', views.Register, name="Register"),
    path('login-alumini/', views.login_alumini, name="login_alumini"),
    path('alumini_dashboard_index/', views.alumini_dashboard_index, name='alumini_dashboard_index'),
    # path('alumni-dashboard/<int:instance_id>/', views.alumni_dashboard, name='alumni_dashboard'),
    path('alumni-dashboard/', views.alumni_dashboard, name="alumni_dashboard"),
    path('profile/', views.profile, name="profile"),
    path('job_notifications/', views.job_notifications, name="job_notifications"),
    path('events/', views.events, name="events"),
    path('online_meetings/', views.online_meetings, name="online_meetings"),
    path('profile/update-profile', views.update_profile, name="update_profile"),
    path('job_notifications/', views.job_notifications, name="job_notifications"),
    path('online_meetings/', views.online_meetings, name="online_meetings"),

]