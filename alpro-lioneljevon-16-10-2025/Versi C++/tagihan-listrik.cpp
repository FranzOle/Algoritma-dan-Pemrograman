#include <iostream>
using namespace std;

int tagihanListrik(int pemakaian, int golongan) {
    int biaya = 0;

    switch (golongan) {
        case 1:
            if (pemakaian <=100) {
                biaya = pemakaian * 1500;
            } else {
                biaya = 100 * 1500 + (pemakaian - 100) * 2000;
            }
            break;

        case 2:
            if (pemakaian <=100) {
                biaya = pemakaian * 2500;
            } else {
                biaya = 100 * 2500 + (pemakaian - 100) * 3000;
            }
            break;

        case 3:
            if (pemakaian <=100) {
                biaya = pemakaian * 4000;
            } else {
                biaya = 100 * 4000 + (pemakaian - 100) * 5000;
            }

            break;

        case 4:
            if (pemakaian <=100) {
                biaya = pemakaian * 5000;
            } else {
                biaya = 100 * 5000 + (pemakaian - 100) * 7000;
            }

            break;
    }

    if (!golongan) {
        if (pemakaian <=100) {
            biaya = pemakaian * 4000;
        } else {
            biaya = 100 * 4000 + (pemakaian - 100) * 5000;
        }
    }
    return biaya;
}

int main() {
    cout << "Menghitung Tagihan Listrik \n";
    int pemakaian, golongan;

    cout << "Masukkan Pemakaian Listrik (kWh) : "; cin >> pemakaian;
    cout << "Masukkan Golongan (1-4) Anda : "; cin >> golongan;
    long biayaTagihan = tagihanListrik(pemakaian, golongan);

    cout << " Biaya : " << biayaTagihan << endl;
    return 0;
}