import matplotlib.pyplot as plt
import numpy as np

def guest(fyear):
    # label custom
    x_data = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_datang = [78, 86, 91, 73, 108, 97, 102, 85, 62, 62, 63, 48]
    y_telp = [281, 271, 249, 238, 308, 248, 303, 320, 22, 0, 2, 0]
    y_wa = [0, 0, 0, 0, 0, 0, 0, 0, 342, 369, 276, 261]

    # Create the plot
    plt.plot(x_data, y_datang, 'o-', label="Datang")
    plt.plot(x_data, y_telp, 'o-', label="Telp")
    plt.plot(x_data, y_wa, 'o-', label="Whatsapp")

    plt.legend()

    for i, j in zip(x_data, y_datang):
        plt.text(i, j, str(j), ha='center', va='bottom')
    for i, j in zip(x_data, y_telp):
        plt.text(i, j, str(j), ha='center', va='bottom')
    for i, j in zip(x_data, y_wa):
        plt.text(i, j, str(j), ha='center', va='bottom')

    plt.yticks(np.arange(0, 400, 50))
    plt.grid(True)

    # Add labels and title
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah')
    plt.title('Media Kedatangan Tamu')

    # Show the plot
    plt.show()

print("Daftar fungsi yang tersedia:")
print("1. Kedatangan tamu (guest([tahun]))")

userinput = input("Ketik fungsi: ")
guest(2024)