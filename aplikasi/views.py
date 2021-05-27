from django.shortcuts import render
from aplikasi.models import *
from aplikasi.form import *
from django.conf import settings
from django.shortcuts import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from aplikasi.fungsi_tambahan import *
from aplikasi.resource import *

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

@login_required(login_url=settings.LOGIN_URL)
def coba(request):
    karyawan = Karyawan.objects.all()
    list_usia,list_masa_kerja, list_prestasi,list_k_komunikasi, list_kesehatan = [n.usia for n in karyawan],\
                                                                                 [n.masa_kerja for n in karyawan], \
                                                                                 [n.prestasi.bobot for n in karyawan], \
                                                                                 [n.kemampuan_komunikasi.bobot for n in karyawan],\
                                                                                 [n.kesehatan.bobot for n in karyawan]
    """
    total_usia = sum([nilai_usia(x) for x in list_usia])
    total_masakerja = sum([nilai_masa_kerja(x) for x in list_masa_kerja])
    total_prestasi = sum(list_prestasi)
    total_k_komunikasi = sum(list_k_komunikasi)
    total_kesehatan = sum(list_kesehatan)"""

    akhir=[]
    utilitas = []
    n = []
    kriteria = ["Prestasi","Masa Kerja","Usia","Kemampuan Komunikasi", "Kesehatan"]
    normasilasi = [0.4,0.3,0.15,0.1,0.05]
    for x in range(len(karyawan)):
        prestasi = list_prestasi[x]*normasilasi[0]
        masa_kerja = nilai_masa_kerja(list_masa_kerja[x]) * normasilasi[1]
        usia = nilai_usia(list_usia[x])*normasilasi[2]
        kemampuan_komunikasi = list_k_komunikasi[x]*normasilasi[3]
        kesehatan = list_kesehatan[x]*normasilasi[4]
        n.append([list_prestasi[x],nilai_masa_kerja(list_masa_kerja[x]),nilai_usia(list_usia[x]),list_k_komunikasi[x],list_kesehatan[x]])
        akhir.append([prestasi,masa_kerja,usia,kemampuan_komunikasi,kesehatan])
        utilitas.append([karyawan[x].prestasi,list_masa_kerja[x],list_usia[x],karyawan[x].kemampuan_komunikasi,karyawan[x].kesehatan])
    kk =[]
    for p in akhir:
        kk.append([sum(p)])

    final = []
    for m in range(len(karyawan)):
        nama_karyawan = karyawan[m].nama
        hasil = akhir[m]
        hasil_akhir = kk[m][0]
        util = utilitas[m]
        nilai = n[m]
        rekomendasi = generator(hasil_akhir)
        final.append([[nama_karyawan],kriteria,util,nilai,normasilasi,hasil,[hasil_akhir],[rekomendasi]])
    final = sorted(final, key=lambda x: x[6][0], reverse=True)
    konteks={
        'list_hasil':final,
        'normalisasi': normasilasi,
    }
    return render(request, 'coba.html', konteks)

def export_xls(request):
    karyawan = KaryawanResources()
    dataset = karyawan.export()
    response = HttpResponse(dataset.xls,content_type='applications/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=karyawan.xls'
    return response