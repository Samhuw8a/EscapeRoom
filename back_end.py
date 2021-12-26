import json
from typing import Optional

class Eventhandler():
    def __init__ (self,render_eng,titel,framesraw = None)-> None:
        self.framesraw = framesraw
        self.nextframe: Optional[int] = None
        self.render_eng = render_eng
        self.titel=titel
    
    def impjson(self,path : str):
        """ladet die Frames aus der json Datei"""
        with open(path) as jsondata:
            self.framesraw = json.load(jsondata)
    
    def loadframe(self,index : int):
        """Ladet die Inf. des Frame und entscheidet was der mächste Frame ist."""
        frame= self.framesraw[str(index)]

        #Liest alle Var aus die immer existieren
        text : str= frame["text"]
        needsinput : bool = frame["input"]
        needscode : bool = frame["code"]
        next_f : Optional[int] = frame["next"]

        #speichert den render output
        render_output= self.render_eng.render(self.titel,text,needsinput,needscode)

        #Evaluieren des Output
        if needsinput: 
            ifs=frame["ifs"] #liest ifs ein
            for i,j in enumerate(ifs): #geht durch alle ifs und entscheidet was self.nextframe ist
                if render_output ==i+1:
                    self.nextframe = ifs[j] 

        elif needscode: 
            #Testet ob der Code richtig ist
            iscode:str = frame["is_code"] # liest iscode ein
            if iscode  =="*": 
                # Wenn is_code '*' ist dann wird jerder code weitergeleitet
                self.nextframe=next_f
            else:
                #Wenn der Code stimmt wird der user weitergeleitet. 
                #Wenn der Code nicht richtig ist dann wird der user zum gleichen Frame weitergeleitet
                self.nextframe = next_f if render_output == iscode else index
               
        else:  
            #testet ob es das ende ist. (siehe loadnextframe())
            self.nextframe=next_f if next_f else None

    def loadnextframe(self) -> bool:
        """Ladet den nächsten Frame"""
        if self.nextframe:
            self.render_eng.load_screen()
            self.loadframe(self.nextframe)

        #return für den main loop
            return True
        return False

    def end_game(self):
        """endet das Game"""
        self.render_eng.end_screen()

