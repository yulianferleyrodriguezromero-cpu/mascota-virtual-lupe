import time
import os

# Colores para consola
class Color:
    RESET = "\033[0m"
    ROJO = "\033[91m"
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    CIAN = "\033[96m"
    NEGRITA = "\033[1m"

class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100
        self.hambre = 0
        self.felicidad = 100
        print(f"{Color.CIAN}🐶 ¡Hola! Soy {self.nombre}, tu mascota virtual.{Color.RESET}\n")
        time.sleep(1)

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def barra_estado(self, valor, maximo=100, longitud=20):
        lleno = int((valor / maximo) * longitud)
        vacio = longitud - lleno
        return f"[{Color.VERDE}{'█' * lleno}{Color.ROJO}{'░' * vacio}{Color.RESET}] {valor}/100"

    def mostrar_estado(self):
        self.limpiar_pantalla()
        print(f"{Color.NEGRITA}{Color.MAGENTA}--- ESTADO DE {self.nombre.upper()} ---{Color.RESET}")
        print(f"Energía:   {self.barra_estado(self.energia)}")
        print(f"Hambre:    {self.barra_estado(self.hambre)}")
        print(f"Felicidad: {self.barra_estado(self.felicidad)}")
        print(f"{Color.MAGENTA}------------------------------{Color.RESET}\n")

    def comer(self):
        if self.hambre <= 0:
            print(f"{Color.AMARILLO}{self.nombre} no tiene hambre 🐾{Color.RESET}")
        else:
            print(f"{Color.VERDE}{self.nombre} está comiendo 🍗...{Color.RESET}")
            time.sleep(1.5)
            self.hambre = max(self.hambre - 20, 0)
            self.energia = min(self.energia + 10, 100)
            self.felicidad = min(self.felicidad + 5, 100)
            print(f"{self.nombre} ha terminado de comer y se ve feliz 😋")

    def saltar(self):
        print(f"{Color.CIAN}{self.nombre} da un gran salto 🐕‍🦺✨{Color.RESET}")
        self.energia = max(self.energia - 10, 0)
        self.felicidad = min(self.felicidad + 10, 100)
        self.hambre = min(self.hambre + 5, 100)

    def acostarse(self):
        print(f"{Color.AZUL}{self.nombre} se acuesta a descansar 😴{Color.RESET}")
        time.sleep(2)
        self.energia = min(self.energia + 30, 100)
        self.hambre = min(self.hambre + 10, 100)
        print(f"{Color.VERDE}{self.nombre} se siente renovado 💪{Color.RESET}")

    def jugar(self):
        if self.energia <= 10:
            print(f"{Color.ROJO}{self.nombre} está muy cansado para jugar 😴{Color.RESET}")
        else:
            print(f"{Color.AMARILLO}{self.nombre} está jugando con una pelota 🎾{Color.RESET}")
            self.energia = max(self.energia - 15, 0)
            self.felicidad = min(self.felicidad + 20, 100)
            self.hambre = min(self.hambre + 10, 100)

    def dormir(self):
        print(f"{Color.AZUL}{self.nombre} está durmiendo profundamente 💤...{Color.RESET}")
        time.sleep(3)
        self.energia = 100
        self.hambre = min(self.hambre + 20, 100)
        self.felicidad = min(self.felicidad + 10, 100)
        print(f"{Color.VERDE}{self.nombre} ha despertado lleno de energía ☀️{Color.RESET}")

    def paso_del_tiempo(self):
        self.hambre = min(self.hambre + 5, 100)
        self.energia = max(self.energia - 5, 0)
        self.felicidad = max(self.felicidad - 5, 0)
        if self.hambre >= 100:
            print(f"{Color.ROJO}{self.nombre} tiene mucha hambre 😢{Color.RESET}")
        if self.energia <= 0:
            print(f"{Color.ROJO}{self.nombre} está agotado y necesita dormir 😴{Color.RESET}")

def main():
    lupe = MascotaVirtual("Lupe")

    while True:
        lupe.mostrar_estado()
        print(f"{Color.NEGRITA}--- MENÚ DE OPCIONES ---{Color.RESET}")
        print("1. Comer 🍗")
        print("2. Saltar 🐕‍🦺")
        print("3. Acostarse 😴")
        print("4. Jugar 🎾")
        print("5. Dormir 💤")
        print("6. Ver estado 📋")
        print("7. Salir 🚪")

        try:
            opcion = int(input(f"\n¿Qué quieres que haga {lupe.nombre}? 👉 "))

            lupe.limpiar_pantalla()

            if opcion == 1:
                lupe.comer()
            elif opcion == 2:
                lupe.saltar()
            elif opcion == 3:
                lupe.acostarse()
            elif opcion == 4:
                lupe.jugar()
            elif opcion == 5:
                lupe.dormir()
            elif opcion == 6:
                lupe.mostrar_estado()
            elif opcion == 7:
                print(f"\n👋 ¡Hasta luego! {lupe.nombre} te dice adiós 💖")
                break
            else:
                print(f"{Color.ROJO}⚠️ Opción no válida. Elige un número del 1 al 7.{Color.RESET}")

        except ValueError:
            print(f"{Color.ROJO}❌ Por favor, ingresa solo números del 1 al 7.{Color.RESET}")

        lupe.paso_del_tiempo()
        input(f"\nPresiona ENTER para continuar...")
        lupe.limpiar_pantalla()


if __name__ == "__main__":
    main()

