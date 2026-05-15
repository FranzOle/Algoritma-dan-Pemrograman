#include <iostream>
using namespace std;

void printNama(string nama) {
    cout << "Hello World " << nama << endl;
}

int tambah(int a, int b) {
    return a + b;
}

int tambahTiga(int a, int b, int c) {
    return a + b + c;
}

double opsionalBelanja(double belanja, double diskon = 0.0) {
    double total = belanja - (belanja * diskon) / 100.0;
    return total;
}

void kali(int a, int b) {
    cout << "a adalah " << a << endl;
    cout << "b adalah " << b << endl;
    cout << "a * b adalah " << (a * b) << endl;
}

auto fungsiLambda(int x, int y) {
    return [=](int a) { return a * x + y; };
}

auto doubleLambda(int n) {
    return [=](int a) { return a * n; };
}

int main() {
    int c = tambah(2, 4);
    cout << c << endl;
    cout << tambah(3, 5) << endl;
    cout << tambahTiga(2, 3, 4) << endl;

    printNama("Lionel Jevon");

    kali(4, 3);

    auto x = [](int a) { return a + 10; };
    cout << x(5) << endl;

    auto kaliLambda = [](int a, int b) { return a * b; };
    cout << kaliLambda(2, 3) << endl;

    auto hasil = fungsiLambda(2, 3);
    cout << hasil(4) << endl;
    cout << hasil(5) << endl;

    auto hasilX = doubleLambda(2);
    auto hasilY = doubleLambda(3);
    cout << hasilX(11) << endl;
    cout << hasilY(11) << endl;

    cout << opsionalBelanja(100.0) << endl;
    cout << opsionalBelanja(200.0, 10.0) << endl;

    return 0;
}
