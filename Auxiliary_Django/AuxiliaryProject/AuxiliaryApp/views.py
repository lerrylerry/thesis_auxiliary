from django.shortcuts import render, redirect
# from django.http import HttpResponse

from .models import *
from .forms import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseForbidden
import cv2

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
            login(request, user)
            return redirect('vehicle')
        elif user is not None and user.userType == 'MAINTENANCE':
            login(request, user)
            return redirect('maintenance')
        else:
            messages.error(request, 'FAILED: Invalid Account or Not Found')
            return render(request, 'pages/homepage/signin.html')
     
    else:
        x = 0
        if CustomUser.objects.filter(userType__in = ['ADMIN','ASSISTANT_DIRECTOR']).count() < 2:
            return render(request, 'pages/homepage/signin.html', {'x':x})
        return render(request, 'pages/homepage/signin.html', {'x':x+1})

def signup(request):
    if request.user.userType != 'ADMIN':
        if request.method == 'POST':
            if CustomUser.objects.filter(userType__in = ['ADMIN','ASSISTANT_DIRECTOR']).count() == 2:
                form = userForm(request.POST ,no_delete=True)
            elif CustomUser.objects.filter(userType__in = ['ADMIN','ASSISTANT_DIRECTOR']).count() == 1:
                if CustomUser.objects.filter(userType = 'ADMIN').exists():
                    form = userForm(request.POST, no_admin=True)
                elif CustomUser.objects.filter(userType = 'ASSISTANT_DIRECTOR').exists():
                    form = userForm(request.POST, no_asst=True)
            else:
                form = userForm(request.POST)

            if form.is_valid():
                form.save()
                name = request.POST['username']
                password = request.POST['password1']
                email = request.POST['email']
                send_mail(
                    subject='Registered Successfully',
                    message="Thank You"+"! \nName: "+name+" \nPassword: "+password,
                    from_email='Developers '+settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False
                )
                return redirect('/signin')
            else: 
                return render(request,'pages/homepage/signup.html',{'form':form})
                    
        else:
            if CustomUser.objects.filter(userType__in = ['ADMIN','ASSISTANT_DIRECTOR']).count() == 2:
                form = userForm(no_delete=True)
            elif CustomUser.objects.filter(userType__in = ['ADMIN','ASSISTANT_DIRECTOR']).count() == 1:
                if CustomUser.objects.filter(userType = 'ADMIN').exists():
                    form = userForm(no_admin=True)
                elif CustomUser.objects.filter(userType = 'ASSISTANT_DIRECTOR').exists():
                    form = userForm(no_asst=True)
            else:
                form = userForm()
        return render(request,'pages/homepage/signup.html',{'form':form})

    else:
        if request.method == 'POST':
            form = mainteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/admin-homepage')
        else: 
            form = mainteForm()
            return render(request,'pages/homepage/signup.html', {'form':form})

def logoutUser(request):
    logout(request)
    return redirect('index')

'''<----------------------------------------------------------------------->'''

'''<-----------------------------ADMINPAGE--------------------------------->'''
@login_required(login_url='signin')
def status(request, id):
    if request.user.userType == 'ADMIN':
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
    
    else:
        return HttpResponseForbidden()

@login_required(login_url='signin')
def mainteStatus(request, id):
    if request.user.userType == 'ADMIN':
        stats= CustomUser.objects.get(id=id)
        if stats.status == 'ACTIVE':
            stats.status = 'INACTIVE'
            stats.save()
        else:
            stats.status = 'ACTIVE'
            stats.save()
        return redirect('maintenance-personnel-list')

    else:
        return HttpResponseForbidden()

@login_required(login_url='signin')
def addItems(request):
    if request.user.userType == 'ADMIN':
        if request.method == "POST":
            form = itemsForm(request.POST)
            if form.is_valid():
                name = request.POST['item_name']
                quantity = request.POST['item_quantity']
                unit = request.POST['item_unit']
                query = itemsDB.objects.filter(item_name = name).count()
                if query == 0:
                    items = itemsDB.objects.create(item_name = name, item_quantity = quantity, item_unit = unit)
                    messages.success(request, 'SUCCESS: successfully added')
                    # form.save()
                    return redirect('/add-items')
                else:
                    messages.error(request, 'FAILED: item already exist')
                    return redirect('/add-items')
        else:
            form = itemsForm()
        items = itemsDB.objects.all()
        context = {'form':form, 'items':items}
        return render(request, 'pages/admin/addItems.html', context)

    else:
        return HttpResponseForbidden()

