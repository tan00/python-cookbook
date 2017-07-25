from time import localtime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

   
    @classmethod
    def today(cls):
        t = localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_mday)


d = Date.today()


