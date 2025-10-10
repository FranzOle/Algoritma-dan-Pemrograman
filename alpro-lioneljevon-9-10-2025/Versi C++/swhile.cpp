#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    cout << "=======================" << endl;
    int x, akhir;
    cout << "Masukkan nilai awal : "; cin >> x;
    cout << "Masukkan nilai akhir : "; cin >> akhir;

    cout << "\n=================================" << endl;
    printf("x \t| x+2 \t| x*x \t| (x+2)*x**2 \n");

    int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;

    while(x <= akhir) {
        a = x + 1;
        b = x + 2;
        c = x * x;
        d = (x + 2) * x*x;
        printf("%d\t| %d\t| %d\t| %d\t|\n", a, b, c, d);
        x++;
    }
}