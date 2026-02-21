class Distance:
    def __init__(self, km):
        if not isinstance(km, (int, float)):
            raise TypeError(f"Not is int of float type")

        self.km = float(km)

    def __str__(self):
        return f"Distance: {self.km:.4g} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km:.4g})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

        if isinstance(other, (int, float)):
            return Distance(self.km + other)

        return NotImplemented


    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += float(other.km)
            return self
        elif isinstance(other, (int, float)):
            self.km += float(other)
            return self
        else:
            raise TypeError(f"Not is int of float type")


    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Distance(self.km * scalar)
        else:
            raise TypeError(f"Not is int of float type")


    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar == 0:
            raise ZeroDivisionError(f"Not is int of float type")

        if isinstance(scalar, (int, float)):
            return Distance(round(self.km / scalar ,2))
        else:
            raise TypeError(f"Not is int of float type")


    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            return NotImplemented


    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            return NotImplemented
