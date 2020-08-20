"""
class Dollars:
    def __init__(self, amt: float, currency: str):
        
    def __add__(self, other: "Money"):
        if self.currency == other.currency:
            return self.amt + other.amt
        else:
            ValueError("")
    def __eq__(self, other: "Money"):
        rounded_amt1 = round(self.amt, 2)
        rounded_amt2 = round(other.amt, 2)
        if rounded_amt1 == rounded_amt2:
            return
        pass
    def __str__(self):
        pass
"""

def my_range(start: int, limit: int, increment=1):
    new_list = []
    while start < limit:
        new_list.append[start]
        start += increment
    yield new_list
list(my_range(-1, 3))