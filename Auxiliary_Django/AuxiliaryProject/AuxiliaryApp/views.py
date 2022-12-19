from django.shortcuts import render, redirect
# from django.http import HttpResponse

from .models import *
from .forms import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

'''<-----------------------------HOMEPAGE---------------------------------->'''

def index(request):
    return render(request, 'pages/homepage/home.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.userType == 'ADMIN':
            login(request, user)
            return redirect('admin-homepage')
        elif user is not None and user.userType == 'ASSISTANT_DIRECTOR':
            print('asst-direc')
            login(request, user)
            return redirect('vehicle')
        else:
            print('Account not found or invalid')
            return render(request, 'pages/homepage/home.html')
     
    else:
        x = 0
        if CustomUser.objects.filter(userType__in = ['ADMIN','ASSISTANT_DIRECTOR']).count() < 2:
            print("no match")
            return render(request, 'pages/homepage/signin.html', {'x':x})
        print("match")
        return render(request, 'pages/homepage/signin.html', {'x':x+1})

def signup(request):
    if request.method == 'POST':
        if CustomUser.objects.filter(userType__in = ['ADMIN','ASSISTANT_DIRECTOR']).count() == 2:
            form = userForm(request.POST ,no_delete=True)
            print("no_delete")
        elif CustomUser.objects.filter(userType__in = ['ADMIN','ASSISTANT_DIRECTOR']).count() == 1:
            if CustomUser.objects.filter(userType = 'ADMIN').exists():
                form = userForm(request.POST, no_admin=True)
                print("no_admin")
            elif CustomUser.objects.filter(userType = 'ASSISTANT_DIRECTOR').exists():
                form = userForm(request.POST, no_asst=True)
                print("no_asst")
        else:
            form = userForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/signin')
        else: 
            return render(request,'pages/homepage/signup.html',{'form':form})
                
    else:
        if CustomUser.objects.filter(userType__in = ['ADMIN','ASSISTANT_DIRECTOR']).count() == 2:
            form = userForm(no_delete=True)
            print("no_delete")
        elif CustomUser.objects.filter(userType__in = ['ADMIN','ASSISTANT_DIRECTOR']).count() == 1:
            if CustomUser.objects.filter(userType = 'ADMIN').exists():
                form = userForm(no_admin=True)
                print("no_admin")
            elif CustomUser.objects.filter(userType = 'ASSISTANT_DIRECTOR').exists():
                form = userForm(no_asst=True)
                print("no_asst")
        else:
            form = userForm()
            print("nothing")
    return render(request,'pages/homepage/signup.html',{'form':form})


def logoutUser(request):
    logout(request)
    return redirect('signin')

'''<----------------------------------------------------------------------->'''

'''<-----------------------------ADMINPAGE--------------------------------->'''
def status(request, id):
    stats= janitorDB.objects.get(id=id)
    if stats.up_status == 'ACTIVE':
        stats.up_status = 'INACTIVE'
        stats.save()
    else:
        stats.up_status = 'ACTIVE'
        stats.save()
    return redirect('utility-personnel-list')
    # up = janitorDB.objects.all()
    # context = {'up':up}
    # return render(request, 'pages/admin/utilityPersonnelList.html', context)

@login_required(login_url='index')
def addItems(request):
    if request.user.userType == 'ADMIN':
        if request.method == "POST":
            form = itemsForm(request.POST)
            if form.is_valid():
                dict = {}
                name = request.POST['item_name']
                quantity = request.POST['item_quantity']
                unit = request.POST['item_unit']
                dict[name] = quantity
                items = itemsDB.objects.create(item_name = name, item_quantity = quantity, item_unit = unit, itemsName_Quantity = dict)
                # form.save()
                return redirect('/add-items')
        else:
            form = itemsForm()
        items = itemsDB.objects.all()
        context = {'form':form, 'items':items}
        return render(request, 'pages/admin/addItems.html', context)
    else:
        return redirect('index')

def addSupplies(request):
    if request.method == "POST":
        form = itemsForm(request.POST)
        if form.is_valid():
            itemName = request.POST['items']
            quantity = int(request.POST['item_quantity'])
            check = itemsDB.objects.get(id=itemName)
            new_val = check.item_quantity + quantity
            check.item_quantity = new_val
            check.itemsName_Quantity[check.item_name] = new_val
            check.save()
            return redirect('/add-items')
    else:
        form = itemsForm()
    items = itemsDB.objects.all()
    context = {'form':form, 'items':items}
    return render(request, 'pages/admin/addItems.html',context)

def borrowed(request):
    requests = borrowDB.objects.prefetch_related('utility_personnel').filter(status='PENDING')
    items = itemsDB.objects.all()
    context = {
        'requests':requests,
        'items':items
    }
    return render(request, 'pages/admin/borrowed.html', context)

def borrowed_accept(request, id):
    #updatesupplies
    # borrowItems = borrowDB.objects.all()
    # allItems = itemsDB.objects.all()
    
    # quantity = int(request.POST['quantity'])
    # check = itemsDB.objects.get(id=old)
    # new_val = check.item_quantity - quantity
    # check.item_quantity = new_val
    # check.itemsName_Quantity[check.item_name] = new_val
    # check.save()

    query = borrowDB.objects.get(id=id)
    query.status = "ACCEPTED"
    query.save()
    #createhistory
    his = historyDB.objects.create(his_name = query.utility_personnel.up_name, service = 'UTILITY', his_status=query.status)
    his.save()
    return redirect('borrowed')
def history(request):
    vehi_his = historyDB.objects.filter(service = 'VEHICLE')
    his = historyDB.objects.all()
    context ={
        'his':his,
        'vehi_his':vehi_his
        }
    return render(request, 'pages/admin/history.html',context)

def adminHomepage(request):
    return render(request, 'pages/admin/homepage.html')

def maintenancePersonnelList(request):
    if request.method == "POST":
        form = mainteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/maintenance-personnel-list')
    else:
        form = mainteForm()
    mp = mainteDB.objects.all()
    context = {'form':form, 'mp':mp}
    return render(request, 'pages/admin/maintePersonnelList.html', context)
   

def utilityPersonnelList(request):
    if request.method == "POST":
        form = janitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/utility-personnel-list')
    else:
        form = janitorForm()
    up = janitorDB.objects.all()
    context = {'form':form, 'up':up}
    return render(request, 'pages/admin/utilityPersonnelList.html', context)

def minorRepair(request):
    repair = clientrepairDB.objects.filter(status = 'PENDING')
    context = {'repair':repair}
    return render(request, 'pages/admin/minorRepair.html',context)

@login_required(login_url='index')
def vehicle(request):
    if request.user.userType == 'ASSISTANT_DIRECTOR':
        #vehicles = vehicleDB.objects.get(id=id)
        vehicles = vehicleDB.objects.filter(status = 'PENDING')
        #form = vehicleForm(instance=vehicles)
        context = {'vehicles':vehicles}
        return render(request, 'pages/admin/vehicle.html', context)
    else:
        return redirect('index')


def camera(request):
    return render(request, 'pages/admin/camera.html')

def vehicle_accept(request, id):
    query = vehicleDB.objects.get(id=id)
    receiver = query.email
    query.status = "ACCEPTED"
    # query.save()
    #createhistory
    his = historyDB.objects.create(his_name = query.req_name, service = 'VEHICLE', his_status=query.status)
    # his.save()

    send_mail(
        subject='Accepted Successfully',
        message="Thank You"+"! \nThis email was used to ... for TUPC Auxiliary System.",
        from_email='Developers '+settings.EMAIL_HOST_USER,
        recipient_list=[receiver],
        fail_silently=False
    )
    return redirect('vehicle')

def vehicle_decline(request, id):
    query = vehicleDB.objects.get(id=id)
    query.status = "REJECTED"
    # query.save()
    his = historyDB.objects.create(his_name = query.req_name, service = 'VEHICLE', his_status=query.status)
    # his.save()
    return redirect('vehicle')

'''<----------------------------------------------------------------------->'''

'''<-----------------------------FORMSPAGE--------------------------------->'''

def adminForm(request):
    return render(request, 'pages/forms/admin-form.html')

def borrowForm(request):
    if request.method == "POST":
        form = borrowUPForm(request.POST)
        if form.is_valid():
            up_id = request.POST["name"]
            #for x in janitorDB
            print(up_id)
            borrow = janitorDB.objects.get(id=up_id)
            print(borrow.up_code)
            code = request.POST['up_code']
            print(code)
            if borrow.up_code == code:
                print("nice")
                items = itemsDB.objects.all()
                dict = {}
                for x in range(len(items)):
                    name = items[x].item_name
                    quantity = request.POST.get(name)
                    print('working')
                    if quantity != '0' and quantity != '':
                        dict[name] = quantity
                if len(dict) != 0:
                    save = borrowDB.objects.create(utility_personnel_id=up_id,items_req=dict)
                    messages.success(request, 'SUCCESS: Request Sent')
                else:
                    messages.error(request, 'ERROR: No Quantity')
                print(dict)
            else:
                print("errror")
                messages.error(request, "ERROR: Wrong PIN")
    else:
        form = borrowUPForm()
    items = itemsDB.objects.all()
    up = janitorDB.objects.exclude(up_status = 'INACTIVE')
    context = {'form':form, 'items':items, 'up':up}
    return render(request, 'pages/forms/borrow-form.html', context)

def clientForm(request):
    if request.method == "POST":
        form = clientrepairForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            # return redirect('/utility-personnel-list')
    else:
        form = clientrepairForm()
    context = {'form':form}
    return render(request, 'pages/forms/client-form.html', context)

def personnelForm(request):
    return render(request, 'pages/forms/personnel-form.html')

def vehicleForm(request):
    if request.method == "POST":
        form = vehiclesForm(request.POST)
        if form.is_valid():
            messages.success(request, 'SUCCESS: Request Sent')
            form.save()
            return redirect('vehicle-form')
    else:
        form = vehiclesForm()
    context = {'form':form}
    return render(request, 'pages/forms/vehicle-form.html', context)

'''<----------------------------------------------------------------------->'''