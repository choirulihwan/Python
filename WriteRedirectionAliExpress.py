def main():
    try:

        with open('csv/hotProduct_SmartJewelry_2019-10-01_1_100.csv', 'r') as istr:
            with open('csv/redirection-aliexpress.csv', 'w') as ostr:
                for i, line in enumerate(istr):
                    line = line.rstrip('\n')
                    newline = ""
                    if i > 0:
                        strTemp = line[-40:]
                        strTemp2 = strTemp.replace("http://s.click.aliexpress.com/", "/products/")

                        newline = strTemp2 + "," + strTemp + ",0"
                        #
                    print(newline, file=ostr)

    except IOError as err:
        print("Error: {}".format(err))
    print("app is done")


if __name__ == "__main__" : main()


