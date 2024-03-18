import sys

def pohonPencarianBiner(F, P, n):
    for j in range(n):
        F[j][j] = P[j]
        for i in range(j - 1, -1, -1):
            F[i][j] = sys.maxsize
            for k in range(i, j + 1):
                biaya = (
                    sum(P[i : j + 1])
                    if k == j
                    else F[i][k - 1] + F[k + 1][j] + sum(P[i : j + 1]))
                
                F[i][j] = min(F[i][j], biaya)

    return F[0][n - 1]


def Main():
    # inisialisasi data pemesanan
    baju = ["kaos", "kemeja", "dress", "batik"]
    probabilitas = [0.1, 0.2, 0.3, 0.4]
    n = len(baju)

    # membuat tabel F untuk menyimpan biaya minimal
    F = [[0] * n for _ in range(n)]

    # menghitung biaya minimal
    biayaMinimal = pohonPencarianBiner(F, probabilitas, n)

    # tampilkan biaya minimal
    print("Biaya minimal untuk pemesanan baju adalah:", biayaMinimal)

Main()