class Temperature:
    def __init__(self, celsius):
        self._c = celsius

    @property
    def celsius(self):
        return self._c

    @property
    def fahrenheit(self):
        return (self._c * 9/5) + 32
