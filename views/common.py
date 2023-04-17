from os import name, system


class Usefull:
    def clear(self):
        """define our clear function"""

        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def wait(self):
        """Permet d'obtenir une pause du programme"""
        print("")
        input("Appuyez sur ENTREE pour continuer ...")
        print("")
