from django.contrib import admin
from django.urls import path
from aplikasi.views import *
from django.contrib.auth.views import *

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('index/ubah_data/<int:id_karyawan>', ubah_data,name='ubah'),
    path('index/hapus_data/<int:id_karyawan>', hapus_data, name='hapus'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
