#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand: str = None, size: int = None):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
            print(f"Pair of {self.brand} shoes (size {size}) added.")
        else:
            print("size must be an integer")
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")