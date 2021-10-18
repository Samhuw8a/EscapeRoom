from front_end import Render
from back_end import Eventhandler
import sys

def main():

    #setup

    #Prüfen ob --v2 angegeben wird
    if "--v2" in sys.argv:
        is_v2=True

    else: is_v2=False

    #Instanzieren der front und back_end Klassen
    render_eng = Render(is_v2)
    handler=Eventhandler(render_eng,"Escaperoom Samuel")
    
    #ladet die frames aus der json datei in das backend
    handler.impjson("Test.json")
    handler.loadframe(0)

    #Haupt schliefe
    while True:
        #wenn ein nächster frame existiert dann wird dieser geladen
        if not handler.loadnextframe(): break
    
    #Endet das game mit dem Endscreen
    handler.end_game()

if __name__ == '__main__':
    main()
