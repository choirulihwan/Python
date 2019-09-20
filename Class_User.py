class User:
    def setUserName(self, userName):
        self._userName = userName
    def getUserName(self):
        return self._userName;

def main():
    u1 = User()
    u1.setUserName("Choirul Ihwan")
    print(u1.getUserName())

if __name__ == '__main__': main()
