import random
import time # Importar time para simular un poco de "emoción" en el lanzamiento

def juego_pares_y_nones():
    """
    Juego de Pares y Nones con dados.
    El usuario elige si juega con pares o impares.
    """
    print("🎲✨ **JUEGO: PARES Y NONES** ✨🎲")
    print("-" * 30)

    # 1. Selección de Bando
    while True:
        eleccion = input("¿Quieres jugar como **Pares (P)** o como **Impares (I)**?: ").strip().upper()
        if eleccion == 'P':
            jugador_humano_bando = 'Pares'
            jugador_maquina_bando = 'Impares'
            break
        elif eleccion == 'I':
            jugador_humano_bando = 'Impares'
            jugador_maquina_bando = 'Pares'
            break
        else:
            print("❌ Opción no válida. Por favor, ingresa 'P' para Pares o 'I' para Impares.")

    print(f"\n✅ ¡Has elegido jugar como **{jugador_humano_bando}**!")
    print(f"La máquina jugará como **{jugador_maquina_bando}**.")

    # 2. Entrada del Número de Dados con Validación
    while True:
        try:
            dados = int(input("\n¿Cuántos dados quieres lanzar (ej. 5)?: "))
            if dados > 0:
                break
            else:
                print("❌ Por favor, ingresa un número de dados mayor que cero.")
        except ValueError:
            print("❌ Entrada no válida. Por favor, ingresa un número entero.")

    # Inicialización de contadores
    puntos_humano = 0
    puntos_maquina = 0

    print(f"\n🔥 Preparando el lanzamiento de {dados} dados...")
    time.sleep(1.5) # Pausa para el efecto dramático

    # 3. Lanzamiento de Dados
    print("\n--- ¡LANZAMIENTO! ---\n")
    for i in range(1, dados + 1):
        tiro = random.randint(1, 6)
        es_par = (tiro % 2 == 0)
        resultado_str = "PAR" if es_par else "IMPAR"

        print(f"✨ Dado {i}: **{tiro}** ({resultado_str})")

        # Asignación de puntos basada en la elección del usuario
        if (es_par and jugador_humano_bando == 'Pares') or (not es_par and jugador_humano_bando == 'Impares'):
            puntos_humano += 1
            print("   --> ¡Punto para ti! 🎉")
        else:
            puntos_maquina += 1
            print("   --> Punto para la máquina. 🤖")
        
        time.sleep(0.5) # Pausa para que se vea el resultado individual

    # 4. Resultados Finales
    print("\n" + "=" * 40)
    print("🏆 **RESULTADOS FINALES** 🏆")
    print("=" * 40)
    print(f"👤 Tu Puntuación ({jugador_humano_bando}): **{puntos_humano}** puntos")
    print(f"💻 Máquina ({jugador_maquina_bando}): **{puntos_maquina}** puntos")
    print("-" * 40)

    # 5. Determinación del Ganador
    if puntos_humano > puntos_maquina:
        print("🥇🥳 ¡FELICIDADES! HAS GANADO LA PARTIDA. 🥳🥇")
    elif puntos_maquina > puntos_humano:
        print("😔 ¡Oh no! Gana la máquina. ¡Más suerte la próxima vez! 🤖")
    else:
        print("🤝 ¡EMPATE! Ha sido un enfrentamiento muy igualado. 🤝")

    print("\n" + "=" * 40)

if __name__ == "__main__":
    juego_pares_y_nones()
