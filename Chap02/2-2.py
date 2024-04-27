class Date:
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d
        
        
    def is_new_year_day(self):
        if self.month == 1 and self.day == 1:
            return True
        else:
            return False
    
    
    def __str__(self):
        return f"このインスタンスは{self.year}年{self.month}月{self.day}日です。"
    
    
    def __ge__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        
        if other.year < self.year:
            return True
        elif other.year > self.year:
            return False
        else:
            if self.month > other.month:
                return True
            elif self.month < other.month:
                return False
            else:
                if self.day > other.day:
                    return True
                else:
                    return False
    
    
    def __eq__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        else:
            return False

exec(input())