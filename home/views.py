from django.shortcuts import render, redirect
from .forms import HomeForm
from .models import Home
from geopy.geocoders import Nominatim

def home_view(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)

# Dùng Nominatim
            if obj.dia_chi:
                geolocator = Nominatim(user_agent="django_geocoder")
                location = geolocator.geocode(obj.dia_chi)
                if location:
                    obj.lat = location.latitude
                    obj.lon = location.longitude

            obj.save()
            return redirect('home')
    else:
        form = HomeForm()

    items = Home.objects.all().order_by('-ngay_tao')
    return render(request, 'home/home.html', {'form': form, 'items': items})

# Edit_home
def edit_home(request, id):
    record = Home.objects.get(pk=id)
    if request.method == "POST":
        record.name = request.POST.get("name")
        record.email = request.POST.get("email")
        record.save()
        return redirect('home')
    return render(request, 'edit_home.html', {'record': record})

# Delete_home
def delete_home(request, id):
    try:
        home = Home.objects.get(id=id)
        home.delete()
    except Home.DoesNotExist:
        pass
    return redirect('home')