#include <iostream>
using namespace std;

int main() {
    cout << "Rata Rata Bilangan Bulat \n" << endl;

    int bilangan1, bilangan2, bilangan3;

    cout << "Masukkan bilangan bulat pertama: ";
    cin >> bilangan1;
    cout << "Masukkan bilangan bulat kedua: ";
    cin >> bilangan2;
    cout << "Masukkan bilangan bulat ketiga: ";
    cin >> bilangan3;

    auto rataRata = [](int a, int b, int c) {
        return (a + b + c) / 3.0;
    };

    cout << "Rata-rata dari " << bilangan1 << ", " << bilangan2
         << " dan " << bilangan3 << " adalah: "
         << rataRata(bilangan1, bilangan2, bilangan3) << endl;

    return 0;
}
