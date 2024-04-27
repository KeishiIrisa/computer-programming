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


class JDate(Date): 
    def __init__(self, g, y, m, d):
        ERA_DICT = {
            "令和": [2019, 5, 1],
            "平成": [1989, 1, 8],
            "昭和": [1926, 12, 25]
            }
        self.japanese_calender = g
        self.year = ERA_DICT[g][0] + y - 1
        self.month = m
        self.day = d
        
    
    def __str__(self):
        return f"「このインスタンスは{self.japanese_calender}{self.year}年{self.month}月{self.day}日です。」"
    

exec(input())
