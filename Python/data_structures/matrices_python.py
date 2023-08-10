class List:
    def __init__(self):
        self.lst = []
        self.size = 0

    def inser_list(self, size):
        self.size = size

        for posicao in range(self.size):
            value = input(f"Insira um valor - Posição: {posicao}: ")
            self.lst.append(value)

    def show_list(self):
        print(self.lst)

    def clear_list(self):
        self.lst.clear()


class Matrice:
    def __init__(self):
        self.matr = []
        self.lines = 0
        self.collumns = 0

    def insert_matrice(self, lin, col):
        self.lines = lin
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

    def menu_structure_options(self, type_structure):
        # Default menu
        print(f"\n1 - Inserir {type_structure}")
        print(f"2 - Mostrar {type_structure}")
        print(f"3 - Limpar {type_structure}")
        print("0 - Sair")
        option = input("\nEscolha uma das opções acima: ")
        print("")

        # Option to insert the data in the structure
        if option == "1":

            if type_structure == "matriz":
                line = input("Quantas linhas vai ter? ")
                collumn = input("Quantas colunas vai ter? ")
                print("")
                self.matr.insert_matrice(int(line), int(collumn))

            elif type_structure == "lista":
                size = input("Qual vai ser o tamanho da lista? ")
                print("")
                self.lst.inser_list(int(size))

        # Option to show the data in the structure
        elif option == "2":

            if type_structure == "matriz":
                self.matr.show_matrice()

            elif type_structure == "lista":
                self.lst.show_list()

        # Option to clear the data in the structure
        elif option == "3":

            if type_structure == "matriz":
                self.matr.clear_matrice()

            elif type_structure == "lista":
                self.lst.clear_list()

        # Option to exit
        elif option == "0":
            return True

        # Unavailable option
        else:
            print("Opção indisponível!")
            return True
        
        return False

    def show_main_menu(self):
        exit_main = False

        while exit_main == False :
            # Main menu
            print("\n1 - Usar matriz")
            print("2 - Usar lista")
            print("0 - Sair")
            option = input("\nEscolha uma das opções acima: ")

            exit_matrice = False
            exit_list = False

            # Matrice structure menu options
            if option == "1":
                while exit_matrice == False:
                    exit_matrice = self.menu_structure_options("matriz")

            # List structure menu options
            elif option == "2":
                while exit_list == False:
                    exit_list = self.menu_structure_options("lista")    

            # Option to exit
            elif option == "0":
                    exit_main = True
            
            # Unavailable option
            else:
                print("Opção indisponível!")

            if exit_main is True:
                    print("Interrompendo programa...")
                    break

menu = Menu()
menu.show_main_menu()
