from typing import List

class BlockProcessor:
    """Procesa bloques de números separados por ceros."""
    
    def __init__(self, array: List[int]):
        self.array = array
    
    def process_blocks(self) -> str:
        """
        Procesa los bloques, ordena números y retorna resultado.
        
        Returns:
            str: Bloques ordenados separados por espacios
        """
        if not self.array:
            return "X"
        
        blocks = self._split_into_blocks()
        sorted_blocks = [self._sort_block(block) for block in blocks]
        return " ".join(sorted_blocks)
    
    def _split_into_blocks(self) -> List[List[int]]:
        """Divide el arreglo en bloques usando 0 como separador."""
        blocks = []
        current_block = []
        
        for num in self.array:
            if num == 0:
                blocks.append(current_block[:])  # Copia del bloque actual
                current_block = []
            else:
                current_block.append(num)
        
        # Agregar el último bloque
        blocks.append(current_block)
        return blocks
    
    def _sort_block(self, block: List[int]) -> str:
        """Ordena un bloque y lo convierte a string."""
        if not block:
            return "X"
        
        sorted_numbers = sorted(block)
        return "".join(map(str, sorted_numbers))
