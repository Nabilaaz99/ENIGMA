import unidecode, string,json

#couche applicat°

def main():
    """fonction qui crée les fichiers : message et fichier"""
    global message,fichier
    message = open(r"C:\Users\NABILA\Desktop\message.txt","r")
    message.close()
    message = open(r"C:\Users\NABILA\Desktop\message.txt","r")
    fichier =  open(r"C:\Users\NABILA\Desktop\fichier.txt","w")


def Menu():
    """menu avec choix de quattres options"""
    global que_voulez_vous_faire,liste_option
    que_voulez_vous_faire = input("Que voulez-vous faire? :\n"
                                  "Entrée\t\t\t\t   :"
                                  "\n\t\t\t\t\t\t1- Lire Message \n"
                                  "\t\t\t\t\t\t2- Écrire Message \n"
                                  "\t\t\t\t\t\t3- Sauvegarder Message\n"
                                  "\t\t\t\t\t\t4- Quitter \n\t\t\t\t\t\t"
                                  ":")
    liste_option = ["1" ,"2","3","4"]

def rappeller_menu():
    """pour ne pas rappeller la
    fonction menu dans les fonctions du menu"""
    Menu()
    while que_voulez_vous_faire == liste_option[0]:
            LectureMessage(fichier, message)
            Menu()
    while que_voulez_vous_faire == liste_option[1]:
            EcritureMessage()
            Menu()
    while que_voulez_vous_faire == liste_option[2]:
            SauvegarderMessage()
            Menu()
    if que_voulez_vous_faire == liste_option[3]:
        Quitter()

#couche logique

def LectureMessage(fichier,message):
    """Lit le fichier : message et écrit correctement le message dans le fichier : fichier"""


    for ligne in message:
        liste_ponctuation = [",", ";", "!", "?", ".", "'", "(", ")", "\"", "@", "|", "&", "%", "£", "µ", "/", "\\", "=",
                             "-", "*", "§", "^", ":", "[", "]"]
        for i in range(len(liste_ponctuation)):
            ligne = ligne.replace(liste_ponctuation[i],"")
        ligne = ligne.split()
        ligne = "".join(ligne)

        ligne = ligne.strip()
        ligne = unidecode.unidecode(ligne)

        fichier.write(ligne.upper())
    fichier.close()
    message.close()
   # codage()


def EcritureMessage():
    """Écrit un message (chaîne de caractères) et retire les ponctuation ainsi que
    les slash etc
    Met le message en majuscules """


    global msg
    msg = input("Entrez votre message : ")

    for i in range(len(msg)):
        liste_ponctuation = [",", ";", "!", "?", ".", "'", "(", ")","\"","@",
                             "|","&","%","£","µ","/","\\","=","-","*","§","^",":","[","]"]
        for j in range(len(liste_ponctuation)):
            msg = msg.replace(liste_ponctuation[j],"")


    msg = unidecode.unidecode(msg)
    msg = msg.upper()
    msg = msg.strip()
    msg = msg.split()
    msg = "".join(msg)
   # codage()
def Quitter():
    """Quitte le menu """


    print("Au revoir")

#couche data
def SauvegarderMessage():
    """Sauvegarde le message écrit dans la f() EcritureMessage() dans un fichier nouveau_fichier.txt"""


    nouveau_fichier = open(r"C:\Users\NABILA\Desktop\nouveau_fichier.txt", "w")
    liste_ponctuation = [",", ";", "!", "?", ".", "'", "(", ")"]
    for i in range(len(msg)):
        for j in range(len(liste_ponctuation)):
            if liste_ponctuation[j] in msg:
                msg.replace(msg[i], "")
    nouveau_fichier.write(msg)
    nouveau_fichier.close()

#fin couche data

def listAlphabet():
    """Crée deux listes (tableau_entree et tableau_sortie)"""
    return list(string.ascii_uppercase)
tableau_entree=(listAlphabet())
tableau_sortie =(listAlphabet())

def rotors():
    global rotor1liste ,rotor2liste , rotor3liste
    """Utilise les rotors et le(s) réflecteur(s) du fichier rotors.json"""
    with open('rotors.json',"r") as r:

        r = json.load(r)
        rotors = (r["rotors"])

        rotor1dict = dict(rotors[0])
        rotor1liste =rotor1dict["RA"]
        rotor2dict = dict(rotors[2])
        rotor2liste = rotor2dict["RC"]
        rotor3dict = dict(rotors[4])
        rotor3liste = rotor3dict["RE"]
        print("\n",rotor1liste,"\n",rotor3liste,"\n",rotor2liste)

def reflecteurs():
    with open('rotors.json',"r") as r:

        r = json.load(r)
        reflecteurs = (r["reflecteurs"])

        reflec1 = reflecteurs[0]

        reflec1 = (reflec1["RFA"])
        print("\n", reflec1)

        reflec2 = reflecteurs[1]

        reflec2 = (reflec2["RFB"])
        print("\n",reflec2)

#def codage():
#    """Pour coder un message"""



    reflecteurs()
#def decodage():
#    pass



if __name__=='__main__':
    main()

rappeller_menu()
#codage()