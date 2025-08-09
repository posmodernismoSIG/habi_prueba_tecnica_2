from logic import BlockProcessor
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


if __name__ == "__main__":
    # Ejecutar demostración
    run()
    print("\n" + "="*50 + "\n")
    
