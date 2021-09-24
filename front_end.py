#Importiert die benutzten packages
from os import system
import sys
from time import sleep
import platform

class Render():
    @staticmethod
    def clean():
        #klärt das Terminal
        os_name = platform.system().lower()
        if 'windows' in os_name:
            system('cls')
        else:
            system('clear')

    @staticmethod
    def animation(text,time):
        #Animiert den Text
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush ()
            sleep (time)

    def load_screen(self):
        #Gibt den Lade screen aus
        self.clean()
        sleep(0.1)
        for _ in range(2):
            self.animation("...",0.15)
            self.clean()
        sleep(0.2)

    def end_screen(self):
        # der End_screen des Spiel
        try:
            self.clean()
            self.animation("Ein Informatik projekt von Samuel Huwiler\n\t Vielen Dank für spielen.\n", 0.1)
        except KeyboardInterrupt: exit()
    
    def render(self,titel,text,needsinput,needscode):
        #Rendert einen Frame
        self.clean()
        print (titel)
        print ("\n")
        self.animation(text,0.025)

        while True:
            try:
                if needsinput:         
                    return int(input(f"\n{[i+1 for i in range(needsinput)]}: "))
                       
                elif needscode:
                    return input("\nWas ist der Code? ")

                else:
                    input()
                    return None

            except ValueError:
                print ("Du hast einen Fehler gemacht.")

            except KeyboardInterrupt:
                self.end_screen()
                exit()

