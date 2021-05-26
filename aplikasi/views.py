from django.shortcuts import render
from aplikasi.models import *
from aplikasi.form import *
from django.conf import settings
from django.shortcuts import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from aplikasi.fungsi_tambahan import *


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


def coba(request):
    karyawan = Karyawan.objects.all()
    total_usia = 0
    total_masakerja = 0
    total_prestasi = 0
    total_k_komunikasi = 0
    total_kesehatan = 0
    for x in range(len(karyawan)):
        total_usia += nilai_usia(karyawan[x].usia)
        total_masakerja += nilai_masa_kerja(karyawan[x].masa_kerja)
        total_prestasi += karyawan[x].prestasi.bobot
        total_k_komunikasi += karyawan[x].kemampuan_komunikasi.bobot
        total_kesehatan += karyawan[x].kesehatan.bobot
    konteks={
        'total_usia': total_usia,
        'total_masakerja': total_masakerja,
        'total_prestasi': int(total_prestasi),
        'total_k_komunikasi': int(total_k_komunikasi),
        'total_kesehatan': int(total_kesehatan),
    }
    return render(request,'coba.html',konteks)