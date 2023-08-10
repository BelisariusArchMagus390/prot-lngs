class List:
    def __init__(self):
        self.list = []
        self.size = 0

    def inser_list(self, size):
        self.size = size

        for posicao in range(self.size):
            value = input(f"Insira um valor - Posição: {posicao}: ")
            self.list.append(value)

    def show_list(self):
        print(self.list)

    def clear_list(self):
        self.list.clear()


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
                value = input(f"Insira um valor - Posição: linha: {line}, coluna: {collumn}: ")
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

class Menu():
    def __init__(self):
        self.matr = Matrice()
        self.lst = List()

    def menu_otions(self, type):
        # Menu options
        print("\n1 - Inserir {type}")
        print("2 - Mostrar {type}")
        print("3 - Limpar {type}")
        print("0 - Sair")
        option2 = input("\nEscolha uma das opções acima: ")
        print("")

        if option2 == "1":
            if type == "matrice":
                line = input("Quantas linhas vai ter? ")
                collumn = input("Quantas colunas vai ter? ")
                print("")
                self.matr.insert_matrice(int(line), int(collumn))
            elif type == "list":
                pass
        elif option2 == "2":
            if type == "matrice":
                self.matr.show_matrice()
            elif type == "list":
                pass
        elif option2 == "3":
            if type == "matrice":
                self.matr.clear_matrice()
            elif type == "list":
                pass
        elif option2 == "0":
            return True
        else:
            print("Opção indisponível!")
            return True

    def show_main_menu(self):
        exit_main = False

        while exit_main == False :

            print("\n1 - Usar matriz")
            print("2 - Usar lista")
            print("0 - Sair")
            option1 = input("\nEscolha uma das opções acima: ")

            exit_matrice = False
            exit_list = False

            if option1 == "1":
                while exit_matrice == False:
                    

                    if exit_matrice is True:
                        break
            
            elif option1 == "2":
                while exit_list == False:
                    # Menu options of list
                    print("\n1 - Inserir lista")
                    print("2 - Mostrar lista")
                    print("3 - Limpar lista")
                    print("0 - Sair")
                    option2 = input("\nEscolha uma das opções acima: ")
                    print("")

                    if option2 == "1":
                        size = input("Qual vai ser o tamanho da lista? ")
                        print("")
                        self.lst.inser_list(int(size))
                    elif option2 == "2":
                        self.lst.show_list()
                    elif option2 == "3":
                        self.lst.clear_list()
                    elif option2 == "0":
                        exit_list = True
                    else:
                        print("Opção indisponível!")

                    if exit_list is True:
                        break

            elif option1 == "0":
                    exit_main = True
            else:
                print("Opção indisponível!")

            if exit_main is True:
                    print("Interrompendo programa...")
                    break

menu = Menu()
menu.show_menu()

            
