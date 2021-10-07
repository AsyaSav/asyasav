#include <math.h>
#include <iostream>

using namespace std;

int main()
{
    float x1, x2, a, b, c, D;
    cin>> a>> b>> c;
    D = b * b - 4 * a * c;
    if (D >= 0) {
        x1 = (-b + sqrt(D)) / 2 * a;
        if (D == 0) {    
            cout << x1;
        }
        else {
        x2 = (-b - sqrt(D)) / 2 * a;
        cout<<x1<<x2;
    }
    }
}