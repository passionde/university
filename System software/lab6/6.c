#include <stdio.h>
#include <math.h>

int main() {
    long double eps = 1e-13; // Точность
    long double sum = 0;
    long double h = 0.02;
    long double old_I = 0;
    long double x = 0;

    do {
        old_I = sum;
        sum = 0; h /= 2.0;
        for (int i = 0; i < 2 / h; i++)
        {
            x = i * h + h / 2.0;
            if (x <= 1) {
                sum += cos(x)*exp(-pow(x, 2));
            } else {
                sum += log(x + 1) - sqrt(4 - pow(x, 2));
            }
        }
        sum *= h;
    } while (fabsl(sum - old_I) > eps);
    printf("%.20Lf\n\n", sum);
    return 0;
}