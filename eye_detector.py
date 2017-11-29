import cv2

eye_cascade = cv2.CascadeClassifier('//static//data//haarcascade_eye.xml')

def eye(image_name):
    img = cv2.imread(image_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eye = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in eye:
        name = str(x+y+image_name)
        t_img=img.copy()
        t_img = t_img[y:y + h, x:x + w] # NOTE: its img[y: y + h, x: x + w]
        cv2.imwrite(name, t_img)
        yield  name
