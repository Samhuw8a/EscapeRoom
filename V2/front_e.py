import sys
import time

class Renderer():
    def __init__(self,titel,end_screen):
        self.end_screen = end_screen
        self.titel = titel

    def unpack_frame(self,frame: dict)-> tuple:
        text = frame["text"]
        inp = frame["input"]
        code = frame["code"]
        other = {}

        if "input"in frame.keys():
            other["input"] = frame["input"]
        if "is_code"in frame.keys():
            other["is_code"] = frame["is_code"]

        return (text,inp,code,other)

    def render(self,frame: dict)-> None:
        text,inp,code,other = self.unpack_frame(frame)

        print(self.titel)
        self.animate(text,0.032)

        while True:
            try:
                if inp:
                    pass
                elif code:
                    pass

                break

            except ValueError: 
                pass
            except KeyboardInterrupt: 
                exit()



    @staticmethod
    def animate(text:str,t:float)-> None:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(t)

def main():
    r = Renderer("Titel","tsg")
    f = {
        "text": "Das ist Text 4",
        "input": 2,
        "code": False,
        "next": None,
        "ifs": {
            "if_1": 5,
            "if_2": 6
        }
    }
    r.render(f)

if __name__ == '__main__':
    main()
