from django.shortcuts import render
from aplikasi.models import *


def index(request):
    karyawan = Karyawan.objects.all()
    konteks={
        'list_karyawan': karyawan,
    }

    return render(request,'test.html', konteks)
