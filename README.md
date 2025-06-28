# Gender-detection-and-age-estimation-using-AI-ML-
A simple Beginner friendly AI/ML project. Technologies used in this project is Pyhton and its libraries such as OpenCV, Math, Argparse, Time.
Here I given 2 datasets that are agelist for pedicting age and genderlist for definning or age ('male','female') that datasets is labelled.
OpenCV captures the face of the person live using webcam or else you can pass the image of the person.
it uses BLOB for capturing large object its may be Video and files. 
for face detection is used DNN model,for gender gender_net.caffemodel and age age_net.caffemodel to predict age and gender of particular person.
Pre-trained Model Files Required:opencv_face_detector.pbtxt, opencv_face_detector_uint8.pb
age_deploy.prototxt, age_net.caffemodel
gender_deploy.prototxt, gender_net.caffemodel
