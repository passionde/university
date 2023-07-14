#include <math.h>

double func_f(double x) {
  return exp(sin(x)) - x;
}

double func_g(double x) {
  return log(1.0 + sqrt(x)) - cos(x);
}

double func_a_ij(double i){
  return fabs(func_f(i) + func_g(i));
}


double func_n_a(double m, double n){
  m = fmin(m, n);
  double max_value = 0.0;

  for (double i = 0.0; i <= m; i++) {
    max_value = fmax(max_value, func_a_ij(i));
  }
  return sqrt(max_value);
}

// $ gcc task_4_lib_c.c -fPIC -shared -o c_shared_lib.so -lm -Ofast -march=native
