from os import system, name


class Usefull:

    def clear(self):
        """define our clear function"""

        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def wait(self):
        """Permet d'obtenir une pause du programme"""
        print("")
        pause = input("Appuyer sur ENTREE pour continuer ...")
        pause
        print("")
