#include <iostream>
#include <cmath>
using namespace std;

double persamaanMatematika(double x){
    double result = (2 * pow(x, 3)) + 2 * x + 15/x;
    return result;
}

int main() {
    cout<<"Menghitung Fungsi Persamaan Matematika \n";
    double a;

    cout<<"Masukkan nilai :"; cin>>a;
    cout << "Nilai dari fungsinya adalah: " << persamaanMatematika(a) << endl;

return 0;
}