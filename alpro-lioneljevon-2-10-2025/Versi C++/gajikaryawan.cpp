#include <iostream>
#include <string>
using namespace std;

int main() {
    cout << "++ Perhitungan Tunjangan Karyawan ++\n" << endl;

    string nama;
    double gaji_pokok = 0;
    int golongan, pendidikan;
    double jam_kerja;

    cout << "Masukkan nama karyawan: ";
    getline(cin, nama);

    cout << "Masukkan gaji pokok: ";
    cin >> gaji_pokok;

    cout << "Masukkan golongan (1/2/3): ";
    cin >> golongan;

    cout << "Masukkan pendidikan (SMA = 1, D4/S1 = 2, S2 = 3, S3 = 4): ";
    cin >> pendidikan;

    cout << "Masukkan jam kerja dalam sebulan: ";
    cin >> jam_kerja;

    double tunjangan_golongan = 0;
    double tunjangan_pendidikan = 0;
    double tunjangan_lembur = 0;

    if (golongan == 1) {
        tunjangan_golongan = 0.05 * gaji_pokok;
    } 
    else if (golongan == 2) {
        tunjangan_golongan = 0.10 * gaji_pokok;
    } 
    else if (golongan == 3) {
        tunjangan_golongan = 0.15 * gaji_pokok;
    }

    if (pendidikan == 1) {
        tunjangan_pendidikan = 0.05 * gaji_pokok;
    } 
    else if (pendidikan == 2) {
        tunjangan_pendidikan = 0.10 * gaji_pokok;
    } 
    else if (pendidikan == 3) {
        tunjangan_pendidikan = 0.20 * gaji_pokok;
    } 
    else if (pendidikan == 4) {
        tunjangan_pendidikan = 0.30 * gaji_pokok;
    }

    int jam_harian = 8;
    int hari_kerja = 24;
    double jam_normal_per_bulan = jam_harian * hari_kerja;
    double jam_lembur = jam_kerja - jam_normal_per_bulan;

    if (jam_lembur < 0) {
        jam_lembur = 0;
    }

    tunjangan_lembur = jam_lembur * 3500;
    double gaji_total = gaji_pokok + tunjangan_golongan + tunjangan_pendidikan + tunjangan_lembur;

    cout << "\nRincian Gaji Karyawan:" << endl;
    cout << "Nama Karyawan: " << nama << endl;
    cout << "Gaji Pokok: " << gaji_pokok << endl;
    cout << "Tunjangan Golongan: " << tunjangan_golongan << endl;
    cout << "Tunjangan Pendidikan: " << tunjangan_pendidikan << endl;
    cout << "Tunjangan Lembur: " << tunjangan_lembur << endl;
    cout << "Total Gaji: " << gaji_total << endl;

    return 0;
}

