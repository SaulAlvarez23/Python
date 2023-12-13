import random

def jugar_piedra_papel_tijera():
    while True:
        # Mostrar las opciones disponibles
        print("Opciones:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        print("4. Salir")

        # Obtener la elección del usuario
        eleccion_usuario = input("Elige tu opción (1-4): ")

        # Validar la entrada del usuario
        if eleccion_usuario == '4':
            print("¡Gracias por jugar! Hasta luego.")
            break
        elif eleccion_usuario not in ['1', '2', '3']:
            print("Opción no válida. Por favor, elige entre 1 y 3.")
            continue

        # Mapear la elección del usuario
        opciones = {'1': 'Piedra', '2': 'Papel', '3': 'Tijera'}
        eleccion_usuario_texto = opciones[eleccion_usuario]

        # Generar la elección aleatoria de la computadora
        eleccion_computadora = random.choice(['Piedra', 'Papel', 'Tijera'])

        # Mostrar las elecciones
        print(f"Tú elegiste: {eleccion_usuario_texto}")
        print(f"La computadora eligió: {eleccion_computadora}")

        # Determinar el ganador
        if eleccion_usuario_texto == eleccion_computadora:
            print("¡Es un empate!")
        elif (eleccion_usuario_texto == 'Piedra' and eleccion_computadora == 'Tijera') or \
             (eleccion_usuario_texto == 'Papel' and eleccion_computadora == 'Piedra') or \
             (eleccion_usuario_texto == 'Tijera' and eleccion_computadora == 'Papel'):
            print("¡Ganaste!")
        else:
            print("¡La computadora gana!")

if __name__ == "__main__":
    jugar_piedra_papel_tijera()
    
    