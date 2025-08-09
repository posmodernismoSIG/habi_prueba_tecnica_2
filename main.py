from logic import BlockProcessor
from tests import TestBlockProcessor
import sys
import unittest

def run():
    """Función de demostración del procesador."""
    print("=== Procesador de Bloques de Números ===")
    print("Ingresa números separados por comas (ej: 1,3,2,0,7,8):")
    
    try:
        entrada = input("Tu arreglo: ")
        array = [int(x.strip()) for x in entrada.split(",")]
        processor = BlockProcessor(array)
        resultado = processor.process_blocks()
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingresa solo números separados por comas")

def run_tests():
    """Ejecuta los tests desde la carpeta tests."""
    try:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestBlockProcessor)
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
    except ImportError:
        print("Error: No se encontró el archivo tests/test.py")
        print("Asegúrate de que existe la carpeta 'tests' con el archivo 'test.py'")


if __name__ == "__main__":
    # Ejecutar demostración

    
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Ejecutar solo tests
       run_tests()
    else:
        # Ejecutar solo demostración
        run()
        print("\n" + "="*50 + "\n")
