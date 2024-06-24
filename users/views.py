from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login, logout,update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserRegistrationForm
# ,ChangeUserForm
# ,UserUpdateForm


from django.contrib import messages

class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()

        login(self.request, user)
        # print(user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
    

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

# class UserLogoutView(LogoutView):
#     def get_success_url(self):
#         if self.request.user.is_authenticated:
#             logout(self.request)
#         return reverse_lazy('home')
def user_logout(request):
    logout(request)
    return redirect('home')

class UserBankAccountUpdateView(View):
    template_name = 'update_profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})

# def profile(request):
#     return render(request,'profile.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserUpdateForm  # Assuming you have a form for updating user profile

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserUpdateForm  # Assuming you have a form for updating user profile

@login_required
def profile(request):
    user = request.user  # Get the current user
    
    if request.method == 'POST':
        profile_form = UserUpdateForm(request.POST, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')  # Redirect to the profile page after successful update
    else:
        profile_form = UserUpdateForm(instance=user)  # Populate the form with current user data
    
    return render(request, 'profile.html', {'form': profile_form, 'user': user})


def Passchange(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, './passchange.html', {'form': form})
    else:
        return redirect('login')
    

def booking_seat(request):
    return render(request,'booking_seat.html')


from Train.models import Train, Comment
from Train.forms import CommentForm

def book_detail(request, book_id):
    train = Train.objects.get(pk=book_id)
    reviews = train.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.train = train
            review.save()
            print(form.cleaned_data)
            return render(request, 'book_detail.html', {'book': train, 'reviews': reviews, 'form': form})
    else:
        form = CommentForm()
    return render(request, 'book_detail.html', {'book': train, 'reviews': reviews, 'form': form})