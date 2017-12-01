from flask import Flask, render_template, request
import base64
import random

from eye_detector import pred


# media_folder = "/var/www/iris/media/"
media_folder = "media/"


app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def staging():
    try:
        imgstring = request.form.get("imgBase64")  # geting data from reques
        imgstring = imgstring.replace(" ", "+")   # replacing the space chat to +
        imgdata = base64.b64decode(imgstring.split(",")[1])  # spliting sentance to neded data
        name_gen = random.randint(100, 10000)                 # randomize namin
        # filename = '/var/iris/media/picture.png'     #  generate file name  f" " - allowed on python 3.6+
        filename = "{0}{1}picture.png".format(media_folder, name_gen)
        # print(filename)
        with open(filename, 'wb') as f:
            f.write(imgdata)                         # saving file
        print(pred(filename))                        # final return - need to be processed on web UI
    finally:
        return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def api_point():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
