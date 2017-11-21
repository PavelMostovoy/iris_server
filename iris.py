import sys
from flask import Flask, render_template,request
import base64
import random


from os import path




app = Flask(__name__)




@app.route('/',methods=['GET','POST'])
def index():
    try:
        imgstring = request.form.get("imgBase64")
        imgstring = imgstring.replace(" ","+")

        print ("imgstring = ",imgstring)

        imgdata = base64.b64decode(imgstring.split(",")[1])
        print("imgdata = ", imgdata)

        name_gen = random.randint(100,1000)
        print ("gen name = ",name_gen)

        filename = str(f'{name_gen}picture.png')
        print("file name = ", filename)

        with open(filename, 'wb') as f:
            print ("saved as",filename)
            f.write(imgdata)

    finally:
        return render_template('index.html')




@app.route('/temp',methods=['GET','POST'])
def temp():
    imgstring = "empty"

    img_request = (request.form)
    imgstring = request.form.get("imgBase64")
    try:
        imgstring = imgstring.replace(" ", "+")
    except:
        pass

    print ("imgstring = ",imgstring)
    print("img_request = ", img_request)

    try :
        imgdata = base64.b64decode(imgstring.split(",")[1])
        print("imgdata = ", imgdata)
    except:
        imgdata = b"000"


    name_gen = random.randint(100,1000)
    print ("gen name = ",name_gen)

    filename = str(f'{name_gen}picture.png')
    print("file name = ", filename)

    with open(filename, 'wb') as f:
        print ("saved as",filename)
        f.write(imgdata)

    return render_template('temp.html')



@app.route('/home',methods=['GET','POST'])
@app.route('/home/',methods=['GET','POST'])
def home():
    test = request.form.get("img")
    print (type(test))
    print (test)

    return render_template('home.html')


@app.route('/camera',methods=['GET','POST'])
def camera():

    try:
        imgstring = request.form.get("imgBase64")

        print ("imgstring = ",imgstring)

        imgdata = base64.b64decode(imgstring.split(",")[1])
        print("imgdata = ", imgdata)

        name_gen = random.randint(100,1000)
        print ("gen name = ",name_gen)

        filename = str(f'{name_gen}picture.png')
        print("file name = ", filename)

        with open(filename, 'wb') as f:
            print ("saved as",filename)
            f.write(imgdata)

    finally:
        return render_template('camera.html')


@app.route('/stage',methods=['GET','POST'])
def staging():
    try:
        imgstring = request.form.get("imgBase64") # geting data from request
        imgstring = imgstring.replace(" ", "+")   # replacing the space chat to +
        imgdata = base64.b64decode(imgstring.split(",")[1])  # spliting sentance to neded data
        name_gen = random.randint(100,1000)                 # randomize naming
        filename = str(f'media\{name_gen}picture.png')      # generate file name
        # file_path = path.relpath(filename)               # file path ...
        with open(filename, 'wb') as f:
            print ("saved as",filename)
            f.write(imgdata)                         # saving file
    except:
        pass
    finally:
        return render_template('stage.html')





if __name__ == '__main__':
    app.run(debug=True)
