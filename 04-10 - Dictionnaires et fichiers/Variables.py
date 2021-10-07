# coding: utf-8

Players = []
FilePath = "04-10 - Dictionnaires et fichiers/Sauvegarde.txt"
StopApplication = False

MenuEntries = [
    {
        "Description" : "(A)jouter un joueur",
        "Commande" : "A"
    },
    {
        "Description" : "(S)upprimer un joueur",
        "Commande" : "S"
    },
    {
        "Description" : "Modifier le score d'un (j)oueur",
        "Commande" : "J"
    },
    {
        "Description" : "Afficher la (l)iste des joueurs",
        "Commande" : "L"
    },
    {
        "Description" : "(C)harger la liste des joueurs depuis le fichier",
        "Commande" : "C"
    },
    {
        "Description" : "Sauve(g)arder la liste des joueurs dans un fichier",
        "Commande" : "G"
    },
    {
        "Description" : "(Q)uitter l'application",
        "Commande" : "Q"
    }
]

PlayerData = [
    {
        "Name" : "LastName",
        "Description" : "Nom",
        "Type" : "str"
    },
    {
        "Name" : "FirstName",
        "Description" : "Prénom",
        "Type" : "str"
    },
    {
        "Name" : "Age",
        "Description" : "Age",
        "Type" : "int"
    },
    {
        "Name" : "Sex",
        "Description" : "Sexe",
        "Type" : [
            ("F", "(F)éminin"),
            ("M", "(M)asculin"),
            ("I", "(I)ndéfini"),
            ("A", "(A)utre")
        ]
    },
    {
        "Name" : "Score",
        "Description" : "Score",
        "Type" : "int"
    }
]