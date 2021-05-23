from django.contrib import admin
from aplikasi.models import *
# Register your models here.
class Admin_karyawan(admin.ModelAdmin):
    list_display = [
        'nama',
        'masa_kerja',
        'usia',
        'kemampuan_komunikasi',
        'kesehatan',
        'prestasi'
    ]
    search_fields = [
        'nama',
        'usia',
        'masa_kerja'
    ]

    list_filter = [
        'prestasi'
    ]


admin.site.register(Karyawan, Admin_karyawan)
admin.site.register(Nilai_prestasi_kerja)
admin.site.register(Nilai_kemampuan_komunikasi)
admin.site.register(Nilai_kesehatan)