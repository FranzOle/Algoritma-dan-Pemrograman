#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    cout << "TABEL PERKALIAN" << endl;

    int a, b;
    cout << "Masukkan angka pertama : "; cin >> a;
    cout << "Masukkan angka kedua   : "; cin >> b;

    cout << "\n📊 Hasil Tabel Perkalian dari " << a << " sampai " << b << endl;
    cout << "===================================================\n" << endl;

    int i = a;
    while(i <= b) {
        int j = a;
        while(j <= b) {
            printf("%2d x %-2d = %-4d  ", i, j, i*j);
            j++;
        }
        printf("\n");
        i++;
    }

    cout << "\n===================================================" << endl;

    return 0;
}
