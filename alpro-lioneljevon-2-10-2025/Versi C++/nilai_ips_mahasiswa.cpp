#include <iostream>
using namespace std;

int main(){
	
	cout << "++ Menghitung Nilai IPS Mahasiswa Universitas Negeri Surabaya ++ \n";
	
	string nama_mahasiswa;
	cout << "Masukkan Nama Lengkap Mahasiswa: "; 
	getline(cin, nama_mahasiswa);

	int nilai_partisipasi, nilai_tugas, nilai_uts, nilai_uas;

	cout << "Masukkan Nilai Partisipasi Siswa: ";
	cin >> nilai_partisipasi;
	cout << "Masukkan Nilai Tugas Siswa: ";
	cin >> nilai_tugas;
	cout << "Masukkan Nilai Ujian Tengah Siswa: ";
	cin >> nilai_uts;
	cout << "Masukkan Nilai Ujian Akhir Semester Siswa: ";
	cin >> nilai_uas;
	cout << endl;

	if (
		nilai_partisipasi < 0 || nilai_partisipasi > 100 ||
		nilai_tugas < 0 || nilai_tugas > 100 ||
		nilai_uts < 0 || nilai_uts > 100 ||
		nilai_uas < 0 || nilai_uas > 100 ) {
		cout << "Input angka tidak boleh negatif atau lebih dari 100. Silakan ulangi inputnya." << endl << endl;
	}
	else {
		double nilai_akhir = ((2 * nilai_partisipasi) + (3 * nilai_tugas) + (2 * nilai_uts) + (3 * nilai_uas)) / 10.0;
		string grade;
		
		if (nilai_akhir >= 85 && nilai_akhir <= 100)
		grade = "A";
		else if (nilai_akhir >= 80)
			grade = "A-";
		else if (nilai_akhir >= 75)
			grade = "B+";
		else if (nilai_akhir >= 70)
			grade = "B";
		else if (nilai_akhir >= 65)
			grade = "B-";
		else if (nilai_akhir >= 60)
			grade = "C+";
		else if (nilai_akhir >= 55)
			grade = "C";
		else if (nilai_akhir >= 40)
			grade = "D";
		else
			grade = "E";

		cout << "Nilai Akhir " << nama_mahasiswa << " adalah: " << nilai_akhir 
				<< " | Nilai Huruf: " << grade << endl << endl;
	}
	
	return 0;
}
