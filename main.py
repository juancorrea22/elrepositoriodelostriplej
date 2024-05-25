from chat_to_bin import char_to_binary
from word_to_binary import word_to_binary
from ascii_a_binary import binary_to_ascii

def main():
    while True:
        print("Menú de opciones:")
        print("1. Generar la representación en byte de un carácter")
        print("2. Generar la representación en byte de una palabra")
        print("3. Generar la representación ASCII de un byte")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            char = input("Ingrese un carácter: ")
            if len(char) == 1:
                print(f"Representación en byte: {char_to_binary(char)}")
            else:
                print("Debe ingresar un solo carácter.")
        
        elif opcion == '2':
            word = input("Ingrese una palabra: ")
            print(f"Representación en byte: {word_to_binary(word)}")
        
        elif opcion == '3':
            binary = input("Ingrese un byte en formato binario: ")
            if len(binary) == 8 and set(binary).issubset({'0', '1'}):
                print(f"Representación ASCII: {binary_to_ascii(binary)}")
            else:
                print("Debe ingresar un byte válido en formato binario (8 bits).")
        
        elif opcion == '4':
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()