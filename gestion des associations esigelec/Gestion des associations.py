# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:49:16 2024

@author: 43285092
"""

from mysql.connector import connect
bdd=connect(host="localhost",user="root",password="root",database="Association")
cursor=bdd.cursor()
import Associations as ASSO
assotest=ASSO.Association(0,"asctest","asctestprésid","asctestdsc","asctestlocal")
elvtest=ASSO.Elève(0,"nomtest","prénomtest",0,"M")
def Menu_principal():
    print("*1=Ajouter les informations d'un élève ou d'une association ou d'un évènement dans la base de données;")
    print("*2=Ajouter un élève ou un événement dans une association;")
    print("*3=Supprimer un élève ou une association ou un événement dans la base de données;")
    print("*4=Supprimer un élève ou un événement dans un associaiton;")
    print("*5=Afficher les informations d'un élève ou d'une association ou d'un évènement ;")
    print("*6=Modifier les informations d'un élève ou d'une association ou d'un évènement ;")
    print("*0=Quitter.")
print("*Bienvenue, Selectionnez votre option:")
Menu_principal()
choix1=int(input("Saissiser votre choix:"))
while choix1==1 or choix1==2 or choix1==3 or choix1==4 or choix1==5 or choix1==0:
    if choix1==1:
        print("""
                *=================================================*
                *1=Ajouter un élève dans la base de données;
                *2=Ajouter une association dans la base de données;
                *3=Ajouter un événement dans la base de données.
                *=================================================*
                """)
        choix2=int(input("Saissiser votre choix:"))
        if choix2==1:
            elvtest.ajouter_elv()
            Menu_principal()
            choix1=int(input("Saissiser votre choix:"))
        elif choix2==2:
            assotest.ajouter_asso()
            Menu_principal()
            choix1=int(input("Saissiser votre choix:"))
        elif choix2==3:
            assotest.ajouter_evnm()
            Menu_principal()
            choix1=int(input("Saissiser votre choix:"))
    elif choix1==2:
        print("""
                *========================*
                *1=Ajouter un élève;
                *2=Ajouter un événement.
                *========================*
                """)
        choix2=int(input("Saissiser votre choix:"))
        if choix2==1:
            elvtest.ajouter_elv_dans_asc()
            Menu_principal()
            choix1=int(input("Saissiser votre choix:"))
        elif choix2==2:
            assotest.ajouter_evnm()
            Menu_principal()
            choix1=int(input("Saissiser votre choix:"))
    elif choix1==3:
        print("""
                *============================================*
                *1=Supprimer un élève;
                *2=Supprimer une association;
                *3=Supprimer un évènement.
                *============================================*
                """)
        choix2=int(input("Saissiser votre choix:"))
        if choix2==1:
            elvtest.supprimer_elv()
            Menu_principal()
            choix1=int(input("Saissiser votre choix:"))
        elif choix2==2:
            assotest.supprimer_asso()
            Menu_principal()
            choix1=int(input("Saissiser votre choix:"))
        elif choix2==3:
            assotest.supprimer_evnm()
            Menu_principal()
            choix1=int(input("Saissiser votre choix:"))
    elif choix1==4:
        print("""
              *=========================*
              *1=Supprimer un élève;
              *2=Supprimer un événement.
              *=========================*
              """)
        choix2=int(input("Saissiser votre choix:"))
        if choix2==1:
            assotest.supprimer_elv_dans_asc()
            Menu_principal()
            choix1=int(input("Saissiser votre choix:"))
        elif choix2==2:
            assotest.supprimer_evnm_dans_asc()
            Menu_principal()
            choix1=int(input("Saissiser votre choix:"))
    elif choix1==5:
        print("""
        *=============================================================================*
        *1=afficher les informations de toutes les associations;
        *2=afficher les informations de tous les élèves;
        *3=afficher les informations de tous les événements;
        *4=afficher des associations auquel un élève appartient;
        *5=afficher des événements d'une association donnée;
        *6=afficher des élèves qui est dans une certaine année dans une association.
        *=============================================================================*
        """)
        choix2=int(input("Saissiser votre choix:"))
        if choix2==1:
           elvtest.afficher_tous_eleves()
           Menu_principal()
           choix1=int(input("Saissiser votre choix:"))
        elif choix2==2:
           assotest.afficher_tous_asso()
           Menu_principal()
           choix1=int(input("Saissiser votre choix:"))
        elif choix2==3:
           assotest.afficher_tous_evenements()
           Menu_principal()
           choix1=int(input("Saissiser votre choix:"))
        elif choix2==4:
           elvtest. afficher_elv_appartient()
           Menu_principal()
           choix1=int(input("Saissiser votre choix:"))
        elif choix2==5:
           assotest.afficher_evnm_dans_asc()
           Menu_principal()
           choix1=int(input("Saissiser votre choix:"))
        elif choix2==6:
           assotest.afficher_elv_dans_annee_dans_asc()
           Menu_principal()
           choix1=int(input("Saissiser votre choix:"))
    elif choix1==6:
        print("""
                *==============================================*
                *1=Modifier les informations d'un élève;
                *2=Modifier les informations d'une association;
                *3=Modifier les informations d'un évènement.
                *==============================================*
                """)
        choix2=int(input("Saissiser votre choix:"))
        if choix2==1:
            elvtest.modifier_elv()
            Menu_principal()
            choix1=int(input("Saissiser votre choix:"))
        elif choix2==2:
            assotest.modifier_asso()
            Menu_principal()
            choix1=int(input("Saissiser votre choix:"))
        elif choix2==3:
            assotest.modifier_evnm()
            Menu_principal()
            choix1=int(input("Saissiser votre choix:"))
    elif choix1==0:
        print("Bonne journée!")
        break
    else:
        print('Je comprend pas votre option.')
        Menu_principal()
        choix1=int(input("Saissiser votre choix:"))