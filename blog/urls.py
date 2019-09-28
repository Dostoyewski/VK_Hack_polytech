from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.PostDetail, name='post_detail'),
    path('accounts/profile/', views.redirect_to_profile, name='redir'),
    path('accounts/profile/events/', views.redirect_to_event, name='redir_e'),
    path('accounts/profile/change/', views.redirect_to_change, name='redir_ch'),
    path('accounts/profile/arhive/', views.redirect_to_arhive, name='redir_a'),
    path('users/<slug:slug>/events/', views.my_events, name='events'),
    path('users/<slug:slug>/arhive/', views.my_arhive, name='arhive'),
    path('<slug:slug>/event_register/', views.event_register, name='registration'),
    path('users/<slug:slug>/', views.acc_det, name='account'),
    path('users/<slug:slug>/change/', views.change, name='change_data'),
] 