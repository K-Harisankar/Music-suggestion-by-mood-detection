# Music-recommendation-based-on-mood-detection
Python based program to detect emotions and recommend music based on current mood

The Human facial expressions are important for visually 
expressing a lot more information. Facial expression recognition is 
essential in the field of human-machine interaction. Automated facial 
recognition systems have many applications, including understanding of 
human behavior, diagnosing mental disorders, and synthetic human 
expression. Identifying facial expressions through computers with high 
detection rates is still a challenging task.


Computer animated agents and robots bring new dimension in
 human computer interaction which makes it vital as how computers can 
affect our social life in day-to-day activities. Face to face 
communication is a real-time process operating at a a time scale in the 
order of milliseconds. The level of uncertainty at this time scale is 
considerable, making it necessary for humans and machines to rely on 
sensory rich perceptual primitives rather than slow symbolic inference 
processes.


In this project we are presenting the real time facial 
expression recognition of seven most basic human expressions.We have 
used a variety of intensive deep learning techniques (convolutional 
neural networks) to identify the main seven universal human emotions:


I. Neutral II. Angry III. Disgust IV. Fear V. Happy VI. Sadness VII. Surprise


Problem
For
 any real time image taken from our web camera, our goal is to predict 
the expression of the face in that image out of seven basic human 
expression.
i.e. CLASSIFY THE EXPRESSION OF FACE IN IMAGE OUT OF SEVEN BASIC HUMAN EXPRESSION


Project Formulation
The hands on building this project of Facial Expression Recognition is divided into following tasks/steps:-

•	Import essential modules and helper functions from NumPy, cv2, deepface.

•	We than run the main.py script to serve the model's predictions to a web interface.


•	Applied the model for real time recognition of facial expresssions of users using webcam of the Laptop.


Dataset Description
 The data consists of 48x48 pixel grayscale images of faces. The faces 
have been automatically registered so that the face is more or less 
centered and occupies about the same amount of space in each image. The 
task is to categorize each face based on the emotion shown in the facial
 expression in to one of seven categories (0=Angry, 1=Disgust, 2=Fear, 
3=Happy, 4=Sad, 5=Surprise, 6=Neutral).


Prerequisites
You need to have installed following softwares and libraries in your machine before running this project.


1.Python 3

2.OpenCV

3.DeepFace

Project Structure

Locating faces in the scene




Extracting facial features from the detected face region




Analyzing the motion of facial features and/or the changes in the appearance of facial features




Steps followed for building the project
As per various surveys it is found that for implementing this project four basic steps are required to be performed.


i.) Preprocessing- Preprocessing is a common name for 
operations with images at the lowest level of abstraction both input and
 output are intensity images.


ii.) Face registration- Face Registration is a computer 
technology being used in a variety of applications that identifies human
 faces in digital images.


iii.) Facial feature extraction- Facial Features 
extraction is an important step in face recognition and is defined as 
the process of locating specific regions, points, landmarks, or 
curves/contours in a given 2-D image or a 3D range image.


iv.) Emotion classification- In this step, of 
classification, the algorithm attempts to classify the given faces 
portraying one of the seven basic emotions.


Conclusion
Therefore by following these steps, in this project a 
Emotion/Facial Recognition model has been trained and saved. It can 
recognize/detect the facial expressions of an individual on a real time 
basis that whether the individual is  Neutral, Angry, Disgust, Fear, 
Happy, Sad, Surprised.

