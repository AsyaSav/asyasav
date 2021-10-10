#include <math.h>
#include <iostream>

using namespace std;

int main()
{
    float x1, x2,  D;
    int a, b, c;
    cin>> a>> b>> c;
    D = b * b - 4 * a * c;
    if ((b * b - 4 * a * c) >= 0) {
        x1 = (-b + sqrt(D)) /( 2 * a);
        if ((b * b - 4 * a * c)== 0) {    
            cout << x1;
        }
        else {
        x2 = (-b - sqrt(D)) / (2 * a);
        cout<<x1<<x2;
    }
    }
}