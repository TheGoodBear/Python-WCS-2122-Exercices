# coding utf-8

# Imports
import Variables as Var

# Variables


# Functions
def Main():
    """
        Do job according to subject
    """

    print("Liste des animaux")
    print("-----------------")

    UserInput = ""
    while UserInput != "Q":
        UserInput = input("\nQue veux-tu faire ?\n(A)fficher la liste des animaux\nA(j)outter un animal\n(S)auvegarder la liste dans un fichier\n(C)harger la liste depuis un fichier\n(Q)uitter\nChoix : ").upper()
        print()

        if UserInput == "Q":
            print("Au revoir\n")

        elif UserInput == "A":
            GetFastestAndSlowest()
            PrintAnimals()
            print()

        elif UserInput == "J":
            GetNewAnimal()

        elif UserInput == "S":
            SaveToTextFile()

        elif UserInput == "C":
            LoadFromTextFile()


    # GetFastestAndSlowest()
    # PrintAnimals()


def GetFastestAndSlowest():
    """
    """
    for Animal in Var.Animals:
        if Animal["Speed"] >= Var.Fastest:
            Var.Fastest = Animal["Speed"]
        if Animal["Speed"] <= Var.Slowest:
            Var.Slowest = Animal["Speed"]  


def PrintAnimals():
    """
        Get each animal from list and print its data
    """

    for Animal in Var.Animals:
        PrefixString = "Le"
        SlowestString = ""
        FastestString = ""
        if Animal["Gender"] == "F":
            PrefixString = "La"
        if Animal["Speed"] == Var.Slowest:
            SlowestString = " et il est le plus lent"
        if Animal["Speed"] == Var.Fastest:
            FastestString = " et il est le plus rapide"
        print(f"{PrefixString} {Animal['Name']} {Animal['Color'].lower()} se déplace à {Animal['Speed']} km/h{SlowestString}{FastestString}")


def GetNewAnimal():
    """
    """
    print("Entre le nom, la couleur, la vitesse et le genre de l'animal séparés par des virgules :")
    NewAnimal = input("Nouvel animal : ")
    AnimalData = NewAnimal.split(",")
    try:
        Var.Animals.append(
            {
                "Name" : AnimalData[0],
                "Color" : AnimalData[1],
                "Speed" : int(AnimalData[2]),
                "Gender" : AnimalData[3].upper(),
            }
        )
        print("\nL'animal a été ajouté à la liste")
    except ValueError:
        print("\nLa vitesse n'est pas un nombre !")
    except IndexError:
        print("\nIl manque des informations !")
    except:
        print("\nErreur de saisie !")


def SaveToTextFile():
    """
    """

    # open new file MyFile in write mode
    with open("01-10 - Dictionnaires/Animals.txt", "w", encoding="utf-8") as MyFile:
        # for each animal il list
        for Animal in Var.Animals:
            # create temporary list of animal data
            AnimalData = []
            # for each data in animal (dictionary)
            for Value in Animal.values():
                # add animal data to temporary list
                AnimalData.append(str(Value))
            # write list strings separated with , to file
            MyFile.write(f"{','.join(AnimalData)}\n")

    print("Le fichier a été sauvegardé")


def LoadFromTextFile():
    """
    """

    # reset list
    Var.Animals = []

    # open file MyFile in read mode
    with open("01-10 - Dictionnaires/Animals.txt", "r", encoding="utf-8") as MyFile:
        # load each file line in AnimalList list
        AnimalList = MyFile.readlines()
        # for each Animal in list
        for Animal in AnimalList:
            # split animal data with , as separator
            AnimalData = Animal.split(",")
            # add new animal as dictionary to Animals list
            Var.Animals.append(
                {
                    "Name" : AnimalData[0],
                    "Color" : AnimalData[1],
                    "Speed" : int(AnimalData[2]),
                    "Gender" : AnimalData[3],
                }
            )

    print("Le fichier a été chargé")


# Code start
if __name__ == "__main__":
    Main()
