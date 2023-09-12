class Neuron:
    def __activation(self, v):
        return v <= 0

    def predict(self, x1, x2):
        w1, w2 = 1, 1
        s = x1 * w1 + x2 * w2
        return self.__activation(s)


if __name__ == "__main__":
    cases = [
        ((0, 0), 1),
        ((0, 1), 0),
        ((1, 0), 0),
        ((1, 1), 0),
    ]

    n = Neuron()

    for args, result in cases:
        if n.predict(*args) == result:
            print("Test passed")
        else:
            print("Test fail")
