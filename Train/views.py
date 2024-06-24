from django.shortcuts import render,redirect
from  .import forms
from  .import models
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import Train,BorrowingHistory
from django.contrib import messages

class DetailPostView(DetailView):
    model = models.Train
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.train = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


@login_required
def borrow_book(request, book_id):
    train= Train.objects.get(pk=book_id)
    if request.user.account.balance >= train.borrowing_price:
        # Deduct borrowing price from user's account balance
        request.user.account.balance -= train.borrowing_price
        train.quantity -=1
        request.user.account.save()
        train.save()
        # Create borrowing record
        
        BorrowingHistory.objects.create(user=request.user, train=train)


        return redirect('booking_seat')
    else:
        return render(request, 'post_details.html', {'book': train})

