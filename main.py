from front_end import Render
from back_end import Eventhandler
import sys

def main():
    #setup
    #  Prüfung von argv
    hiden = True if "--hiden" in sys.argv else False
    is_v2 = True if "--v2" in sys.argv else False
    if "-h" in sys.argv or "--help" in sys.argv:
        print("""Usage:
    Flags:
        -h / --help:
            Dieses Menu

        --v2:
            Formatierte Textausgabe
            benötig das rich Modul

        -hiden:
              Versteckt das Passwort

                
              """)
        exit()

    #  Instanzieren der front und back_end Klassen
    render_eng = Render(is_v2,hiden)
    handler=Eventhandler(render_eng,"Escaperoom Samuel")
    #  ladet die frames aus der json datei in das backend
    handler.impjson("Frames.json")
    handler.loadframe(0)

    #Haupt schliefe
    while True:
        #  wenn ein nächster frame existiert dann wird dieser geladen
        if not handler.loadnextframe(): break
    
    #  Endet das game mit dem Endscreen
    handler.end_game()

if __name__ == '__main__':
    main()
