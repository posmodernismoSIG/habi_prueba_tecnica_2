
from  logic import BlockProcessor
import unittest

class TestBlockProcessor(unittest.TestCase):
    """Tests para la clase BlockProcessor."""
    
    def test_ejemplo_basico(self):
        """Test con el ejemplo dado en el enunciado."""
        processor = BlockProcessor([1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1])
        resultado = processor.process_blocks()
        self.assertEqual(resultado, "123 1378 167")
    
    def test_bloque_vacio(self):
        """Test con bloques vacíos."""
        processor = BlockProcessor([2, 1, 0, 0, 3, 4])
        resultado = processor.process_blocks()
        self.assertEqual(resultado, "12 X 34")
    
    def test_sin_ceros(self):
        """Test sin separadores."""
        processor = BlockProcessor([3, 1, 4, 2])
        resultado = processor.process_blocks()
        self.assertEqual(resultado, "1234")
    
    def test_solo_ceros(self):
        """Test con solo ceros."""
        processor = BlockProcessor([0, 0, 0])
        resultado = processor.process_blocks()
        self.assertEqual(resultado, "X X X X")
    
    def test_arreglo_vacio(self):
        """Test con arreglo vacío."""
        processor = BlockProcessor([])
        resultado = processor.process_blocks()
        self.assertEqual(resultado, "X")
    
    def test_un_elemento(self):
        """Test con un solo elemento."""
        processor = BlockProcessor([5])
        resultado = processor.process_blocks()
        self.assertEqual(resultado, "5")
    
    def test_numeros_repetidos(self):
        """Test con números repetidos en bloques."""
        processor = BlockProcessor([3, 3, 1, 0, 9, 9, 2])
        resultado = processor.process_blocks()
        self.assertEqual(resultado, "133 299")