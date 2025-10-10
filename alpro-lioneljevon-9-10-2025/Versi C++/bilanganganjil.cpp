#include <iostream>
#include <cstdio>
using namespace std;

int main() {

    cout << "\n=================================" << endl;
    int a, b;
    cout << "Masukkan angka pertama : "; cin >> a;
    cout << "Masukkan angka kedua : "; cin >> b;

    int i = a;
    int n = 0;
    int sum = 0;

    cout << "\nBilangan ganjil: " << endl;
    while(a <= b) {
        if(a % 2 != 0) {
            printf("%d ", a);
            n = n + 1;
            sum += a;
        }
        a++;
    }

    cout << endl;
    cout << "Jumlah bilangan ganjil dari " << i << " sampai " << b << " adalah: " << sum << endl;
    cout << "Banyak bilangan ganjil dari " << i << " sampai " << b << " adalah: " << n << endl;
    cout << "Rata-rata bilangan ganjil dari " << i << " sampai " << b << " adalah: " << (float)sum/n << endl;

    return 0;
}