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
        
        
    def __eq__(self, other):
        if not isinstance(other, Comp):
            return NotImplemented
        
        if ((self.real)**2 + (self.imag)**2)**0.5 == ((other.real)**2 + (other.imag)**2)**0.5:
            return True
        return False

    
    def __lt__(self, other):
        if not isinstance(other, Comp):
            return NotImplemented
        
        return ((self.real)**2 + (self.imag)**2)**0.5 < ((other.real)**2 + (other.imag)**2)**0.5

    
    def __add__(self, other):
        if not isinstance(other, Comp):
            return NotImplemented
        
        if self.imag + other.imag == 0:
            return str(self.real + other.real)
        elif self.imag + other.imag < 0:
            return f"{self.real + other.real} - {abs(self.imag + other.imag)}i"
        return f"{self.real + other.real} + {self.imag + other.imag}i"

    
    def __mul__(self, other):
        if not isinstance(other, Comp):
            return NotImplemented

        if self.real * other.imag + self.imag * other.real == 0:
            return str((self.real * other.real) - (self.imag * other.imag))
        elif self.real * other.imag + self.imag * other.real < 0:
            return f"{(self.real * other.real) - (self.imag * other.imag)} - {abs(self.real * other.imag + self.imag * other.real)}i"
        return f"{(self.real * other.real) - (self.imag * other.imag)} + {self.real * other.imag + self.imag * other.real}i"


exec(input())
