#include <iostream>
using namespace std;

int main() {
    cout << "++ Menghitung Luas & Keliling Lingkaran ++" << endl;
    
    const double phi = 3.14;
    double r;

    cout << "Masukkan jari-jari lingkaran: ";
	cin >> r;
	   
	    if (r < 0) {
	        cout << "Tidak Bisa\n" << endl;
	        
	    } else {
	        double luas = phi * r * r;
	        double keliling = 2 * phi * r;
	
	        cout << "Luas lingkaran: " << luas << endl;
	        cout << "Keliling lingkaran: " << keliling << "\n" << endl;
	        break;
		}
	

    return 0;
}
