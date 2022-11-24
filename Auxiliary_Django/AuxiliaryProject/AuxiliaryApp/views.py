from django.shortcuts import render
# from django.http import HttpResponse

'''<-----------------------------HOMEPAGE---------------------------------->'''

def index(request):
    return render(request, 'pages/homepage/home.html')

def login(request):
    return render(request, 'pages/homepage/login.html')

'''<----------------------------------------------------------------------->'''

'''<-----------------------------ADMINPAGE--------------------------------->'''

def addItems(request):
    return render(request, 'pages/admin/addItems.html')

def addSupplies(request):
    return render(request, 'pages/admin/addSupplies.html')

def borrowed(request):
    return render(request, 'pages/admin/borrowed.html')

def history(request):
    return render(request, 'pages/admin/history.html')

def adminHomepage(request):
    return render(request, 'pages/admin/homepage.html')

def utilityPersonnel(request):
    return render(request, 'pages/admin/utilityPersonnel.html')

def utilityPersonnelList(request):
    return render(request, 'pages/admin/utilityPersonnelList.html')

def minorRepair(request):
    return render(request, 'pages/admin/minorRepair.html')

def vehicle(request):
    return render(request, 'pages/admin/vehicle.html')

'''<----------------------------------------------------------------------->'''

'''<-----------------------------FORMSPAGE--------------------------------->'''

def adminForm(request):
    return render(request, 'pages/forms/admin.html')

def borrowForm(request):
    return render(request, 'pages/forms/borrow.html')

def clientForm(request):
    return render(request, 'pages/forms/client.html')

def personnelForm(request):
    return render(request, 'pages/forms/personnel.html')

def vehicleForm(request):
    return render(request, 'pages/forms/vehicle.html')

'''<----------------------------------------------------------------------->'''