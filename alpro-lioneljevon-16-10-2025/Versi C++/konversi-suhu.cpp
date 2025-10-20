#include <iostream>
using namespace std;

double celsiusFahrenheit(double celsius) {
    return (9.0 / 5.0) * celsius + 32;
}

double celsiusReamur(double celsius) {
    return (4.0 / 5.0) * celsius;
}


int main() {
    double celsius;
    cout << "Masukkan Suhu Celsius : "; cin >> celsius;
    cout << celsius << endl;

    double fahrenheit = celsiusFahrenheit(celsius);
    double reamur = celsiusReamur(celsius);
    cout << "Hasil Celsius ke Fahrenheit : " << fahrenheit << endl;
    cout << "Hasil Celsius ke Reamur : " << reamur << endl;

    return 0;
}