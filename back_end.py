import json

class Eventhandler():

    def __init__(self, render_eng,titel,framesraw=None):
        #setzt die "globalen" Variablen
        self.framesraw = framesraw
        self.nextframe = None
        self.render_eng = render_eng
        self.titel=titel
    
    def impjson(self,path):
        #Ladet Die Frames aus einer Json Datei.
        with open(path) as jsondata:
            self.framesraw = json.load(jsondata)
    
    def loadframe(self,index):
        #Ladet die Inf. des Frame und entscheidet was der mächste Frame ist.
        frame= self.framesraw[str(index)]

        #Liest alle Var aus die immer existieren
        text = frame["text"]
        needsinput = frame["input"]
        needscode = frame["code"]
        next_f = frame["next"]

        #speichert den render output
        render_output= self.render_eng.render(self.titel,text,needsinput,needscode)

        if needsinput: 
            #setzt den nächsten frame
            ifs=frame["ifs"] #liest ifs ein
            for i,j in enumerate(ifs): #geht durch alle ifs und entscheidet was slef.nextframe ist
                if render_output ==i+1:
                    self.nextframe = ifs[j] 
                    break

        elif needscode: 
            #Testet ob der Code richtig ist
            iscode = frame["is_code"] # liest iscode ein
            if iscode=="*": 
                self.nextframe=next_f
            else:
                self.nextframe = next_f if render_output == iscode else index
               
        else:  
            #testet ob es das ende ist. (siehe loadnextframe())
            self.nextframe=next_f if next_f else None

    def loadnextframe(self):
        #Ladet den nächsten Frame
        if self.nextframe:
            self.render_eng.load_screen()
            self.loadframe(self.nextframe)

        #return für den main loop
        else: return False
        return True

    def end_game(self):
        #endet das game
        self.render_eng.end_screen()

