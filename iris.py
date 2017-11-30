from flask import Flask, render_template,request
import base64
import random
import time
import eye_detector

#import tensorflow
#import keras
# media_folder = "/var/www/iris/media/"
media_folder = "media/"


app = Flask(__name__)


@app.route('/api',methods=['GET','POST'])
def staging():
    try:
        imgstring = request.form.get("imgBase64") # geting data from reques
        imgstring = imgstring.replace(" ", "+")   # replacing the space chat to +
        imgdata = base64.b64decode(imgstring.split(",")[1])  # spliting sentance to neded data
        name_gen = random.randint(100,10000)                 # randomize namin
        #filename = '/var/iris/media/picture.png'      # generate file name  f" " - allowed on python 3.6+
        filename = "{0}{1}picture.png".format( media_folder,name_gen)
        # print(filename)
        with open(filename, 'wb') as f:
            f.write(imgdata)                         # saving file

        #processor  = eye_detector.locator("{name_gen}picture.png".format(name_gen=name_gen),media_folder)

        pred = eye_detector.prediction(names = eye_detector.locator("{name_gen}picture.png".format(name_gen=name_gen),media_folder))
        print (pred)

    except:
        pass
    finally:
        return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def api_point():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
