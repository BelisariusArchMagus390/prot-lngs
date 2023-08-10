class List:
    def __init__(self):
        self.lst = []
        self.size = 0

    def create_list(self, size):
        self.size = size

        for posicao in range(self.size):
            value = input(f"Insira um valor - Posição: {posicao}: ")
            self.lst.append(value)

    def insert_element_in_list(self, element, idx):
        if self.size <= idx:
            self.lst[idx] = element
        else:
            return False

    def search_element_in_list(self, element):
        for element_list in self.lst:
            if element_list == element:
                return [element_list, self.lst.index(element_list)]

        return False

    def delete_element_in_list(self, element):
        value = self.search_element_in_list(element)
        if value is not False:
            self.lst.remove(value[0])

    def show_size_list(self):
        return self.size

    def show_list(self):
        print(self.lst)

    def clear_list(self):
        self.lst.clear()


class Matrice:
    def __init__(self):
        self.matr = []
        self.lines = 0
        self.collumns = 0

    def create_matrice(self, lin, col):
        self.lines = lin
        self.collumns = col

        for line in range(self.lines):
            lst_aux = []
            for collumn in range(self.collumns):
                value = input(f"Insira um valor - Posição: linha: {line}, coluna: {collumn}: ")
                lst_aux.append(value)
            self.matr.append(lst_aux)

    def insert_element_in_matrice(self, element, line, collumn):
        if line <= self.lines and collumn <= self.collumns:
            self.matr[line][collumn] = element
        else:
            return False

    def search_element_in_matrice(self, element):
        for line in self.matr:
            for element_matr in line:
                if element_matr == element:
                    return [element_matr, self.matr.index(line), self.matr.index(element_matr)]

        return False

    def delete_element_in_matrice(self, element):
        value = self.search_element_in_matrice(element)
        if value is not False:
            line = value[1]
            self.matr[line].remove(value[0])

    def show_size_matrice(self):
        return [self.lines, self.collumns]
    
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
        print(f"\n1 - Criar {type_structure}")
        print(f"2 - Mostrar {type_structure}")
        print(f"3 - Limpar {type_structure}")
        print(f"4 - Inserir elemento na {type_structure}")
        print(f"5 - Pesquisar elemento na {type_structure}")
        print(f"6 - Remover elemento na {type_structure}")
        print(f"7 - Mostrar tamanho da {type_structure}")
        print("0 - Sair")
        option = input("\nEscolha uma das opções acima: ")
        print("")

        # Option to insert the data in the structure
        if option == "1":

            if type_structure == "matriz":
                lines = input("Quantas linhas vai ter? ")
                collumns = input("Quantas colunas vai ter? ")
                print("")
                self.matr.create_matrice(int(lines), int(collumns))

            elif type_structure == "lista":
                size = input("Qual vai ser o tamanho da lista? ")
                print("")
                self.lst.create_list_list(int(size))

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

        # Option to insert a new element in the structure
        elif option == "4":

            element = input("Elemento a ser inserido: ")

            if type_structure == "matriz":
                line = input("Em qual linha será inserido o novo elemento: ")
                collumn = input("Em qual coluna será inserido o novo elemento: ")
                print("")

                self.matr.insert_element_in_matrice(element, int(line), int(collumn))

            elif type_structure == "lista":
                position = input("Qual será a posição do novo elemento: ")
                print("")

                self.lst.insert_element_in_list(element, int(position))

        # Option to search a element in the structure
        elif option == "5":
            element = input("O elemento a ser buscado: ")
            print("")

            if type_structure == "matriz":
                self.matr.search_element_in_matrice(element)

            elif type_structure == "lista":
                self.lst.search_element_in_list(element)

        # Option to remove a element of the structure
        elif option == "6":
            element = input("O elemento a ser removido: ")

            if type_structure == "matriz":
                self.matr.delete_element_in_matrice(element)

            elif type_structure == "lista":
                self.lst.delete_element_in_list(element)

        # Option to show the size of the structure
        elif option == "7":
            
            if type_structure == "matriz":
                lines, collumns = self.matr.show_size_matrice()
                print(f"Tamanho da matriz - Linhas: {lines}, Colunas: {collumns} ")

            elif type_structure == "lista":
                size = self.lst.show_size_list()
                print(f"Tamanho da lista - {size} ")

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
