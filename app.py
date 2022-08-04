from flask import Flask

app = Flask(__name__)

@app.route('/my_app',methods = ['GET','POST'])
def message():
    return 'This is my ml project with complete pipeline'


if __name__=='__main__':
    app.run(debug=True)


    