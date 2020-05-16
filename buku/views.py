from buku.models import bukus

def run_view():
    print('Daftar buku')
    print('-----------')

    for db in bukus:
        print(db)