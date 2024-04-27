class Comp:
    def __init__(self, a, b):
        self.real = a
        self.imag = b
    
    
    def __str__(self):
        if self.imag == 0:
            return str(self.real)
        elif self.imag < 0:
            return f"{self.real} - {abs(self.imag)}i"
        else:
            return f"{self.real} + {abs(self.imag)}i"

exec(input())
