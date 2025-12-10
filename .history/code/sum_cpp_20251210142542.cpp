#include <iostream>
#include <cstdlib>
using namespace std;

int main(int argc, char* argv[]) {
    int a = 0, b = 0;
    if (argc >= 3) {
        a = atoi(argv[1]);
        b = atoi(argv[2]);
    } else {
        cout << "Enter first number: ";
        if (!(cin >> a)) return 1;
        cout << "Enter second number: ";
        if (!(cin >> b)) return 1;
    }

    cout << "Sum: " << (a + b) << endl;
    return 0;
}
