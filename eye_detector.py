import cv2
import keras
from keras.preprocessing import image
import numpy as np


def locator(full_name, media_folder = "media/"):
    eye_cascade = cv2.CascadeClassifier('static/data/haarcascade_eye.xml')
    '''find eyes in presented '''
    names = []
    name = full_name.split("/")[-1]
    img = cv2.imread(full_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eye = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in eye:
        ext_name = str(x + y) + "_" + name
        ext_img = img.copy()
        ext_img = ext_img[y:y + h, x:x + w]  # NOTE: its img[y: y + h, x: x + w]
        cv2.imwrite('{media_folder}{name}'.format(media_folder=media_folder+'converted/', name=ext_name), ext_img)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        names.append(ext_name)
    return names

def prediction(names,media_path = "media/converted/"):
    classifier = keras.models.load_model("static/data/model.h5")
    '''names  - list of file-names. image_path - where to find files'''
    results = []
    for name in names :
        test_image = image.load_img(media_path + name, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = classifier.predict(test_image)
        # print(result) # debug
        if result[0][0] == 1:
            results.append('woman')
        else:
            results.append('man')

    if results.count(('man')) > results.count(('woman')):

        return "MAN"
    elif results.count(('man')) < results.count(('woman')):

        return "WOMAN"
    else:

        return "TRY_AGAIN"

def pred (file_name):
    return prediction(locator(file_name))



#print (pred("media/1228picture.png"))


