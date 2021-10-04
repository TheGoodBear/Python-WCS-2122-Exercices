# coding utf-8

# Imports
import Variables as Var

# Variables


# Functions
def Main():
    """
        Do job according to subject
    """
    GetFastestAndSlowest()
    PrintAnimals()


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


# Code start
if __name__ == "__main__":
    Main()
