import requests
import json
import math
import os


def xstr(s):
    if s is None:
        return ''
    return str(s)

#convert to csv
def write_csv(idata, namafile):

    with open(namafile, 'a') as ostr:

        for i in range(0, len(idata)):
            data = idata[i]['nama'] + ';' + str(idata[i]['pagu']) + ';' + idata[i]['metode'] + ';' + idata[i]['waktu'] + ';' + idata[i]['kldi'] + ';' + idata[i]['satuan_kerja'] + ';' + xstr(idata[i]['lokasi'])
            print(data, file=ostr)


# scraping function
def scrap_web(url, istart, namafile):
    url = url.strip('/')
    response = requests.get(url)
    cont = response.json()

    write_csv(cont['data'], namafile)

    jml_page = math.ceil(cont['recordsFiltered']/10)
    #print(jml_page)

    istart = istart+1
    for x in range(istart, 2):
        istart = istart * 10
        url = 'https://sirup.lkpp.go.id/sirup/pencarianctr/search?tahunAnggaran=2020&keyword=&jenisPengadaan=2&metodePengadaan=0&draw=2&columns[0][data]=&columns[0][name]=&columns[0][searchable]=false&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=nama&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=true&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=pagu&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=true&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=jenis&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=true&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=metode&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=true&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=waktu&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=true&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=kldi&columns[6][name]=&columns[6][searchable]=true&columns[6][orderable]=true&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=satuan_kerja&columns[7][name]=&columns[7][searchable]=true&columns[7][orderable]=true&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=lokasi&columns[8][name]=&columns[8][searchable]=true&columns[8][orderable]=true&columns[8][search][value]=&columns[8][search][regex]=false&columns[9][data]=id&columns[9][name]=&columns[9][searchable]=true&columns[9][orderable]=true&columns[9][search][value]=&columns[9][search][regex]=false&order[0][column]=5&order[0][dir]=DESC&start=' + str(istart) + '&length=10&search[value]=&search[regex]=false&_=1583757844534'
        scrap_web(url, istart, namafile)


namafile = 'csv/sirup.csv'
if os.path.isfile(namafile):
    os.remove(namafile)

start = 0
url = 'https://sirup.lkpp.go.id/sirup/pencarianctr/search?tahunAnggaran=2020&keyword=&jenisPengadaan=2&metodePengadaan=0&draw=2&columns[0][data]=&columns[0][name]=&columns[0][searchable]=false&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=nama&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=true&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=pagu&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=true&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=jenis&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=true&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=metode&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=true&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=waktu&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=true&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=kldi&columns[6][name]=&columns[6][searchable]=true&columns[6][orderable]=true&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=satuan_kerja&columns[7][name]=&columns[7][searchable]=true&columns[7][orderable]=true&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=lokasi&columns[8][name]=&columns[8][searchable]=true&columns[8][orderable]=true&columns[8][search][value]=&columns[8][search][regex]=false&columns[9][data]=id&columns[9][name]=&columns[9][searchable]=true&columns[9][orderable]=true&columns[9][search][value]=&columns[9][search][regex]=false&order[0][column]=5&order[0][dir]=DESC&start=0&length=10&search[value]=&search[regex]=false&_=1583757844534'
scrap_web(url, start, namafile)
