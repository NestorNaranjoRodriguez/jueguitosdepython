import subprocess
import sys
import os

def mostrar_menu():
    print("\n" + "═" * 55)
    print("🎮          BIENVENIDO AL MENÚ DE JUEGOS          🎮")
    print("═" * 55)
    print("1. 🎲 Juego de Azar con Dados")
    print("   Lanza dados, suma puntos y compite contra la suerte.")
    print()
    print("2. 🪨 Piedra, 📄 Papel, ✂️ Tijera, 🦎 Lagarto, 🖖 Spock")
    print("   ¡La versión épica del clásico! Incluye lagarto y Spock.")
    print()
    print("3. 🐍 Snake")
    print("   Controla una serpiente y come manzanas sin chocar.")
    print()
    print("4. 🃏 Blackjack")
    print("   Juega contra el crupier y intenta acercarte a 21 sin pasarte.")
    print()
    print("5. 🚪 Salir")
    print("═" * 55)

def ejecutar_juego(ruta_script, nombre_juego, descripcion):
    if not os.path.isfile(ruta_script):
        print(f"❌ Error: No se encontró el archivo '{ruta_script}'.")
        return
    
    print("\n" + "─" * 50)
    print(f"🎮 ¡BIENVENIDO A {nombre_juego.upper()}!")
    print("─" * 50)
    print(f"📌 {descripcion}")
    print("¡Diviértete y buena suerte!\n")

    try:
        # Ejecutar el script como subproceso (en la misma terminal)
        subprocess.run([sys.executable, ruta_script])
    except KeyboardInterrupt:
        print("\n⏸️ Juego interrumpido por el usuario.")
    except Exception as e:
        print(f"💥 Error inesperado al ejecutar '{nombre_juego}': {e}")

def main():
    # Definimos los juegos como lista de tuplas: (número, archivo, nombre, descripción)
    lista_juegos = [
        (1, "dados.py", "Juego de Azar con Dados", 
         "Lanza dados virtuales, acumula puntos y gana por suerte o estrategia."),
        (2, "pptls.py", "Piedra, Papel, Tijera, Lagarto, Spock", 
         "Versión ampliada del clásico: ahora con reglas de Sheldon Cooper 😎."),
        (3, "snake.py", "Snake", 
         "Guía a la serpiente para comer manzanas y crecer sin tocar las paredes ni a sí misma."),
        (4, "blackjack.py", "Blackjack", 
         "Intenta sumar 21 puntos o acercarte lo más posible sin pasarte. ¡Desafía al crupier!")
    ]

    while True:
        mostrar_menu()

        try:
            opcion = int(input("🔹 Elige una opción (1-5): "))
        except ValueError:
            print("⚠️  Entrada inválida. Por favor, ingresa un número entero.")
            continue

        # Procesar la opción elegida
        if opcion == 5:
            print("\n👋 ¡Gracias por jugar! ¡Hasta la próxima aventura! 👋\n")
            break

        # Buscar el juego seleccionado usando un for + if
        juego_encontrado = False
        for num, archivo, nombre, desc in lista_juegos:
            if opcion == num:
                ejecutar_juego(archivo, nombre, desc)
                juego_encontrado = True
                break

        if not juego_encontrado:
            print("❌ Opción no válida. Por favor, elige 1, 2, 3, 4 o 5.")

        # Pausa antes de volver al menú
        input("\n➡️ Presiona Enter para regresar al menú principal...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()