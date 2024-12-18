import cv2
from deepface import DeepFace
import webbrowser

Screen = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cv2.waitKey(100)
while Screen.isOpened():
    _, frame = Screen.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in face:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
        try:
            analyze = DeepFace.analyze(frame, actions=['emotion'])

            age = DeepFace.analyze(frame, actions=['age'])
            gender = DeepFace.analyze(frame, actions=['gender'])
            cv2.putText(img, analyze[0]["dominant_emotion"], (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0),
                        2)
            # cv2.putText(img, age[0]["age"], (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 800), 4)
            print(analyze)
            print(analyze[0]["dominant_emotion"])
            print(age)
            print(age[0]["age"])
            print(gender)
            print(gender[0]["dominant_gender"])

            if analyze[0]["dominant_emotion"] == 'happy' and age[0]["age"] < 15:
                print("Showing song recommendations for happy mood....")
                #trending tamil
                webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DX4Im4BTs2WMg?si=4ed04110a8c74434")
                Screen.release()
                exit()

            if analyze[0]["dominant_emotion"] == 'sad' and age[0]["age"] < 15:
                print("Showing song recommendations for sad mood....")
                #2k melodies
                webbrowser.open("https://open.spotify.com/playlist/07iEYDeEOVKEZ7XOv9P1aH?si=24197be509ee4abe")
                Screen.release()
                exit()

            if analyze[0]["dominant_emotion"] == 'angry' or analyze[0]["dominant_emotion"] == 'fear' and age[0]["age"] < 15:
                print("Showing song recommendations to calm your anger....")
                #chill vibes
                webbrowser.open("https://open.spotify.com/playlist/5nG3U5u6Q7Zcl8mjkrqHpX?si=b396ada3fb1440a8")
                Screen.release()
                exit()
            if analyze[0]["dominant_emotion"] == 'happy' and age[0]["age"] < 40 and age[0]["age"] > 15:
                print("Showing song recommendations for happy mood....")
                webbrowser.open("https://open.spotify.com/playlist/5nG3U5u6Q7Zcl8mjkrqHpX?si=b396ada3fb1440a8")
                Screen.release()
                exit()
            if analyze[0]["dominant_emotion"] == 'sad' and age[0]["age"] < 40 and age[0]["age"] > 15:
                print("Showing song recommendations for sad mood...")
                webbrowser.open("https://open.spotify.com/album/5qPbqRXgkPgMsqCmA3Dn1I?si=9NQgikVQQWiwV3-BS4R-fQ")
                Screen.release()
                exit()
            if analyze[0]["dominant_emotion"] == 'anger' or analyze[0]["dominant_emotion"] == 'fear' and age[0]["age"] < 40 and age[0]["age"] > 15:
                print("Showing song recommendations to calm your anger....")
                webbrowser.open("https://open.spotify.com/album/5qPbqRXgkPgMsqCmA3Dn1I?si=9NQgikVQQWiwV3-BS4R-fQ")
                Screen.release()
                exit()
            if analyze[0]["dominant_emotion"] == 'happy' and age[0]["age"] > 40:
                print("Showing song recommendations for happy mood...")
                #80s punch
                webbrowser.open("https://open.spotify.com/playlist/7nCANwL3luPdhb5G7Xvw7A?si=dd288acb67a244fa")
                Screen.release()
                exit()
            if analyze[0]["dominant_emotion"] == 'sad' and age[0]["age"] > 40:
                print("Showing song recommendations for sad mood...")
                #old melodies
                webbrowser.open("https://open.spotify.com/playlist/3ZQPI3XuRSuSs5isX3bQsX?si=76f86c56d2fe44ce")
                Screen.release()
                exit()

if analyze[0]["dominant_emotion"] == 'anger' or analyze[0]["dominant_emotion"] == 'fear' and age[0]["age"] > 40 :
                print("Showing song recommendations to calm your anger....")
                #80s melodies
                webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DWWOp144dTCQd?si=e866dc520b794dac")
                Screen.release()
                exit()

        except:
            print("no face")

    cv2.imshow('Screen', frame)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
Screen.release()