class Matrice:
    def __init__(self):
        self.matr = []
        self.lines = 0
        self.collumns = 0

    def insert_matrice(self, ln, col):
        self.lines = ln
        self.collumns = col

        for line in range(self.lines):
            lst_aux = []
            for collumn in range(self.collumns):
                value = input(f"Insira um valor aqui linha: {line}, Coluna: {collumn}: ")
                lst_aux.append(value)
            self.matr.append(lst_aux)

    def show_matrice(self):
        if len(self.matr) == 0:
            print("[ ]")
        else:
            for line in range(self.lines):
                print("| ", end="")
                message = ""
                for collumn in range(self.collumns):
                    message += f"{self.matr[line][collumn]}, "
                message = message[:-2]
                print(message, end=" ")
                print("|")

    def clear_matrice(self):
        self.matr.clear()


matr = Matrice()

exit = False

while exit == False :

    print("\n1 - Inserir matriz")
    print("2 - mostrar matriz")
    print("3 - limpar matriz")
    print("0 - Sair")
    option = input("\nEscolha uma das opções abaixo: ")
    print("")

    if option == "1":
        line = input("Quantas linhas vai ter: ")
        collumn = input("Quantas colunas vai ter: ")
        print("")
        matr.insert_matrice(int(line), int(collumn))
    elif option == "2":
        matr.show_matrice()
    elif option == "3":
        matr.clear_matrice()
    elif option == "0":
        exit = True
    else:
        print("Opção indisponível!")

    if exit is True:
        print("Interrompendo programa...")
        break

            