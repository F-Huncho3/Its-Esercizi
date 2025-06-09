import re
from typing import Self

class Indirizzo:
    
    via:str
    
    civico:int

    def __init__(self, via:str, civico:int) -> Self:
        self.via = via
        self.civico = civico
    
    def via(self) -> str:
        return self.via
    
    def civico(self) -> int:
        return self.civico

    def __str__(self) -> str:
        return f"{self.via()}, {self.civico()}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Indirizzo) or hash(self) != hash(other):
            return False
        else:
            return (self.via(), self.civico() ) == (other.via(), other.civico())

    def __hash__(self)->int: 
        return hash((self.via(), self.civico()))