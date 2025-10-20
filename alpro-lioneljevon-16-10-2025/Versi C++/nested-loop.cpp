#include <iostream>
using namespace std;

int main() {
    cout << "Nested Loop \n";
    cout << "Segitiga Angka: \n";

    int jumlah;
    cout << "Masukkan Jumlah yang kamu may: "; cin >> jumlah;

    for(int i = 1; i <= jumlah; i++) {
        for(int j = 1; j <= i; j++) {
            cout << i << " ";
        } cout << endl;
    }

    cout << endl;

    for (int a = 1; a <= jumlah; a++) {
        for (int b = 1; b <= a; b++) {
            cout << b << " ";
        }
        cout << endl;
    }

    for (int x = 1; x <= jumlah; x++) {
        if (x % 2 != 0) {
            for (int y = 1; y <= jumlah; y++) {
                cout << y << " ";
            }
            cout << endl;
        }
        else {
            for (int y = jumlah; y >= 1; y--) {
                cout << y << " ";
            }
            cout << endl;
        }
    }

    return 0;
}