@login_required(login_url='signin')
def addSupplies(request):
    if request.user.userType == 'ADMIN':
        if request.method == "POST":
            form = itemsForm(request.POST)
            if form.is_valid():
                itemName = request.POST['items']
                quantity = int(request.POST['item_quantity'])
                check = itemsDB.objects.get(id=itemName)
                new_val = check.item_quantity + quantity
                check.item_quantity = new_val
                #check.itemsName_Quantity[check.item_name] = new_val
                check.save()
                return redirect('/add-items')
        else:
            form = itemsForm()
        items = itemsDB.objects.all()
        context = {'form':form, 'items':items}
        return render(request, 'pages/admin/addItems.html',context)
    
    else:
        return HttpResponseForbidden()

@login_required(login_url='signin')
def borrowed(request):
    if request.user.userType == 'ADMIN':
        requests = borrowDB.objects.prefetch_related('utility_personnel').filter(status='PENDING')
        items = itemsDB.objects.all()
        context = {
            'requests':requests,
            'items':items
        }
        return render(request, 'pages/admin/borrowed.html', context)

    else:
        return HttpResponseForbidden()

@login_required(login_url='signin')
def borrowed_accept(request, id):
    if request.user.userType == 'ADMIN':
        # quantity = int(request.POST['quantity'])
        allItems = borrowDB.objects.get(id=id)
        print(allItems.items_req)
        for x in allItems.items_req:
            print(allItems.items_req[x])
            req = allItems.items_req[x]
            availItems = itemsDB.objects.get(item_name = x)
            old = availItems.item_quantity
            print(availItems.item_name)
            print(availItems.item_quantity)
            new_quantity = int(old) - int(req)
            print(new_quantity)
            availItems.item_quantity = new_quantity
            availItems.save()
        allItems.status = "ACCEPTED"
        allItems.save()
        #createhistory
        his = historyDB.objects.create(his_name = allItems.utility_personnel.up_name, service = 'INVENTORY', his_status=allItems.status, borrow=allItems)
        his.save()
        return redirect('borrowed')

    else:
        return HttpResponseForbidden()

@login_required(login_url='signin')
def history(request):
    vehi_his = historyDB.objects.filter(service = 'VEHICLE')
    his = historyDB.objects.exclude(service = 'VEHICLE')
    items= itemsDB.objects.all()
    gethis = historyDB.objects.get(borrow = 6)
    name=gethis.borrow.utility_personnel.up_name
    for x in gethis.borrow.items_req:
        print(gethis.borrow.items_req[x])
        print(x)
    context ={
        'his':his,
        'vehi_his':vehi_his,
        'items':items
        }
    return render(request, 'pages/admin/history.html',context)

@login_required(login_url='signin')
def adminHomepage(request):
    if request.user.userType == 'ADMIN':
        return render(request, 'pages/admin/homepage.html')

    else:
        return HttpResponseForbidden()

@login_required(login_url='signin')
def maintenancePersonnelList(request):
    if request.user.userType == 'ADMIN':
        if request.method == "POST":       
            form = mainteForm(request.POST)
            if form.is_valid():
                wait = form.save(commit=False)
                wait.userType = 'MAINTENANCE'
                wait.save()
                return redirect('/maintenance-personnel-list')
        else:
            form = mainteForm()
        mp = CustomUser.objects.filter(userType='MAINTENANCE')
        context = {'form':form, 'mp':mp}
        return render(request, 'pages/admin/maintePersonnelList.html', context)

    else:
        return HttpResponseForbidden()
   
@login_required(login_url='signin')
def utilityPersonnelList(request):
    if request.user.userType == 'ADMIN':
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

    else:
        return HttpResponseForbidden()

@login_required(login_url='signin')
def minorRepair(request):
    if request.user.userType == 'ADMIN':
        repair = clientrepairDB.objects.filter(status = 'PENDING')
        context = {'repair':repair}
        return render(request, 'pages/admin/minorRepair.html',context)

    else:
        return HttpResponseForbidden()

@login_required(login_url='index')
def vehicle(request):
    if request.user.userType == 'ASSISTANT_DIRECTOR':
        #vehicles = vehicleDB.objects.get(id=id)
        vehicles = vehicleDB.objects.filter(status = 'PENDING')
        #form = vehicleForm(instance=vehicles)
        context = {'vehicles':vehicles}
        return render(request, 'pages/admin/vehicle.html', context)

    else:
        return HttpResponseForbidden()

@login_required(login_url='index')
def maintenance(request):
    if request.user.userType == 'MAINTENANCE':
        return render(request, 'pages/admin/maintenance.html')

    else:
        return HttpResponseForbidden()

@login_required(login_url='signin')
def camera(request):
    if request.user.userType == 'ADMIN':
        cap = cv2.VideoCapture(0)
        # Check if the webcam is opened correctly
        if not cap.isOpened():
            raise IOError("Cannot open webcam")
        while True:
            ret, frame = cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            cv2.imshow('Input', frame)
            c = cv2.waitKey(1)
            if c == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
        return render(request, 'pages/admin/camera.html')

    else:
        return HttpResponseForbidden()

