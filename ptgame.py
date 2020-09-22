import time

# welcoming the user and asking for their name
print("Oi! Vamos fazer umas contas. :)\nMas antes, qual é o seu nome?")

user_name = input()

# long string explaining how the program works. (Brazilian portuguese)
mutiply_explanation = f"Este programa multiplicará números inseridos por você,\ncamarada {user_name}, mas não usará a operação de multiplicação.\nEu (o computador), farei uma adição através de um loop!\nMultiplicação é uma adição repetida.\nPor exemplo: 4 x 3 = 4 + 4 + 4.\nCerto? Vamos lá!\n"

# asking if the user wants to know how the game works, S for yes, N for No
wanna_know = input(f"{user_name}, você gostaria de saber como este jogo funciona?\nS ou N ^-^\n").capitalize()

# if the user wants to know, then it'll print the explanation. else, will go straight to the game
if wanna_know == "S":
    print(mutiply_explanation)
else:
    print("Ok, direto ao ponto! Vamos lá.")

# initializing the answer to run the game again
play_again = "S"

# initializing the product
product = 0

# while loop that will execute while the user wants to play again
while play_again != "N":
    user_int_1 = int(input("Insira um número:\n"))
    user_int_2 = int(input("Insira agora mais um número:\n"))

    print(f"Primeiro número: [{user_int_1}]")
    print(f"Segundo número: [{user_int_2}]")

    # just playing around with the time module! the last line says that the PC is summing a million numbers
    for i in range(0,3):
        print("\nComputando...")
        time.sleep(.5)
    print("\n....Somando um milhão de números...\n")
    time.sleep(2.8)

    for times in range(user_int_1):
        product += user_int_2

    # thanking the user for their patience and showing the results while joking that it takes a lot of effort.
    print(f"Agradecemos sua paciência, {user_name}!\nUfa, multiplicar sem usar multiplicação é bem difícil.\nMas vamos aos números!\n\nSeus resultados: {user_int_1} x {user_int_2} = {product}")

    # asking if the user want to play again this answer will break the loop if he while evaluates to False.
    play_again = input("Gostaria de jogar de novo? S ou N:\n")
    play_again = play_again.capitalize()

print(f"Agradecemos sua participação, {user_name}!\nAté logo :)")