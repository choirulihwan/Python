import matplotlib.pyplot as plt
import numpy as np

# basic plot
# plt.plot([1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0])
# plt.show()

# function plot
# x = np.arange(0, 6.4, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
# # options
# plt.grid(True)
# # plt.xticks(fontsize=14)
# # plt.yticks(fontsize=14)
# # plt.xlabel(r'$x/rad$', fontsize=24)
# # plt.ylabel(r'$sin(x)$', fontsize=24)
# plt.xlabel(r'$x/rad$')
# plt.ylabel(r'$sin(x)$')
# plt.tight_layout()
# #plt.savefig('Sinplot.eps', format='eps', dpi=1000)
# # display
# plt.show()

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

