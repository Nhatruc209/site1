from django.shortcuts import render, redirect, get_object_or_404
from .models import Home
from geopy.geocoders import Nominatim
from django.contrib import messages

def home_view(request):
    if request.method == 'POST':
        ten = request.POST.get('ten')
        mo_ta = request.POST.get('mo_ta', '')
        tags = request.POST.get('tags', '')
        hinh_anh = request.FILES.get('hinh_anh')
        dia_chi = request.POST.get('dia_chi')
        luot_xem = request.POST.get('luot_xem', 0)
        status = request.POST.get('status') 
        # Home
        home = Home.objects.create(
            ten=ten,
            mo_ta=mo_ta,
            tags=tags,
            hinh_anh=hinh_anh,
            dia_chi=dia_chi,
            luot_xem=luot_xem,
            status=status,
        )      
        # Geocoding Nominatim
        if home.dia_chi:
            geolocator = Nominatim(user_agent="django_geocoder")
            location = geolocator.geocode(home.dia_chi)
            if location:
                home.lat = location.latitude
                home.lon = location.longitude
            else:
                home.lat = None
                home.lon = None
        home.save()       
        messages.success(request, "Thêm dữ liệu thành công!")
        return redirect('home_view')  
    items = Home.objects.all().order_by('-ngay_tao')  
    return render(request, 'home/home.html', {'items': items})

# Edit_home
def edit_home(request, home_id):
    home = get_object_or_404(Home, id=home_id)
    if request.method == 'POST':
        home.ten = request.POST.get('ten')
        home.mo_ta = request.POST.get('mo_ta', '')
        home.tags = request.POST.get('tags', '')
        if request.FILES.get('hinh_anh'):
            home.hinh_anh = request.FILES.get('hinh_anh')
        home.dia_chi = request.POST.get('dia_chi')
        home.luot_xem = int(request.POST.get('luot_xem', 0))  
        home.status = request.POST.get('status') 
        # Geocoding Nominatim
        if home.dia_chi:
            geolocator = Nominatim(user_agent="django_geocoder")
            location = geolocator.geocode(home.dia_chi)
            if location:
                home.lat = location.latitude
                home.lon = location.longitude
            else:
                home.lat = None
                home.lon = None
        
        home.save()
        messages.success(request, "Cập nhật thành công!")
        return redirect('home_view')
    return render(request, 'home/home.html', {'home': home, 'items': Home.objects.all()})

# Delete_home
def delete_home(request, home_id):
    home = get_object_or_404(Home, id=home_id)
    home.delete()
    messages.success(request, "Xóa thành công!")
    return redirect('home_view')
