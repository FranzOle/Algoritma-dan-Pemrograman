#include <iostream>
using namespace std;

int main() {
    cout << "++ Menghitung Tarif PDAM ++" << endl << endl;

    int pemakaian;
    cout << "Masukkan Pemakaian Air (dalam m3): ";
    cin >> pemakaian;

    long biaya = 0;

    if (pemakaian <= 10) {
        biaya = pemakaian * 5000;
    } 
    else if (pemakaian <= 20) {
        biaya = (10 * 5000) + ((pemakaian - 10) * 7500);
    } 
    else if (pemakaian <= 40) {
        biaya = (10 * 5000) + (10 * 7500) + ((pemakaian - 20) * 10000);
    } 
    else {
        biaya = (10 * 5000) + (10 * 7500) + (20 * 10000) + ((pemakaian - 40) * 15000);
    }

    cout << "Total Biaya PDAM: Rp " << biaya << endl;

    return 0;
}

