import json
import os
import sys

def main(path):
    with open(os.path.join(os.path.dirname(__file__), path), 'r') as json_file:
        data=json.load(json_file)
    
    for i in data:
        try: os.system("clear")
        except : os.system("cls")
        
        # print(sys.argv)
        print(f"{i} :\n")
        print(data[i]["text"])
        input()

if __name__ == '__main__':
    main(sys.argv[1])