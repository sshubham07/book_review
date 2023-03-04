from django.shortcuts import render
from . models import *
from authentication.models import Profile
from django.contrib import messages
# Create your views here.
def show(request):
    books=Book.objects.all()
    print(books.first().photo)
    return render(request, "book.html",{'books':books}) 

def specific_book(request,slug:int):
    if request.method=='POST':
        comment=request.POST['comment']
        rate=request.POST['rating']
        user=request.user
        auth=Profile.objects.filter(user=user)
        book=Book.objects.filter(id=slug).first()
        if auth[0].is_varified==True:
           Comment.objects.create(comment=comment, user=user, book=book,rating=rate)
        else:
           messages.error(request, "You are not a Authenticated User!!!") 
    specific_book=Book.objects.filter(id=slug).first()
    comments=Comment.objects.filter(book=specific_book)
    logged_in=False
    if request.user.is_authenticated:
        logged_in=True
    not_commented=True
    specific_comment=0
    if logged_in:
       specific_comment=Comment.objects.filter(user=request.user).count()
    if specific_comment>0:
        not_commented=False
    return render(request, "specific_book.html",{"book":specific_book,"comments":comments, "logged_in":logged_in, "not_commented":not_commented})

    

