from django.shortcuts import render, redirect
# from django.http import HttpResponse

from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *

from django.contrib.auth import authenticate, login, logout

'''<-----------------------------HOMEPAGE---------------------------------->'''

def index(request):
    return render(request, 'pages/homepage/home.html')

# def signup(request):
 
#     if request.user.is_authenticated:
#         return redirect('/books')
     
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
 
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username = username,password = password)
#             login(request, user)
#             return redirect('/books')
         
#         else:
#             return render(request,'itemsapp/signup.html',{'form':form})
     
#     else:
#         form = UserCreationForm()
#         return render(request,'itemsapp/signup.html',{'form':form})

def login(request):
    if request.user.is_authenticated:
        return redirect('/admin-homepage')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userType = request.POST['userType']
        print(username, password, userType)
        user = authenticate(request, username=username, password=password)
        print(user.userType)

        if user is not None and user.userType == 'ADMIN':
            login(request, user)
            return redirect('admin-homepage')
        elif user is not None and user.userType == 'UTILITY_PERSONNEL':
            login(request, user)
            return redirect('utility-personnel')
        elif user is not None and user.userType == 'REPAIR_MAN':
            print('repair-man')
            login(request, user)
            return redirect('/')
        elif user is not None and user.userType == 'ASSISTANT_DIRECTOR':
            print('asst-direc')
            login(request, user)
            return redirect('/')
        else:
            print('Account not found or Empty or Invalid')
            return render(request, 'pages/homepage/home.html')
     
    else:
        return render(request, 'pages/homepage/login.html')

def logout(request):
    logout(request)
    return redirect('index')

'''<----------------------------------------------------------------------->'''

'''<-----------------------------ADMINPAGE--------------------------------->'''

def addItems(request):
    if request.method == "POST":
        form = itemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add-items')
    else:
        form = itemsForm()
    items = itemsDB.objects.all()
    context = {'form':form, 'items':items}
    return render(request, 'pages/admin/addItems.html', context)

def addSupplies(request):
    items = itemsDB.objects.all()
    context = {
        'items':items
    }
    return render(request, 'pages/admin/addSupplies.html',context)

def borrowed(request):
    return render(request, 'pages/admin/borrowed.html')

def history(request):
    return render(request, 'pages/admin/history.html')

def adminHomepage(request):
    return render(request, 'pages/admin/homepage.html')

def utilityPersonnel(request):
    return render(request, 'pages/admin/utilityPersonnel.html')

def utilityPersonnelList(request):
    if request.method == "POST":
        form = janitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/utility-personnel-list')
    else:
        form = janitorForm()
    up = janitorDB.objects.exclude(up_status = 'INACTIVE')
    context = {'form':form, 'up':up}
    return render(request, 'pages/admin/utilityPersonnelList.html', context)

def minorRepair(request):
    return render(request, 'pages/admin/minorRepair.html')

def vehicle(request):
    return render(request, 'pages/admin/vehicle.html')

def camera(request):
    return render(request, 'pages/admin/camera.html')

'''<----------------------------------------------------------------------->'''

'''<-----------------------------FORMSPAGE--------------------------------->'''

def adminForm(request):
    return render(request, 'pages/forms/admin-form.html')

def borrowForm(request):
    if request.method == "POST":
        form = borrowUPForm(request.POST)
        if form.is_valid():
            #up_name = (request.POST[up_name])
            form.save()
    else:
        form = borrowUPForm()
    items = itemsDB.objects.all()
    up = janitorDB.objects.exclude(up_status = 'INACTIVE')
    context = {'form':form, 'items':items, 'up':up}
    return render(request, 'pages/forms/borrow-form.html', context)

def clientForm(request):
    return render(request, 'pages/forms/client-form.html')

def personnelForm(request):
    return render(request, 'pages/forms/personnel-form.html')

def vehicleForm(request):
    return render(request, 'pages/forms/vehicle-form.html')

'''<----------------------------------------------------------------------->'''