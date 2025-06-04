from Game.game import *

# Menu
print("\n\n--------[ Hexadecimal Game ]--------")
print(" [1] - Counter")
print(" [2] - Hexadecimal to Binary")
print(" [3] - Binary to Hexadecimal")
print(" [4] - Quit")
print("[----------------------------------]")

option = int(input("Choose an option: "))

if option == 1:
    counting()
elif option == 2:
    translate_hexadecimal_to_binary()
elif option == 3:
    translate_binary_to_hexadecimal()
elif option == 4:
    pass
