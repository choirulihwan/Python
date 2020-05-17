from mobil.models import mobil_saya

i = 0
for dt in mobil_saya:
    i += 1
    print('{} : {} '.format(i, dt))
