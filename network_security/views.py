from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q 
from django.contrib.auth.models import User
from django.contrib import messages
from .port_scanner import scan_ports
from .network_mapping import generate_network_map
from .configurations import NetworkConfiguration
from .host_enumeration import scan_network
from .os_detection import detect_os
from .service_identification import identify_services

# Create your views here.
'''
def loginPage(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username= username)
        except :
            messages.error(request , "User does not exist")
            
    context = {}
    return render(request, 'network_security/login_register.html', context)
'''

def home(request):
    context={}
    return render(request, 'network_security/home.html', context)


def scan_ports_view (request):
    config = NetworkConfiguration ( ip_range= "192.168.234", total_machines=55)
    open_ports = scan_ports(config.ip_range)

    if open_ports: 
        return render(request, 'network_security/port_scan_results.html', {'open_ports': open_ports})
    else:
        return render(request, 'network_security/no_ports_found.html')


def network_map_view(request):
    config = NetworkConfiguration(ip_range="192.168.234", total_machines=55)
    generate_network_map(config.ip_range)

    return render(request, 'network_security/network_map.html')

def host_enumeration_view(request):
    config = NetworkConfiguration(ip_range="192.168.234", total_machines=55)
    active_machines = scan_network(config.ip_range)

    if active_machines:
        return render(request, 'network_security/active_machines.html', {'active_machines': active_machines})
    else:
        return render(request, 'network_security/no_active_machines.html')

def detect_os_view(request):
    target_ip = "192.168.48.54"  # Replace with the target IP address
    os_detection_result = detect_os(target_ip)

    return render(request, 'network_security/os_detection_result.html', {'os_detection_result': os_detection_result})


def services_info_view(request):
    config = NetworkConfiguration(ip_range="192.168.234", total_machines=55)
    active_machines = scan_network(config.ip_range)

    # Sélectionnez une machine active pour identifier les services (supposons que la première machine soit sélectionnée ici)
    selected_machine = active_machines[0]

    open_ports = [80, 443, 22, 21]  # Remplacez cela par vos ports d'intérêt
    services_info = identify_services(selected_machine, open_ports)

    return render(request, 'network_security/services_info.html', {'services_info': services_info})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'network_security/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('home')  # Change 'home' to the URL where you want to redirect after login
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'network_security/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')