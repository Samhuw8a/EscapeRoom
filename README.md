# **Informatik Projekt: EscapeRoom**

# Einleitung:
Dies ist ein Text basiertes Game welches in python geschrieben wurde und die Frames im Json format speichert.
Dieses Projekt ist ein Projekt welches wir im Informatik geschrieben haben.
In diesem README werde ich die Struktur des Programmes zeigen.
# Die Struktur:
Als ertste habe ich mich mit der Struktur des Programms auseinander
gesetzt. Ich habe das Projekt in Drei Teile Aufgeteilt. 
> [Input und Output](front_end.py)

> [Logik](back_end.py)

> [Storage](Frames.json)

## Front_end:
Das Projekt hat ein Front_end das die Frames formatiert auf den Bildschirm
bringt. Die datei hat eine Klasse Render() die beinhaltet:

- eine render methode zuständig für den outut und input 
- eine animation methode die den Text animiert
- und andere interne methoden

```python
class Render():
    def __init__(self):
        #"globale Var"

    def animation(self,text):
        #Animiert einen Text
    
    def render(self):
        #Printet den Frame
```

## Back_end:
Das die Render klasse die richten Frames zum rendern bekommt,
braucht das game einen Frame_Handler.
Dieser bekomt einen Render klasse und einen Datei mit den Frames in diesem fall Frames.json
Dieser Handler Beinhaltet:
- eine Loadframe method
- eine Loadnext-frame method
- und eine Optionale Import-json method
- Die Klasse hat auch eine Var. next_frame

```python
class Handler():
    def __init__(self,frames_raw=None):
        self.next_frame=None
    
    def imp_json(self):
        #Importiert eine Json Datei
        #und schreibt diese in self.frames_raw
    
    def load_frame(self,index):
        #Ladet den Frame "index" von Frames raw

    def load_next_frame(self):
        #Ladet den nächsten Frame
        self.loadframe(self.nextframe)
```

## Frames.json
Die Frames werden Roh in der Frames.json datei gespeichert.
Jeder Frame hat:
- einen Index
- einen Text
- ein bool input
- ein bool code
- und ein next

Die Json datei ist so gestaltet:

```json
{
    "Index des Frames":{
        "text":"Der Text des Frames",
        "input": false, //oder eine die anzahl der Inputs\\
        "code": false, // bool der angibt ob es einen Code gibt
        "next": "n", // Index des nächsten Frames
        "is_code": "Der Code",//Der Code des Frames (existiert nur wenn code != false)
        "ifs":{
            "if_n":"index" // wenn die n te wahl ausgewält wird
                        //wird der Frame "index" als nächster gesezt.
            // existiert nur wenn input != false
        }

    }
}
```

## Zusammenfassung:
| Teile:| funktion:|
|---|---|
|[main.py](main.py)| beinhaltet den Main-loop|
|[back_end.py](back_end.py)|verantwortlich für die Logik des Programm|
|[front_end.py](front_end.py)|verantwortlich für den output und den User input|
|[Frames.json](Frames.json)|speichert die Frames mit allen informationen|

# Die "Entwickler-Tools":
Das Projekt hat auch "Tools" um verschiedene Aspekte
zu testen oder die Json dateien zu schreiben.
Zu diesen Tools gehören:
- [Test.json](Test.json)
- [Json_create](Json_create.py)
- [Frame_tester](Frame_tester.py)

## Test.json:
Die Test.json Datei ist genau wie Frames.json aufgebaut.
Hat aber nur 9 Frames die alle atribute "Testen".
Diese Datei Wird zum Testen der front und back -end Dateinen Benötigt
Es ist viel einfacher probleme zu finden, wenn man alles möglichst simple hält.

## Frame_tester:
Die Frame_tester Datei dient dazu den Text zu kontrolieren.
Die Datei gibt den index und den Text jedes Textes einer Kompatiblen Json-datei
aus. Die Json-datei wird im als erstes Argument der Datei einglesen.
```bash
python3 ./Frame_tester.py Json-datei
```

## Json_create:
Die Json_create Datei schreibt eine Kompatible Json datei oder Erweitert eine
bereits existierende Datei.
Mit dieser Datei ist es viel einfacher eine kompatible Json-datei zu schreiben.
