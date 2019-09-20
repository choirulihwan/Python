class User:
    def __init__(self, userName):
        self._userName = userName

    def getUserName(self):
        return self._userName;

def main():
    u1 = User("Choirul Ihwan")
    print(u1.getUserName())

if __name__ == '__main__': main()
