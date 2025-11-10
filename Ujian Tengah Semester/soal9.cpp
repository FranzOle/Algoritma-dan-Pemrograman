#include <iostream>
#include <string>

using namespace std;

string misteri(int a) {
    if (a == 0) {
        return "";
    } else {
        int b = a % 2;
        string str;

        if (b == 0) {
            str = "0";
        } else {
            str = "1";
        }

        return misteri(a / 2) + str;
    }
}

int main() {
    cout << "Hasil konversi desimal 73 ke biner: " << misteri(73) << endl;
    
    cout << "Hasil konversi desimal 13 ke biner: " << misteri(13) << endl;
    cout << "Hasil konversi desimal 0 ke biner: " << misteri(0) << endl;

    return 0;
}