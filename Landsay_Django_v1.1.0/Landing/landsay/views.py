from django.shortcuts import render

# Layouts Pages
def layout1(request):
    return render(request,"layouts/layouts-1.html")
def layout2(request):
    return render(request,"layouts/layouts-2.html")
def layout3(request):
    return render(request,"layouts/layouts-3.html")
def layout4(request):
    return render(request,"layouts/layouts-4.html")
def layout5(request):
    return render(request,"layouts/layouts-5.html")
def layout6(request):
    return render(request,"layouts/layouts-6.html")

def bloglist(request):
    return render(request,"blog/bloglist.html")  

def blogdetails(request):
    return render(request,"blog/blogdetails.html")       

def login(request):
    return render(request,"account/login.html")     

def register(request):
    return render(request,"account/register.html")        

def resetpassword(request):
    return render(request,"account/resetpassword.html")         
