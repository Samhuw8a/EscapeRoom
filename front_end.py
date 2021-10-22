#Importiert die benutzten packages
from os import system
import sys
from time import sleep
import platform

class Render():
    def __init__(self,is_v2 : bool = False ,hiden : bool = False):
        self.is_v2 : bool= is_v2
        self.hiden : bool= hiden
        self.check_args()

    def check_args(self):
        if self.hiden:
            global getpass
            from getpass import getpass
            #  self.getpass = getpass
        if self.is_v2:
            #Import von rich
            try:
                from rich.console import Console
                from rich.theme import Theme
                self.cust_theme=Theme({
                            "text":"italic",
                            "titel": "bold underline green",
                            "Error" : "bold red"
                        })
                self.console= Console(theme=self.cust_theme)

            except ModuleNotFoundError:
                #Hilfe wenn rich nicht importiert ist
                print("""
                        ERROR: um --v2 benötigt das `rich` Modul 
                        gibt:
                            pip3 install rich
                        um das pip modul zu instalieren und versuche es nochmal
                        """,file=sys.stderr)
                exit(1)

    @staticmethod
    def clean():
        #klärt das Terminal
        os_name = platform.system().lower()
        if 'windows' in os_name:
            system('cls')
        else:
            system('clear')

    # die 'schlaue' passwort Funktion
    def inppass(self,prt:str):
        if self.hiden:
            return getpass(prt)
        else:
            return input(prt)

    # die 'schlaue' print Funktion
    @staticmethod
    def print(self,text,typ="text"):
        # Wenn self.if_v2 true ist wird die console.print funktion benutzt
        # Wenn self.if_v3 false ist dann wird die inbuilt print() funktion benutzt
        if self.is_v2:
            self.console.print(text,style=typ)
        else:
            print(text)

    #Animiert den Text
    @staticmethod
    def animation(text,time : int):
        #Text animation mit der stdout.wirte() methode und time.sleep()
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush ()
            sleep (time)

    #Gibt den Lade screen aus
    def load_screen(self):
        #Ein Animierter Loadscreen
        self.clean()
        sleep(0.1)
        for _ in range(2):
            self.animation("...",0.15)
            self.clean()
        sleep(0.2)

    # der End_screen des Spiel
    def end_screen(self):
        try:
            self.clean()
            self.animation("Ein Informatik projekt von Samuel Huwiler\n\t Vielen Dank für spielen.\n", 0.1)
        except KeyboardInterrupt:
            exit()
    
    #Rendert einen Frame
    def render(self,titel :str,text: str,needsinput :bool,needscode: bool)-> str:
        
        #Titel un Text
        self.clean()
        self.print (self,titel,"titel")
        self.print (self,"\n")
        self.animation(text,0.025)

        #Printet den Code oder den Input
        #Und returnt die Informationen für das Backend
        while True:
            try:
                if needsinput:         
                    return int(input(f"\n{[i+1 for i in range(needsinput)]}: "))
                       
                elif needscode:
                    return self.inppass("\nWas ist der Code? ")

                else:
                    return input()

            #Excepion handling
            except ValueError:
                self.print (self,"Bitte gib deine Antwort um richtigen Format an.","Error")
            except KeyboardInterrupt:
                self.end_screen()
                exit()

if __name__== '__main__':
    from getpass import getpass
    getpass("Test")
    test= Render(True)
