import threading
from flask import Flask, render_template, request
from multiprocessing import Process
import threading

from time import sleep
from bogosort import Bogo

app = Flask(__name__)

# Bogosort
bogo = Bogo()
bogo.setup( [2,9,4,1,6,3,7,8,5] )
def runa():
    while not bogo.sorted:
        bogo.sort()
        sleep( 1 )

p = threading.Thread( target=runa )
p.daemon = True
p.start()

@app.route("/")
@app.route("/home")
def home():
    silnia = 3265920 # 9! * 9 for n = 9
    title = "Main page"
    return render_template( 'home.html', 
            title=title, 
            done=bogo.sorted,
            count=bogo.count, 
            maks=silnia,
            best=bogo.closest,
            percent=(bogo.count/silnia)*100, 
            lista=bogo.lista, 
            lenlista=len(bogo.lista),
            history=bogo.history, 
            hislen=len(bogo.history)
     )

@app.route("/about")
def about():
    title = "About page"
    return render_template( 'about.html', title=title )

if __name__ == '__main__':
    app.run( debug=True)

