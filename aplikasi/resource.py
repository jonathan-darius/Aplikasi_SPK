from import_export import resources
from aplikasi.models import Karyawan
from import_export.fields import Field

class KaryawanResources(resources.ModelResource):
    prestasi = Field(attribute='prestasi', column_name='nilai')
    kesehatan = Field(attribute='kesehatan', column_name='nilai')
    kemampuan_komunikasi = Field(attribute='kemampuan_komunikasi', column_name='nilai')
    class Meta:
        model = Karyawan
        fields = ['nama','prestasi','masa_kerja','usia','kesehatan','kemampuan_komunikasi']
        export_order = ['nama', 'prestasi', 'masa_kerja', 'usia','kemampuan_komunikasi','kesehatan']