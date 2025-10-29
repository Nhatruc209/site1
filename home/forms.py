from django import forms
from .models import Home

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['ten', 'mo_ta', 'tags', 'hinh_anh', 'dia_chi', 'luot_xem', 'status']
        labels = {
            'ten': 'Tên',
            'mo_ta': 'Mô tả',
            'tags': 'Tags',
            'hinh_anh': 'Hình ảnh',
            'dia_chi': 'Địa chỉ',
            'luot_xem': 'Lượt xem',
            'status': 'Trạng thái',
        }
