class Fraction():
    def __init__(self,num,dem):
        self.num = num
        self.dem = dem
    def __str__(self):
        return f"{str(self.num)} / {str(self.dem)}"
    def gcd(self):
        if self.num % self.dem == 0:
            print(self.dem)
        else:
            while self.num % self.dem != 0:
                temp = self.num % self.dem
                self.num = self.dem
                self.dem = temp
                if self.num % self.dem == 0:
                    print(self.dem)
myfrac = Fraction(24,6)
myfrac.gcd()