class Line:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2
        
    
    def next(self, s):
        index_next = self.arr1.index(s) + 1
        print(self.arr1[index_next]) 
    
    def prev(self, s):
        index_prev = self.arr1.index(s) - 1
        print(self.arr1[index_prev])

    def next_exp(self, s):
        index_current = self.arr1.index(s)
        station_next_exp = ""
        
        for station in self.arr1[index_current+1:]:
            if station in self.arr2:
                station_next_exp = station
                break
            
        print(station_next_exp)
    
    
    def prev_exp(self, s):
        index_current = self.arr1.index(s)
        station_prev_exp = ""       

        for station in self.arr1[:index_current][::-1]:
            if station in self.arr2:
                station_prev_exp = station
                break
        
        print(station_prev_exp)


class Line2(Line):
    def next(self, s):
        if s not in self.arr1:
            print("no such station exists.")
            return
        elif s == self.arr1[-1]:
            print("input is a terminal station.")
            return
        
        super().next(s)
    
    
    def prev(self, s):
        if s not in self.arr1:
            print("no such station exists.")
            return
        elif s == self.arr1[0]:
            print("input is a terminal station.")
            return
        
        super().next(s)
        
    
    def next_exp(self, s):
        if s not in self.arr1:
            print("no such station exists.")
            return
        elif s not in self.arr2:
            print("express does not stop at this station.")
        elif s == self.arr2[-1]:
            print("input is a terminal station.")
        else:
            super().next_exp(s)
            
    
    def prev_exp(self, s):
        if s not in self.arr1:
            print("no such station exists.")
            return
        elif s not in self.arr2:
            print("express does not stop at this station.")
        elif s == self.arr2[0]:
            print("input is a terminal station.")
        else:
            super().prev_exp(s)


exec(input())
