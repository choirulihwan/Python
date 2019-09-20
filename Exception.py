def main():
    try:
        x = input("Enter number: ")
        print(int(x)+5)
    except ValueError as err:
        print("Error: {}".format(err))


if __name__ == '__main__': main()
