from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutUser, name='logoutUser'),

    path('utility-personnel-list/<int:id>', views.status, name='status'),
    path('maintenance-personnel-list/<int:id>', views.mainteStatus, name='mainteStatus'),
    
    path('add-items/', views.addItems, name='add-items'),
    path('add-supplies/', views.addSupplies, name='add-supplies'),
    path('borrowed/', views.borrowed, name='borrowed'),
    path('history/', views.history, name='history'),
    path('admin-homepage/', views.adminHomepage, name='admin-homepage'),
    path('maintenance-personnel-list/', views.maintenancePersonnelList, name='maintenance-personnel-list'),
    path('utility-personnel-list/', views.utilityPersonnelList, name='utility-personnel-list'),
    path('minor-repair/', views.minorRepair, name='minor-repair'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('maintenance-homepage/', views.maintenanceHomepage, name='maintenance-homepage'),
    path('camera/', views.camera, name='camera'),

    path('vehicle/a/<int:id>', views.vehicle_accept, name='vehicle_accept'),
    path('vehicle/b/<int:id>', views.vehicle_decline, name='vehicle_decline'),

    path('borrowed/a/<int:id>', views.borrowed_accept, name='borrowed_accept'),
    path('borrowed/b/<int:id>', views.borrowed, name='borrowed'),

    path('admin-form/<int:id>', views.adminForm, name='admin-form'),
    path('borrow-form/', views.borrowForm, name='borrow-form'),
    path('client-form/', views.clientForm, name='client-form'),
    path('personnel-form/', views.personnelForm, name='personnel-form'),
    path('vehicle-form/', views.vehicleForm, name='vehicle-form'),
    path('supply-form/<int:id>', views.supplyForm, name='supply-form'),
    path('approval-form/<int:id>', views.approvalForm, name='approval-form'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)