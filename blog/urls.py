from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.PostDetail, name='post_detail'),
    path('accounts/profile/', views.acc_det, name='acc_detail'),
    path('accounts/profile/events', views.my_events, name='events'),
    path('accounts/profile/arhive', views.my_arhive, name='arhive'),
    path('accounts/profile/change', views.change, name='chage_data'),
    path('<slug:slug>/event_register', views.event_register, name='registration'),
] 