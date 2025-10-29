from django.db import models

class Home(models.Model):
    STATUS_CHOICES = [
        ('0','Active'),
        ('1','InActive'),
    ]

    ten = models.CharField(max_length=200)
    mo_ta = models.TextField(blank=True)
    tags = models.CharField(max_length=200, blank=True)
    hinh_anh = models.ImageField(upload_to='uploads/', blank=True, null=True)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    dia_chi = models.CharField(max_length=255, blank=True)
    luot_xem = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='0')
    #  Trường lưu kết quả từ Nominatim
    lat = models.FloatField(null=True, blank=True)   
    lon = models.FloatField(null=True, blank=True) 


    def __str__(self):
        return self.ten
