from django.shortcuts import render, HttpResponse, redirect
from hubofaccounts.models import contact, streviews, image
from django.core.exceptions import ValidationError
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def scholars(request):
    allscholars= image.objects.all()
    context={'allscholars': allscholars}
    return render(request, 'scholars.html', context)

def myspace(request):
    return render(request, 'myspace.html')

def reviews(request):
    allreviews= streviews.objects.all()
    context={'allreviews': allreviews}
    return render(request, 'reviews.html', context)

def Contact(request):
    if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone') 
      desc = request.POST.get('desc')
      Contact = contact(name = name, email = email, phone = phone, desc = desc)
      Contact.save()
      messages.success(request, "Query Sent")
    return render(request, 'contact.html')

def postreviews(request):
     if request.method == "POST":
        review = request.POST.get("review")
        name = request.POST.get("name")
        batch = request.POST.get("batch")
        review = streviews(review= review, name= name, batch= batch)
        review.save()
        messages.success(request, "Review Saved")
     return redirect('/reviews')


def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'tarund' and password == '1234':
            return render(request, 'postdata.html')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'myspace.html')

def upload(request):
    if request.method == "POST" and request.FILES['upload']:
        Image = request.FILES['upload']
        Caption = request.POST.get('caption')
        Image = image(Caption=Caption, Image=Image)
        Image.save()
        messages.success(request, "Image Saved")
    return render(request, 'postdata.html')

