def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
class Fraction:
    def __init__(self, num: int, den: int) -> None:
        assert isinstance(num, int)
        assert isinstance(den, int)
        assert den != 0 
        self._num:int = num
        self._den:int = den 

    # --------- GETTERS ----------- #
    @property 
    def num(self) -> int: 
        return self._num 

    @property 
    def den(self) -> int : 
        return self._den 

    # --------- SETTERS ----------- # 
    # protect the instance attributes
    @num.setter 
    def num(self, value) -> None:
        self._num = int(value) 

    @den.setter 
    def den(self, value)-> None:
        if value == 0:
            self._den = 1 # question requirement 
        else:    
            self._den = int(value)

    def __str__(self) -> str: 
        return f"{self.num:d}/{self.den:d}"
    
    def simplify(self) :
        common: int = gcd(self.num, self.den)
        num: int = self.num // common
        den: int = self.den // common
        return Fraction(num, den)
    
    def __add__(self, other) :
        new_num: int = self.num * other.den + other.num * self.den
        new_den: int = self.den * other.den
        result: Fraction = Fraction(new_num, new_den).simplify()
        return result 
    ###END SOLUTION
    
    def __sub__(self, other)  -> "Fraction":
        ###BEGIN SOLUTION
        new_num: int = self.num * other.den - other.num * self.den
        new_den: int = self.den * other.den
        result: Fraction = Fraction(new_num, new_den).simplify()
        return result 
        ###END SOLUTION
        pass
    
    def __mul__(self, other)  -> "Fraction":
        ###BEGIN SOLUTION
        new_num: int = self.num * other.num
        new_den: int = self.den * other.den
        result: Fraction = Fraction(new_num, new_den).simplify()
        return result
        ###END SOLUTION
        pass
    
    def __eq__(self, other) -> bool:
        ###BEGIN SOLUTION
        left: Fraction = self.simplify()
        right: Fraction = other.simplify()
        return left.num == right.num and left.den == right.den
        ###END SOLUTION
        pass
    
    def __lt__(self, other) -> bool:
        ###BEGIN SOLUTION
        return self.num * other.den < other.num * self.den
        ###END SOLUTION
        pass
    
    def __le__(self, other) -> bool:
        ###BEGIN SOLUTION
        return self < other or self == other
        ###END SOLUTION
        pass
    
    def __gt__(self, other) -> bool:
        ###BEGIN SOLUTION
        return not (self <= other)
        ###END SOLUTION
        pass
    
    def __ge__(self, other) -> bool:
        ###BEGIN SOLUTION
        return not (self < other)
        ###END SOLUTION
        pass
    

f1 = Fraction(5, 6)
f2 = Fraction(3, 6)
print(f1+f2) # automatically call the __and__ function