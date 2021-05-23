from django.db import models

# Create your models here.
class Nilai_prestasi_kerja(models.Model):
    nilai = models.CharField(max_length=20)
    bobot = models.FloatField()

    def __str__(self):
        return self.nilai

class Nilai_kemampuan_komunikasi(models.Model):
    nilai = models.CharField(max_length=20)
    bobot = models.FloatField()

    def __str__(self):
        return self.nilai

class Nilai_kesehatan(models.Model):
    nilai = models.CharField(max_length=20)
    bobot = models.FloatField()

    def __str__(self):
        return self.nilai


class Karyawan(models.Model):
    nama = models.CharField(max_length=50,null=True)
    prestasi = models.ForeignKey(Nilai_prestasi_kerja, on_delete=models.CASCADE, null=True)
    masa_kerja = models.IntegerField()
    usia = models.IntegerField()
    kemampuan_komunikasi = models.ForeignKey(Nilai_kemampuan_komunikasi, on_delete=models.CASCADE, null=True)
    kesehatan = models.ForeignKey(Nilai_kesehatan, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama