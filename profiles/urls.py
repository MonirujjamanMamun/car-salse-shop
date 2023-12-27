from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.register, name='user_signup'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('login/', views.register, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('details/<int:id>/', views.DetailPostView.as_view(), name='details'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('purchase/<int:id>/', views.purchase_car, name='purchase_car'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
]
