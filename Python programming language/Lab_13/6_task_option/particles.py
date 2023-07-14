class Base:
    h = 6.62607015e-27
    c = 299792458

    def calc_specific_charge(self):
        return self.q / self.m

    def calc_compton_wavelength(self):
        return self.h / (self.m / self.c)


class Electron(Base):
    q = 1.60217663e-19
    m = 9.1093837e-31



class Neutron(Base):
    q = 0
    m = 1.67262192e-27


class Proton(Base):
    q = 1.60217663e-19
    m = 1.67262192e-27