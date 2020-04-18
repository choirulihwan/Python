from teman.models import temans

def run_view():
    print('Daftar teman')
    print('-----------')

    for dt in temans:
        print(dt)