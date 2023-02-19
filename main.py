import sys
from os import system
import eel

@eel.expose
def helloWorld():
    print("Hello, World!")

if sys.argv[1] == "--develop":
    @eel.expose
    def stop():
        sys.exit()

    eel.init("client")
    eel.start({ "port": 5173 }, port=8888)
else:
    eel.init("build")
    eel.start("index.html")

system("cls")