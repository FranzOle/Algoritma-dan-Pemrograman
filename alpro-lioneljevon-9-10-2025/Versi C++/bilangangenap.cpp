#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    cout << "\n=================================" << endl;
    cout << "\n";
    cout << "Mencari Bilangan Genap \n" << endl;

    int awal, akhir;
    cout << "Masukkan Angka awal : "; cin >> awal;
    cout << "Masukkan Angka akhir : "; cin >> akhir;

    cout << "\n=================================" << endl;
    printf("Bilangan Genap:\n");

    while(awal <= akhir) {
        awal += 1;
        if(awal % 2 == 0) {
            printf("%d\t|\n", awal);
        }
    }

    return 0;
}
