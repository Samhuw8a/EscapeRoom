from typing import Union
from os import system
import sys
from time import sleep
import platform

class Render():
    def __init__(self,is_v2 : bool = False ,hiden : bool = False)-> None:
        self.is_v2 : bool= is_v2
        self.hiden : bool= hiden
        self.check_args()

    def check_args(self)-> None:
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
    def clean()-> None:
        #klärt das Terminal
        os_name = platform.system().lower()
        if 'windows' in os_name:
            system('cls')
        else:
            system('clear')

    # die 'schlaue' passwort Funktion
    def inp_password(self,prt:str)-> str:
        if self.hiden:
            return getpass(prt)
        else:
            return input(prt)

    # die 'schlaue' print Funktion
    @staticmethod
    def print(self,text:str,typ:str="text")-> None:
        # Wenn self.if_v2 true ist wird die console.print funktion benutzt
        # Wenn self.if_v2 false ist dann wird die inbuilt print() funktion benutzt
        if self.is_v2:
            self.console.print(text,style=typ)
        else:
            print(text)

    #Animiert den Text
    #  @staticmethod
    def animation(self,text:str ,time:float)-> None:
        #Text animation mit der stdout.wirte() methode und time.sleep()
        try:
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush ()
                sleep (time)
        except KeyboardInterrupt:
            self.end_screen()
            exit()

    #Gibt den Lade screen aus
    def load_screen(self)-> None:
        #Ein Animierter Loadscreen
        self.clean()
        sleep(0.1)
        for _ in range(2):
            self.animation("...",0.15)
            self.clean()
        sleep(0.2)

    # der End_screen des Spiel
    def end_screen(self)-> None:
        try:
            self.clean()
            self.animation("Ein Informatik projekt von Samuel Huwiler\n\t Vielen Dank für spielen.\n", 0.1)
        except KeyboardInterrupt:
            exit()
    
    #Rendert einen Frame
    def render(self,titel :str,text: str,needsinput :bool,needscode: bool)-> Union[str,int]:
        #Titel un Text
        self.clean()
        self.print (self,titel,"titel")
        self.print (self,"\n")
        self.animation(text,0.01)
        #Printet den Code oder den Input
        #Und returnt die Informationen für das Backend
        while True:
            try:
                if needsinput:         
                    return int(input(f"\n{[i+1 for i in range(needsinput)]}: "))
                elif needscode:
                    return self.inp_password("\nWas ist der Code? ")
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
