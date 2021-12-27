os =2
ram =int(input("Masukkan jumlah kapasitas RAM: "))
kp  =int(input("Masukkan jumlah kapasitas program: "))

rt =(ram - os)
sisa =(rt - kp)

print("jumlah RAM: ",ram)
print("jumlah sistem operasi: ",os)
print("jumlah kapasitas proogram: ",kp)
print("hasil sisa RAM: ",sisa)