@login_required(login_url='signin')
def vehicle_accept(request, id):
    query = vehicleDB.objects.get(id=id)
    receiver = query.email
    query.status = "ACCEPTED"
    query.save()
    #createhistory
    his = historyDB.objects.create(his_name = query.req_name, service = 'VEHICLE', his_status=query.status, vehicle=query)
    his.save()

    send_mail(
        subject='Accepted Successfully',
        message="Thank You"+"! \nThis email was used to ... for TUPC Auxiliary System.",
        from_email='Developers '+settings.EMAIL_HOST_USER,
        recipient_list=[receiver],
        fail_silently=False
    )
    return redirect('vehicle')

@login_required(login_url='signin')
def vehicle_decline(request, id):
    query = vehicleDB.objects.get(id=id)
    query.status = "REJECTED"
    # query.save()
    his = historyDB.objects.create(his_name = query.req_name, service = 'VEHICLE', his_status=query.status)
    # his.save()
    return redirect('vehicle')

'''<----------------------------------------------------------------------->'''

'''<-----------------------------FORMSPAGE--------------------------------->'''


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
            messages.success(request, "SUCCESS: successfully submitted")
            
            return redirect('client-form')
        else:
            messages.error(request, "ERROR: please enter valid details")
        print(form)
    else:
        form = clientrepairForm()
    context = {'form':form}
    return render(request, 'pages/forms/client-form.html', context)

def adminForm(request, id):
    client = clientrepairDB.objects.get(id=id)
    form = clientrepairForm(instance=client)
    mainte = mainteDB.objects.all()
    if request.method == "POST":
        forms = adminrepairForm(request.POST)
        fabricated = request.POST['fabricate']
        assessed = request.POST['assess']
        assign = request.POST['name']
    
        if forms.is_valid():
            add = adminrepairDB.objects.create(
                fabricate=fabricated,
                assess=assessed, 
                assigned=assign,
                client=client
                )
            # add = forms.save(commit=False)
            # add.client_id = form
            # person = request.POST['name']
            # add.assigned = person
            # add.save()
            # forms.save()
            if fabricated == "YES":
                linkname = '/supply-form/' + str(id)
                return redirect(linkname)
            else:
                linkname = '/approval-form/' + str(id)
                return redirect(linkname)

        else:
            print("error")
    else:
        forms = adminrepairForm()
    context = {'form':form,
            'forms':forms,
            'mainte':mainte,
            'client':client
            }
    return render(request, 'pages/forms/admin-form.html', context)

def supplyForm(request, id):
    client = clientrepairDB.objects.get(id=id)
    saved = suppmatDB.objects.filter(client=id)
    try:
        used = saved[0].client.id
    except:
        pass

    if request.method == "POST":
        forms = suppmatForm(request.POST)
        unit = request.POST['unit']
        quantity = request.POST['quantity']
        particulars = request.POST['particulars']
        if forms.is_valid():
            form = suppmatDB.objects.create(
                unit=unit,
                quantity=quantity, 
                particulars=particulars,
                client=client
                )
            linkname = '/supply-form/' + str(id)
            return redirect(linkname)
    else:
        forms = suppmatForm()
        try:
            context = {
                'forms':forms,
                'saved':saved,
                'data':used,
            }
        except:
            context = {
                'forms':forms,
                'saved':saved,
            }
        
    return render(request, 'pages/forms/supply-form.html',context)

def approvalForm(request,id):
    client = clientrepairDB.objects.get(id=id)
    if request.method == "POST":
        forms = approveForm(request.POST)
        prove = request.POST['prove']
        head = request.POST['head']
        if forms.is_valid():
            form = approvalDB.objects.create(
                prove=prove,
                head=head, 
                client=client
            )
            if prove == 'APPROVED':
                client.status = 'APPROVED'
                send_mail(
                    subject='APPROVED',
                    message="Thank You"+"! \n"+client.name+",Your request has been approved!",
                    from_email='Developers '+settings.EMAIL_HOST_USER,
                    recipient_list=[client.email],
                    fail_silently=False
                )
            elif prove == 'DISAPPROVED':
                client.status = 'DISAPPROVED'
                send_mail(
                    subject='DISAPPROVED',
                    message="We're Sorry"+"! \n"+client.name+",Your request has been decline!",
                    from_email='Developers '+settings.EMAIL_HOST_USER,
                    recipient_list=[client.email],
                    fail_silently=False
                )
            else:
                client.status = 'RESUBMIT'
                send_mail(
                    subject='RESUBMIT',
                    message="We're Sorry"+"! \n"+client.name+",Please resubmit your request!",
                    from_email='Developers '+settings.EMAIL_HOST_USER,
                    recipient_list=[client.email],
                    fail_silently=False
                )

            client.save()
            return redirect('/admin-homepage/')
    else:
        forms = approveForm()
    context = {
        'forms':forms,
    }
    return render(request, 'pages/forms/approval-form.html',context)

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