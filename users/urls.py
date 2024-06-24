from django.urls import path
from .views import UserRegistrationView, UserLoginView,user_logout,profile,Passchange,UserBankAccountUpdateView,booking_seat,book_detail

 
urlpatterns = [
   path('register/', UserRegistrationView.as_view(), name='register'),
   path('login/', UserLoginView.as_view(), name='login'),
   path('Logout/', user_logout, name='logout'),
  #  path('profile/', profile, name='profile'),
   path('profile/', profile, name='profile'),
   path('profile/edit',UserBankAccountUpdateView.as_view(), name='edit_profile'),
  #  path('profile/edit',edit_profile, name='edit_profile'),
   path('Passchange/', Passchange,name='Passchange'),
   path('booking_seat/', booking_seat,name='booking_seat'),
   path('book_detail/<int:book_id>/',book_detail, name='book_detail' ),
   

 ]