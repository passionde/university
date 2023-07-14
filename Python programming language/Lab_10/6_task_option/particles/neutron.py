q = 0
m = 1.67262192e-27
h = 6.62607015e-27
c = 299792458


def calc_specific_charge():
    return q / m


def calc_compton_wavelength():
    return h / (m / c)
