def nilai_masa_kerja(nilai):
    if nilai >= 10:
      hasil = 100
    elif nilai in range(5,10):
      hasil = 75
    elif nilai in range(2,5):
      hasil = 50
    else:
      hasil = 20
    return(hasil)

def nilai_usia(nilai):
    if nilai >= 40:
      hasil = 100
    elif nilai in range(30,40):
      hasil = 80
    else:
      hasil = 50
    return hasil

def generator(hasil):
    hasil = round(hasil)
    if hasil >=80:
        rekomendasi = "Sangat Layak"
    elif hasil in range(50,80):
        rekomendasi = "Layak"
    elif hasil in range(30,50):
        rekomendasi = "Dipertimbangkan"
    else:
        rekomendasi = "Tidak Layak"
    return rekomendasi

def utility(listt,index):
    cmax = max(listt)
    cmin = min(listt)
    cout = listt[index]
    hasil = (cout-cmin)/(cmax-cmin)*100
    return hasil
