def generator(hasil):
    hasil = round(hasil*100)
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
    hasil = (cout-cmin)/(cmax-cmin)
    return hasil