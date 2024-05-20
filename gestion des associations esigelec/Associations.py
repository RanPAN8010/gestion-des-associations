# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:42:33 2024

@author: 43285092
"""

from mysql.connector import connect
bdd=connect(host="localhost",user="root",password="root",database="association")
cursor=bdd.cursor()

class Elève:
    def __init__(self,a,b,c,d,e):
        self.id=a
        self.nom=b
        self.prenom=c
        self.dans_quelle_annee=d
        self.sexe=e
    def ajouter_elv(self):
        nom=str(input("Déterminez le nom de l'élève:"))
        prenom=str(input("Déterminez le prénom de l'élève:"))
        dans_quelle_annee=int(input("Veuillez choisir cet élève est dans quelle année.1=prépa 1, 2=prépa 2, 3=ingénieur 1, 4=ingénieur 2, 5=ingénieur 3:"))
        sexe=str(input("Déterminer son sexe F ou M:"))
        sql="INSERT INTO Eleve(elv_nom,elv_prenom,elv_dans_quelle_annee,elv_sexe) VALUES ('%s','%s',%d,'%s')"% (nom,prenom,dans_quelle_annee,sexe)
        cursor.execute(sql)
        cursor.execute("Select elv_id from Eleve Where elv_nom='%s' AND elv_prenom='%s'"% (nom,prenom))
        row1=cursor.fetchone()
        print("L'id de ",nom,prenom,"est",row1[0])
        bdd.commit()
        print("Achèvement d'ajout.")
    def ajouter_elv_dans_asc(self):
        name=str(input("Entrer l'association:"))
        cursor.execute("Select asc_id from Association Where asc_nom='%s'"% (name))
        row1=cursor.fetchall()
        nom_elv=str(input("Entrer le nom d'étudiant:"))
        prenom_elv=str(input("Entrer le prénom d'étudiant:"))
        cursor.execute("Select elv_id from Eleve Where elv_nom='%s' AND elv_prenom='%s'"% (nom_elv,prenom_elv))
        row2=cursor.fetchall()
        if row2==[] or row1==[]:
            if row1==[]:
                print("L'association n'existe pas, veuillez créer l'association par ajouter des informations de l'association dans la base de données.")
            else:
                print("L'élève n'existe pas, veuillez ajouter des informations de l'élève dans la base de données.")
        else:
            cursor.execute("INSERT INTO Participer_a VALUES (%d,%d)"% (int(row2[0][0]),int(row1[0][0])))
            bdd.commit()
            print("Achèvement d'ajout.")
    def modifier_elv(self):
        nom=str(input("Nom de l'élève pour modifier:"))
        prenom=str(input("Prénom de l'élève pour modifier:"))
        cursor.execute("Select elv_id from Eleve Where elv_nom='%s' AND elv_prenom='%s'"% (nom,prenom))
        row1=cursor.fetchall()
        if row1==[]:
            print("L'élève n'existe pas, veuillez ajouter des informations de l'élève dans la base de données.")
        else:
            choix=int(input("Taper le numéro pour renouveler:1=Nom et prénom,2=dans quelle annee,3=sexe:"))
            if choix==1:
                nom2=str(input("Entrer le nouveau nom de l'élève:"))
                prenom2=str(input("Entrer le nouveau prénom de l'élève:"))
                cursor.execute("UPDATE Eleve Set elv_nom =' %s' , elv_prenom = '%s' WHERE elv_id=%d"% (nom2,prenom2,row1[0][0]))
                bdd.commit()
                print("Achèvement des modifications.")
            elif choix==2:
                annee=int(input("Entrer la nouvelle information:1=prépa 1, 2=prépa 2, 3=ingénieur 1, 4=ingénieur 2, 5=ingénieur 3:"))
                cursor.execute("UPDATE Eleve Set elv_dans_quelle_annee=%d WHERE elv_nom='%s' AND elv_prenom='%s'"% (annee,nom,prenom))
                bdd.commit()
                print("Achèvement des modifications.")
            elif choix==3:
                sexe=str(input("Renouveler son sexe F ou M:"))
                cursor.execute("UPDATE Eleve Set elv_sexe='%s' WHERE elv_nom='%s' AND elv_prenom='%s'"% (sexe,nom,prenom))
                bdd.commit()
                print("Achèvement des modifications.")
            else:
                print("Erreur! Veuillez rechoisir.")
    def supprimer_elv(self):
        nom=str(input("Entrer le nom de l'éleve pour supprimer:"))
        prenom=str(input("Entrer le prenom de l'eleve pour supprimer:"))
        cursor.execute("DELETE from Eleve Where elv_nom = '%s' AND elv_prenom = '%s'"% (nom,prenom))
        bdd.commit()
        print("Achèvement des suppression.")
    def afficher_tous_eleves(self):
        cursor.execute("SELECT * FROM Eleve")
        eleves=cursor.fetchall()
        for eleve in eleves:
            print("*============================================*")
            print("ID:", eleve[0])
            print("Nom:", eleve[1])
            print("Prénom:", eleve[2])
            print("Année:", eleve[3])
            print("Sexe:", eleve[4])
            print("*============================================*")
            print("\n")
    def afficher_elv_appartient(self):
        nom_elv=str(input("Entrer le nom d'étudiant:"))
        prenom_elv=str(input("Entrer le prénom d'étudiant:"))
        cursor.execute("SELECT elv_id from Eleve Where elv_nom='%s' AND elv_prenom='%s'"% (nom_elv,prenom_elv))
        row1=cursor.fetchone()
        if row1==[]:
            print("L'élève n'existe pas, veuillez ajouter des informations de l'élève dans la base de données.")
        else:
            cursor.execute("Select prt_association from Participer_a Where prt_eleve='%d'"% (row1))
            row2=cursor.fetchall() 
            if row2==[]:
                print("Cet élève n'appartient à aucune association.")
            else:
                for i in row2:
                    print("Les associations auxquelles l'élève appartient:")
                    print("*============================================*")
                    cursor.execute("Select asc_nom from Association Where asc_id='%d'"% (i))
                    row3=cursor.fetchall()
                    for b in row3:
                        print(b)
                    print("*============================================*")

class Association:
    def __init__(self,a,b,c,d,e):
        self.id=a
        self.nom=b
        self.présid=c
        self.dsc=d
        self.asc_local=e
    def ajouter_asso(self):
        nom=str(input("Déterminez le nom de l'association:"))
        présid=str(input("Déterminez le Prénom NOM de son président:"))
        local=str(input("Déterminez son local:"))
        description=str(input("Ecrivez sa description:"))
        sql="INSERT INTO Association(asc_nom, asc_nom_president, asc_dsc, asc_local) VALUES ('%s','%s','%s','%s')" % (nom,présid,local,description)
        cursor.execute(sql)
        cursor.execute("Select asc_id from Association Where asc_nom='%s'"% (nom))
        row1=cursor.fetchone()
        print("L'id de ",nom,"est",row1[0])
        bdd.commit()
        print("Achèvement d'ajout.")
    def supprimer_asso(self):
        nom=str(input("Entrer le nom de l'association pour supprimer:"))
        cursor.execute("DELETE from Association Where asc_nom=('%s')"% (nom))
        bdd.commit()
        print("Achèvement des suppression.")
    def ajouter_evnm(self):
        name=str(input("Entrer le nom de l'association:"))
        cursor.execute("Select asc_id from Association Where asc_nom = '%s'"% (name))
        row1=cursor.fetchone()
        if row1==[]:
            print("L'association n'existe pas.")
        else:
            nom=str(input("Déterminez le nom de l'évènement:"))
            date=str(input("Déterminez la date:"))
            description=str(input("Ecrivez sa description:"))
            lieu=str(input("Déterminez son lieu:"))
            sql="INSERT INTO Evenement(evm_nom, evm_date, evm_dsc, evm_lieu) VALUES ('%s','%s','%s','%s')"% (nom,date,description,lieu)
            cursor.execute(sql)
            bdd.commit()
            cursor.execute("SELECT evm_id from Evenement Where evm_nom='%s'"% (nom))
            row2=cursor.fetchone()
            print("L'id de ",nom,"est",row2[0])
            cursor.execute("INSERT INTO Organiser VALUES (%d,%d)"% (row2[0],row1[0]))
            bdd.commit()
            print("Achèvement d'ajout.")
    def supprimer_evnm(self):
        nom=str(input("Entrer le nom d'évenement pour supprimer:"))
        cursor.execute("Select evm_id from Evenement Where evm_nom=('%s')"% (nom))
        row1=cursor.fetchone()
        if row1!=[]:  
            cursor.execute("DELETE from Organiser Where org_evenement=%d"% (row1[0]))
        cursor.execute("DELETE from Evenement Where evm_nom='%s'"% (nom))
        bdd.commit()
        print("Achèvement des suppression.")
    def modifier_evnm(self):
        nom=str(input("Nom de l'événement pour modifier:"))
        cursor.execute("Select evm_id from Evenement Where evm_nom='%s'"% (nom))
        row1=cursor.fetchall()
        if row1==[]:
            print("L'élève n'existe pas, veuillez ajouter des informations de l'événement dans la base de données.")
        else:
            choix=int(input("Taper le numéro pour renouveler:1=Nom,2=date,3=déscription,4=lieu:"))
            if choix==1:
                nom2=str(input("Entrer le nouveau nom de l'événement:"))
                cursor.execute("UPDATE Evenement Set evm_nom='%s' Where evm_nom='%s'"% (nom2,nom))
                bdd.commit()
                print("Achèvement des modifications.")
            elif choix==2:
                date=str(input("Entrer la nouvelle date:"))
                cursor.execute("UPDATE Evenement Set evm_date=('%s') Where evm_nom=('%s')"% (date,nom))
                bdd.commit()
                print("Achèvement des modifications.")
            elif choix==3:
                description=str(input("Entrer la nouvelle déscription:"))
                cursor.execute("UPDATE Evenement Set evm_dsc=('%s') Where evm_nom=('%s')"% (description,nom))
                bdd.commit()
                print("Achèvement des modifications.")
            elif choix==4:
                lieu=str(input("Entrer le nouveau lieu:"))
                cursor.execute("UPDATE Evenement Set evm_lieu=('%s') Where evm_nom=('%s')"% (lieu,nom))
                bdd.commit()
                print("Achèvement des modifications.")
            else:
                print("Erreur! Veuillez rechoisir.")
    def supprimer_elv_dans_asc(self):
        name=str(input("Entrer l'association:"))
        cursor.execute("Select asc_id from Association Where asc_nom='%s'"% (name))
        row1=cursor.fetchone()
        if row1==[]:
            print("L'association n'existe pas.")
        else:
            nom_elv=str(input("Entrer le nom d'étudiant':"))
            prenom_elv=str(input("Entrer le prénom d'étudiant:"))
            cursor.execute("Select elv_id from Eleve Where elv_nom='%s' AND elv_prenom='%s'"% (nom_elv,prenom_elv))
            row2=cursor.fetchone()
            if row2==[]:
                print("L'élève n'existe pas.")
            else:
                cursor.execute("DELETE from Participer_a Where prt_association = %d AND prt_eleve = %d"% (row1[0],row2[0]))
                bdd.commit()
                print("Achèvement des suppression.")
    def modifier_asso(self):
        nom=str(input("Nom de l'association pour modifier:"))
        cursor.execute("Select asc_id from Association Where asc_nom='%s'"% (nom))
        row1=cursor.fetchone()
        if row1==[]:
            print("L'association n'existe pas, veuillez créer l'association par ajouter des informations de l'association dans la base de données.")
        else:
            choix=int(input("Taper le numéro pour renouveler:1=Nom,2=président,3=local,4=description:"))
            if choix==1:
                nom2=str(input("Entrer le nouveau nom de l'association:"))
                cursor.execute("UPDATE Association Set asc_nom='%s' Where asc_nom='%s'"% (nom2,nom))
                bdd.commit()
                print("Achèvement des modifications.")
            elif choix==2:
                president=str(input("Entrer le nom de nouveau président:"))
                cursor.execute("UPDATE Association Set asc_nom_president='%s' Where asc_nom_nom='%s'"% (president,nom))
                bdd.commit()
                print("Achèvement des modifications.")
            elif choix==3:
                local=str(input("Entrer le nouveau local:"))
                cursor.execute("UPDATE Association Set asc_local='%s' Where asc_nom='%s'"% (local,nom))
                bdd.commit()
                print("Achèvement des modifications.")
            elif choix==4:
                description=str(input("Entrer la nouvelle description:"))
                cursor.execute("UPDATE Association Set asc_dsc='%s' Where asc_nom='%s'"% (description,nom))
                bdd.commit()
                print("Achèvement des modifications.")
            else:
                print("Erreur! Veuillez rechoisir.")
    def afficher_tous_asso(self):
        cursor.execute("SELECT * FROM Association")
        associations=cursor.fetchall()
        for association in associations:
            print("*============================================*")
            print("ID de l'association:", association[0])
            print("Nom de l'association:", association[1])
            print("Président de l'association:", association[2])
            print("Description de l'association:", association[3])
            if association[4]!=None:
                print("Local de l'association:", association[4])
                print("*============================================*")
            else:
                print("Il n'y a pas de local")
                print("*============================================*")
            print("\n")
    def afficher_tous_evenements(self):
        cursor.execute("SELECT * FROM Evenement")
        evenements=cursor.fetchall()
        for evenement in evenements:
            print("*============================================*")
            print("ID:", evenement[0])
            print("Nom:", evenement[1])
            print("Date:", evenement[2])
            print("Description:", evenement[3])
            print("Lieu:", evenement[4])
            print("*============================================*")
            print("\n")
    def afficher_asc_membre(self):
        name=str(input("Entrer le nom de l'association:"))
        cursor.execute("Select asc_id from Association Where asc_nom='%s'"% (name))
        row1=cursor.fetchall()
        for i in row1:
            cursor.execute("Select prt_eleve from Participer_a Where prt_association='%d'"% (i))
            row2=cursor.fetchall() 
            if row2!=None:
                print("Les membre de ",name,"sont:")
                for a in row2:
                    cursor.execute("Select * from Eleve Where elv_id='%d'"% (a))
                    row3=cursor.fetchall()
                    for b in row3:
                        print("*============================================*")
                        print("ID:", b[0])
                        print("Nom:", b[1])
                        print("Prénom:", b[2])
                        print("Année:", b[3])
                        print("Sexe:", b[4])
                        print("*============================================*")
                        print("\n")
            else:
                print("Cette association n'a aucun membre.")
    def afficher_evnm_dans_asc(self):
        name=str(input("Entrer le nom de l'association:"))
        cursor.execute("Select asc_id from Association Where asc_nom='%s'"% (name))
        row1=cursor.fetchall()
        for i in row1:
            cursor.execute("Select org_evenement from Organiser Where org_association='%d'"% (i))
            row2=cursor.fetchall()
            if row2!=None:
                print("L'association",name, "propose les événements suivants:")
                for a in row2:
                    cursor.execute("SELECT * FROM Evenement WHERE evm_id='%d'"% (a))
                    row3=cursor.fetchall()
                    for b in row3:
                        print("*============================================*")
                        print("ID:", b[0])
                        print("Nom:", b[1])
                        print("Date:", b[2])
                        print("Description:", b[3])
                        print("Lieu:", b[4])
                        print("*============================================*")
                        print("\n")
            else:
                print("Cette association n'organise aucun événement.")
    def afficher_elv_dans_annee_dans_asc(self):
        name=str(input("Entrer le nom de l'association:"))
        cursor.execute("Select asc_id from Association Where asc_nom='%s'"% (name))
        row1=cursor.fetchall()
        cursor.execute("Select prt_eleve from Participer_a Where prt_association='%d'"% (row1))
        row2=cursor.fetchall() 
        if row2!=None:
            annee=str(input("Entrer l'année de parcours dont vous voulez enquérir.1=prépa 1, 2=prépa 2, 3=ingénieur 1, 4=ingénieur 2, 5=ingénieur 3:"))
            if annee not in [1,2,3,4,5]:
                print("Erreur.")
                annee=str(input("1=prépa 1, 2=prépa 2, 3=ingénieur 1, 4=ingénieur 2, 5=ingénieur 3:"))
            else:
                for i in row2:
                    cursor.execute("Select * from Eleve Where elv_id='%d' AND  elv_dans_quelle_annee='%d'"% (i,annee))
                    row3=cursor.fetchall()
                    if row3!=None:
                        print("les membre de",name,"qui sont dans cette année:")
                        for a in row3:    
                            print("*============================================*")
                            print("ID:", a[0])
                            print("Nom:", a[1])
                            print("Prénom:", a[2])
                            print("Sexe:", a[4])
                            print("*============================================*")
                            print("\n")
                    else:
                        print("Aucun élève de cette année dans cette association.")
        else:
            print("Cette association n'a aucun membre.")
