from ctypes import c_double, CDLL


my_functions = CDLL("./c_shared_lib.so")
my_functions.func_n_a.argtypes = [c_double, c_double]
my_functions.func_n_a.restype = c_double

print(my_functions.func_n_a(1000.0, 1000.0))
