import subprocess
import sys

def run_tests():
    print("\n🔍 Ejecutando pruebas...\n")
    resultado = subprocess.run(["python", "-m", "pytest", "tests/"], capture_output=True, text=True)
    
    if resultado.returncode == 0:
        print("✅ ¡Todos los tests pasaron! Tu solución es correcta. 🎉")
    else:
        print("❌ Algunas pruebas fallaron. Revisa tu código.")
        print(resultado.stdout)  # Muestra detalles del error

if __name__ == "__main__":
    run_tests()
