def main():
    try:

        with open('csv/hotProduct_SmartJewelry_2019-10-01_1_100.csv', 'r') as istr:
            with open('csv/hotProduct_SmartJewelry_2019-10-01_1_100_fix.csv', 'w') as ostr:
                for i, line in enumerate(istr):
                    line = line.rstrip('\n')
                    if i == 0:
                        line += ',Product Short Name'
                    else:
                        strJudul = line.split(",")
                        strTemp = strJudul[2].split(" ")
                        strTemp2 = ""
                        try:
                            for i in range(10):
                                strTemp2 += strTemp[i].lstrip('"') + " "
                        except IndexError as err:
                            for i in range(len(strTemp)):
                                strTemp2 += strTemp[i].lstrip('"') + " "

                        line += ',' + strTemp2.rstrip(" ")

                    print(line, file=ostr)

    except IOError as err:
        print("Error: {}".format(err))
    print("app is done")


if __name__ == "__main__" : main()


