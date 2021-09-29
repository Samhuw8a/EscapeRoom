from front_end import Render
from back_end import Eventhandler

def main():

    #setup
    render_eng = Render()
    handler=Eventhandler(render_eng,"Escaperoom Samuel")
    
    #ladet die frames aus der json datei in das backend
    handler.impjson("Frames.json")
    handler.loadframe(0)

    #Haupt schliefe
    while True:
        #wenn ein nächster frame existiert dann wird dieser geladen
        if not handler.loadnextframe(): break
    
    #Endet das game mit dem Endscreen
    handler.end_game()

if __name__ == '__main__':
    main()
