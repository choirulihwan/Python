import requests
import pandas as pd
import math
import os

# scraping function
def scrap_web(url, istart, namafile, ilength_data):
    url = url.strip('/')
    response = requests.get(url)
    cont = response.json()

    df = pd.DataFrame(cont['data'], columns=['nama', 'pagu', 'metode', 'waktu', 'kldi', 'satuan_kerja', 'lokasi'])
    df.to_csv(namafile, index=False, header=True)  # Don't forget to add '.csv' at the end of the path

    jml_page = math.ceil(cont['recordsFiltered']/ilength_data)

    istart = istart+1
    for x in range(istart, jml_page):
        jstart = istart * ilength_data
        print(istart)
        url = 'https://sirup.lkpp.go.id/sirup/pencarianctr/search?tahunAnggaran=2020&keyword=&jenisPengadaan=2&metodePengadaan=0&draw=2&columns[0][data]=&columns[0][name]=&columns[0][searchable]=false&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=nama&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=true&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=pagu&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=true&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=jenis&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=true&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=metode&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=true&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=waktu&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=true&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=kldi&columns[6][name]=&columns[6][searchable]=true&columns[6][orderable]=true&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=satuan_kerja&columns[7][name]=&columns[7][searchable]=true&columns[7][orderable]=true&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=lokasi&columns[8][name]=&columns[8][searchable]=true&columns[8][orderable]=true&columns[8][search][value]=&columns[8][search][regex]=false&columns[9][data]=id&columns[9][name]=&columns[9][searchable]=true&columns[9][orderable]=true&columns[9][search][value]=&columns[9][search][regex]=false&order[0][column]=5&order[0][dir]=DESC&start=' + str(jstart) + '&length=' + str(ilength_data) + '&search[value]=&search[regex]=false&_=1583757844534'
        namafile = 'csv/sirup_json_' + str(istart) + '.csv'
        scrap_web(url, istart, namafile, ilength_data)

start = 0
ilength_data = 100
start2 = start * ilength_data

namafile = 'csv/sirup_json_' + str(start) + '.csv'
if os.path.isfile(namafile):
    os.remove(namafile)

url = 'https://sirup.lkpp.go.id/sirup/pencarianctr/search?tahunAnggaran=2020&keyword=&jenisPengadaan=2&metodePengadaan=0&draw=2&columns[0][data]=&columns[0][name]=&columns[0][searchable]=false&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=nama&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=true&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=pagu&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=true&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=jenis&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=true&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=metode&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=true&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=waktu&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=true&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=kldi&columns[6][name]=&columns[6][searchable]=true&columns[6][orderable]=true&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=satuan_kerja&columns[7][name]=&columns[7][searchable]=true&columns[7][orderable]=true&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=lokasi&columns[8][name]=&columns[8][searchable]=true&columns[8][orderable]=true&columns[8][search][value]=&columns[8][search][regex]=false&columns[9][data]=id&columns[9][name]=&columns[9][searchable]=true&columns[9][orderable]=true&columns[9][search][value]=&columns[9][search][regex]=false&order[0][column]=5&order[0][dir]=DESC&start=' + str(start2) + '&length=' + str(ilength_data) + '&search[value]=&search[regex]=false&_=1583757844534'
scrap_web(url, start, namafile, ilength_data)

