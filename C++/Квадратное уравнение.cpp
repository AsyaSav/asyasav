#include <math.h>
#include <iostream>

using namespace std;

int main()
{
    float x1, x2, D, a, b, c;
    cin >> a >> b >> c;
    if ((a == 0) and (b != 0) and (c != 0)) {
        x1 = -c / b;

    }
    if ((b == 0) and (a != 0) and (c != 0)) {
        x1 = sqrt(-c / a);
    }
    if ((c == 0) and (b != 0) and (a != 0)) {
        x1 = -b / a;
        x2 = 0;
    }
    if ((b == 0) and (c == 0) and (a != 0)) {
        x1 = 0;
    }
    if ((b == 0) and (c == 0) and (a == 0)) {
        cout << "x может принять любое значение ";
    }
    if ((b == 0) and (c != 0) and (a == 0)) {
        cout << "решений нет";
    }
    if ((b != 0) and (c == 0) and (a == 0)) {
        x1 = 0;
    }
    if ((b != 0) and (c != 0) and (a != 0)) {
        D = b * b - 4 * a * c;
        if (D >= 0) {
            x1 = (-b + sqrt(D)) / (2 * a);
            if (D == 0) {
            }
            else {
                x2 = ((-b - sqrt(D))) / (2 * a);
               
            }
        }
    } 
    cout << x1 << x2;
}