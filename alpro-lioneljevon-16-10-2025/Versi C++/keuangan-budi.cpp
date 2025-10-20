#include <iostream>
#include <iomanip>
using namespace std;

void pendapatan_budi(double gaji, double jam, double &pendapatan_kotor, double &pajak, double &pendapatan_bersih) {
    pendapatan_kotor = gaji * jam * 5;
    pajak = 0.14 * pendapatan_kotor;
    pendapatan_bersih = pendapatan_kotor - pajak;
}

void pengeluaran_budi(double pendapatan_bersih, double &pengeluaran_baju, double &pengeluaran_alat_tulis, double &sisa_belanja) {
    pengeluaran_baju = 0.1 * pendapatan_bersih;
    pengeluaran_alat_tulis = 0.01 * pendapatan_bersih;
    sisa_belanja = pendapatan_bersih - (pengeluaran_baju + pengeluaran_alat_tulis);
}

void sedekah_budi(double sisa_belanja, double &sedekah, double &sedekah_yatim, double &sedekah_dhuafa) {
    sedekah = 0.25 * sisa_belanja;
    sedekah_yatim = 0.3 * sedekah;
    sedekah_dhuafa = sedekah - sedekah_yatim;
}

int main() {
    cout << "=== Program Perhitungan Keuangan Budi Selama Liburan ===\n" << endl;

    double gaji_per_jam, jam_minggu;
    cout << "Masukkan gaji per jam (Rp): ";
    cin >> gaji_per_jam;
    cout << "Masukkan jumlah jam kerja per minggu: ";
    cin >> jam_minggu;

    double pendapatan_kotor, pajak, pendapatan_bersih;
    double pengeluaran_baju, pengeluaran_alat_tulis, sisa_belanja;
    double sedekah, sedekah_yatim, sedekah_dhuafa;

    pendapatan_budi(gaji_per_jam, jam_minggu, pendapatan_kotor, pajak, pendapatan_bersih);
    pengeluaran_budi(pendapatan_bersih, pengeluaran_baju, pengeluaran_alat_tulis, sisa_belanja);
    sedekah_budi(sisa_belanja, sedekah, sedekah_yatim, sedekah_dhuafa);

    cout << "\nRincian Keuangan Budi" << endl;
    cout << fixed << setprecision(0);
    cout.imbue(locale(""));

    cout << "Pendapatan Kotor: Rp " << pendapatan_kotor << endl;
    cout << "Pajak (14%): Rp " << pajak << endl;
    cout << "Pendapatan Bersih: Rp " << pendapatan_bersih << endl;
    cout << "Pengeluaran untuk Baju: Rp " << pengeluaran_baju << endl;
    cout << "Pengeluaran untuk Alat Tulis: Rp " << pengeluaran_alat_tulis << endl;
    cout << "Sisa Belanja: Rp " << sisa_belanja << endl;
    cout << "Total Sedekah (25% dari Sisa Belanja): Rp " << sedekah << endl;
    cout << "  - Sedekah untuk Anak Yatim (30% dari Total Sedekah): Rp " << sedekah_yatim << endl;
    cout << "  - Sedekah untuk Dhuafa: Rp " << sedekah_dhuafa << endl;

    return 0;
}
