# coding: utf-8

# imports
import Variables as Var

# variables


# functions
def Main():
    """
    """
    print("\nGestion des joueurs")
    print("-------------------")
    
    while not Var.StopApplication:
        ShowMenu()

    # user quits
    print("\nAu revoir\n")


def ShowMenu():
    """
    """

    print("\nMENU\n")
    # print all menu descriptions
    for Menu in Var.MenuEntries:
        print(f"{Menu['Description']}")
    # get all possibele menu actions
    Actions = [Menu["Commande"] for Menu in Var.MenuEntries]
    
    Action = ""
    while Action not in Actions:
        Action = input("\nChoisissez une action : ").upper()
        if Action not in Actions:
            print("Ceci n'est pas une commande disponible.")
    
    # execute action
    if Action == "A":
        CreatePlayer()
    elif Action == "S":
        DeletePlayer()
    elif Action == "J":
        EditPlayerScore()
    elif Action == "L":
        ShowPlayerList()
    elif Action == "C":
        LoadPlayersFromFile()
    elif Action == "G":
        SavePlayersToFile()
    elif Action == "Q":
        Var.StopApplication = True


def CreatePlayer():
    """
    """

    # create a new empty player
    Player = {}
    print("\nEntrer les informations du joueur :")

    # ask each data for new player
    for Data in Var.PlayerData:

        # this initialize possible choices if data is a specific list of choices
        ChoicesString = ""
        Choices = None
        if type(Data["Type"]) is list:
            # get choices description
            ChoicesString = [DataType[1] for DataType in Data["Type"]]
            # get possible entered choices 
            Choices = [DataType[0] for DataType in Data["Type"]]

        # ask for data until it is valid (matches its Type)
        IsDataValid = False
        while not IsDataValid:
            # ask for data value     
            DataValue = input(f"{Data['Description']} {','.join(ChoicesString)} : ")
            
            # check for data validity
            if Data['Type'] == "int":
                # integer
                if DataValue.isdigit():
                    DataValue = int(DataValue)
                    IsDataValid = True
                else:
                    print("Vous devez entrer un nombre")
            elif Choices is not None:
                # choice
                if DataValue.upper() in Choices:
                    IsDataValid = True
                else: 
                    print("Ce choix n'est pas disponible")
            else:
                # string
                IsDataValid = True

        # data is valid
        # add it to NewPlayer dictionary with appropriate key
        Player[Data["Name"]] = DataValue

    # all data are entered
    # add new player to player list    
    Var.Players.append(Player)
    print(f"\nLe joueur {Player['LastName']} {Player['FirstName']} a été ajouté à la liste")


def DeletePlayer():
    """
    """

    ShowPlayerList()

    # ask for player index to remove until index is valid
    IsDataValid = False
    while not IsDataValid:
        PlayerNumber = input("Quel joueur voulez-vous supprimer ? ")
        if (PlayerNumber.isdigit() 
            and int(PlayerNumber) > 0 
            and int(PlayerNumber) <= len(Var.Players)):
            IsDataValid = True
    
    # data is valid
    DeletedPlayer = Var.Players.pop(int(PlayerNumber) - 1)
    print(f"\n{DeletedPlayer['LastName']} {DeletedPlayer['FirstName']} a été supprimé")


def EditPlayerScore():
    """
    """

    ShowPlayerList()

    # ask for player index to remove until index is valid
    IsDataValid = False
    while not IsDataValid:
        PlayerNumber = input("De quel joueur voulez-vous modifier le score ? ")
        if (PlayerNumber.isdigit() 
            and int(PlayerNumber) > 0 
            and int(PlayerNumber) <= len(Var.Players)):
            IsDataValid = True
    
    # data is valid
    Player = Var.Players[int(PlayerNumber) - 1]

    # ask for data until it is valid
    IsDataValid = False
    while not IsDataValid:
        # ask for data value     
        DataValue = input(f"Entrez la variation du score pour {Player['LastName']} {Player['FirstName']} : ")
        
        # check for data validity
        if DataValue.isdigit():
            IsDataValid = True
        else:
            print("Vous devez entrer un nombre")

    # data is valid
    # update player score
    Player["Score"] += int(DataValue)
    print(f"\n{Player['LastName']} {Player['FirstName']} a mainteant un score de {Player['Score']}")


def ShowPlayerList():
    """
    """

    print("\nListe des joueurs\n")

    # check if list is empty, if yes exit function
    if len(Var.Players) == 0:
        print("Il n'y a aucun joueur dans la liste")
        return

    # show each player with index number
    for Index, Player in enumerate(Var.Players):
        print(f"{Index + 1} - {Player['LastName']} {Player['FirstName']} a un score de {Player['Score']} points")


def LoadPlayersFromFile():
    """
    """

    # try:
    # open file in read mode
    with open(Var.FilePath, "r", encoding="utf-8") as MyFile:
        # read all players line by line
        Players = MyFile.readlines()
        
    # for each player in file
    for Player in Players:
        # split player data to list
        PlayerData = Player.replace("\n", "").split(",")
        # create empty new player
        NewPlayer = {}
        # for each player data
        for Index, Data in enumerate(Var.PlayerData):
            # add player data to NewPlayer dictionary
            if Data['Type'] == "int":
                # data is integer
                PlayerData[Index] = int(PlayerData[Index])
            NewPlayer[Data['Name']] = PlayerData[Index]

        # add player to list
        Var.Players.append(NewPlayer)

    # load successfull
    print(f"\n{len(Var.Players)} joueurs ont été chargés dans la liste")
     
    # except:
    #     # error while loading
    #     print("\nLes joueurs n'ont pas pu être chargés")


def SavePlayersToFile():
    """
    """

    try:
        # open file in write mode
        with open(Var.FilePath, "w", encoding="utf-8") as MyFile:
            # for each player in list
            for Player in Var.Players:
                PlayerData = ""
                # for each player data
                for Data in Var.PlayerData:
                    # add player data to PlayerData string (separated by ,)
                    Separator = "" if PlayerData == "" else ","
                    PlayerData = f"{PlayerData}{Separator}{Player[Data['Name']]}"
                # write PlayerData string to file
                MyFile.write(f"{PlayerData}\n")

        # save successfull
        print(f"\nLes {len(Var.Players)} joueurs ont été sauvegardés")
     
    except:
        # error while saving
        print("\nLes joueurs n'ont pas pu être sauvegardés")
    


# code starts here
if __name__ == "__main__":
    
    Main()
