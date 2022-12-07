from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),

    path('add-items/', views.addItems, name='add-items'),
    path('add-supplies/', views.addSupplies, name='add-supplies'),
    path('borrowed/', views.borrowed, name='borrowed'),
    path('history/', views.history, name='history'),
    path('admin-homepage/', views.adminHomepage, name='admin-homepage'),
    path('utility-personnel/', views.utilityPersonnel, name='utility-personnel'),
    path('utility-personnel-list/', views.utilityPersonnelList, name='utility-personnel-list'),
    path('minor-repair/', views.minorRepair, name='minor-repair'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('camera/', views.camera, name='camera'),

    path('vehicle_accept/', views.vehicle_accept, name='vehicle_accept'),
    path('vehicle_decline/', views.vehicle_decline, name='vehicle_decline'),


    path('admin-form/', views.adminForm, name='admin-form'),
    path('borrow-form/', views.borrowForm, name='borrow-form'),
    path('client-form/', views.clientForm, name='client-form'),
    path('personnel-form/', views.personnelForm, name='personnel-form'),
    path('vehicle-form/', views.vehicleForm, name='vehicle-form'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)