from front_end import Render
from back_end import Eventhandler

import sys
def main():

    #setup

    #Prüfen ob -v2 angegeben wird
    try:
        if sys.argv [1] =="-v2":
            is_v2=True

    except: is_v2=False

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
