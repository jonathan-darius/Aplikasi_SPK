from django.shortcuts import render
from aplikasi.models import *
from aplikasi.form import *
from django.conf import settings
from django.shortcuts import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url=settings.LOGIN_URL)
def index(request):
    karyawan = Karyawan.objects.all()
    if request.POST:
        form = FormKaryawan(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormKaryawan()
            konteks = {
                'list_karyawan': karyawan,
                'form': form,
                'pesan': "Data Berhasil Dimasukkan",
            }
            return (redirect('index'))
    else:
        form = FormKaryawan()
        konteks={
            'list_karyawan': karyawan,
            'form': form,
        }

    return render(request,'test.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_data(request, id_karyawan):
    karyawan = Karyawan.objects.get(id=id_karyawan)
    if request.POST:
        form = FormKaryawan(request.POST,instance=karyawan)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Di UPDATE!!")
            return redirect('ubah', id_karyawan=id_karyawan)
    else:
        form = FormKaryawan(instance=karyawan)
        konteks = {
            'form': form,
            'karyawan': karyawan,
        }
    return render(request,'ubah_data.html',konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_data(request,id_karyawan):
    karyawan = Karyawan.objects.filter(id=id_karyawan)
    karyawan.delete()

    return (redirect('index'))
