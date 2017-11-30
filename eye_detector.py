import cv2
import keras
from keras.preprocessing import image
import numpy as np

eye_cascade = cv2.CascadeClassifier('static/data/haarcascade_eye.xml')

classifier = keras.models.load_model("static/data/model.h5")

image_path = "media/"
#image_name = "968_many.jpg"


def locator(image_name,image_path):
    names = []
    img = cv2.imread(image_path + image_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eye = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in eye:
        name = str(x + y) + "_" + image_name
        t_img = img.copy()
        t_img = t_img[y:y + h, x:x + w]  # NOTE: its img[y: y + h, x: x + w]
        cv2.imwrite("{file_path}{file_mane}".format(file_path=image_path, file_mane=name), t_img)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        names.append(name)
    return names


# processor = locator(image_name,image_path)

def prediction(names,image_path="media/"):
    results = []
    for name in names :
        test_image = image.load_img(image_path + name, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = classifier.predict(test_image)
        print(result) # debug
        if result[0][0] == 1:
            results.append('woman')
        else:
            results.append('man')

    if results.count(('man')) > results.count(('woman')):
        print("man")
        return "MAN"
    elif results.count(('man')) < results.count(('woman')):
        print("woman")
        return "WOMAN"
    else:
        print("try_again")
        return "TRY_AGAIN"




def f_prediction(image_name,image_path="media/"):
    return prediction(locator(image_name,image_path))





'''
temp = prediction(processor)

temp2 = f_prediction(image_name,image_path)

print (temp2)
'''