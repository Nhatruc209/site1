from django.shortcuts import render, redirect, get_object_or_404
from .models import Home
from geopy.geocoders import Nominatim
from django.contrib import messages  # Để hiển thị thông báo thành công/lỗi

def home_view(request):
    if request.method == 'POST':
        ten = request.POST.get('ten')
        mo_ta = request.POST.get('mo_ta', '')
        tags = request.POST.get('tags', '')
        hinh_anh = request.FILES.get('hinh_anh')
        dia_chi = request.POST.get('dia_chi')
        luot_xem = int(request.POST.get('luot_xem', 0))  # Chuyển thành int
        status = request.POST.get('status')
        
        # Tạo đối tượng Home
        home = Home.objects.create(
            ten=ten,
            mo_ta=mo_ta,
            tags=tags,
            hinh_anh=hinh_anh,
            dia_chi=dia_chi,
            luot_xem=luot_xem,
            status=status,
            # lat và lon sẽ được cập nhật sau
        )
        
        # Geocoding: Lấy tọa độ từ dia_chi
        if home.dia_chi:
            geolocator = Nominatim(user_agent="django_geocoder")
            location = geolocator.geocode(home.dia_chi)
            if location:
                home.lat = location.latitude
                home.lon = location.longitude
            else:
                # Nếu không tìm được, có thể đặt mặc định hoặc để trống
                home.lat = None
                home.lon = None
        home.save()
        
        messages.success(request, "Thêm dữ liệu thành công!")
        return redirect('home_view')  # Reload trang để hiển thị danh sách mới
    
    # GET: Hiển thị form và danh sách
    items = Home.objects.all().order_by('-ngay_tao')  # Sắp xếp theo ngày tạo
    return render(request, 'home/home.html', {'items': items})

# View để chỉnh sửa (tùy chọn, dựa trên link trong bảng)
def edit_home(request, home_id):
    home = get_object_or_404(Home, id=home_id)
    if request.method == 'POST':
        # Cập nhật các trường
        home.ten = request.POST.get('ten')
        home.mo_ta = request.POST.get('mo_ta', '')
        home.tags = request.POST.get('tags', '')
        if request.FILES.get('hinh_anh'):
            home.hinh_anh = request.FILES.get('hinh_anh')
        home.dia_chi = request.POST.get('dia_chi')
        home.luot_xem = int(request.POST.get('luot_xem', 0))  # Chuyển thành int
        home.status = request.POST.get('status')
        
        # Geocoding: Lấy tọa độ từ dia_chi mới
        if home.dia_chi:
            geolocator = Nominatim(user_agent="django_geocoder")
            location = geolocator.geocode(home.dia_chi)
            if location:
                home.lat = location.latitude
                home.lon = location.longitude
            else:
                # Nếu không tìm được, đặt None
                home.lat = None
                home.lon = None
        
        home.save()
        messages.success(request, "Cập nhật thành công!")
        return redirect('home_view')
    
    # Truyền dữ liệu hiện tại vào template để điền sẵn form
    return render(request, 'home/home.html', {'home': home, 'items': Home.objects.all()})

# View để xóa (tùy chọn)
def delete_home(request, home_id):
    home = get_object_or_404(Home, id=home_id)
    home.delete()
    messages.success(request, "Xóa thành công!")
    return redirect('home_view')
