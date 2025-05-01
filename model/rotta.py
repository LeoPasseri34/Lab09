from dataclasses import dataclass

@dataclass
class Rotta:
    aeroporto1: str
    aeroporto2: str
    distanza: float
    numVoli: int

    def __hash__(self):
        return hash((self.aeroporto1, self.aeroporto2))

    def __str__(self):
        return f"La rotta {self.aeroporto1} - {self.aeroporto2} è stata percorsa {self.numVoli} volte con una distanza media di {self.distanza} miglia"

    def __eq__(self, other):
        return ((self.aeroporto1 == other.aeroporto1 and self.aeroporto2 == other.aeroporto1) or
                (self.aeroporto1 == other.aeroporto2 and self.aeroporto2 == other.aeroporto2))