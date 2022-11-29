from django.shortcuts import render

# Create your views here.
def home_linkedin(request):
    return render(request,'home_templates/homepage.html')

def home_login(request):
    return render(request,'home_templates/login.html')    