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


exec(input())
