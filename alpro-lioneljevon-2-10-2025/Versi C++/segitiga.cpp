#include <iostream>
using namespace std;

int main() {
    cout << "++ Menghitung Luas Segitiga ++" << endl;

    double alas, tinggi;
    
    cout << "Masukkan Alas : "; cin>> alas;
    cout << "Masukkan Tinggi Segitiga : "; cin>> tinggi;
    
    double luas_segitiga = 0.5 * alas * tinggi;
	
	cout << "Luas Segitiga Adalah: " << luas_segitiga; 

    return 0;
}
