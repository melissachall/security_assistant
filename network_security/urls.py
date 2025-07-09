
app_name = 'network_security'
from django.urls import path 
from . import views 
from .views import( network_map_view, host_enumeration_view, detect_os_view, scan_ports_view, services_info_view,    register_view,
    login_view,
    logout_view,)

app_name = 'network_security'

urlpatterns = [
    #path('login/', views.loginPage, name="login"),
    path('', views.home, name="home"),
     # URL pour la vue de la carte réseau
    path('network-map/', network_map_view, name='network_map'),

    # URL pour l'énumération des hôtes
    path('host-enumeration/', host_enumeration_view, name='host_enumeration'),

    # URL pour la détection des systèmes d'exploitation
    path('os-detection/', detect_os_view, name='os_detection'),

    # URL pour la numérisation des ports
    path('port-scanning/', scan_ports_view, name='port_scanning'),

    # URL pour l'identification des services
    path('services_info/', services_info_view, name='services_info'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),


]