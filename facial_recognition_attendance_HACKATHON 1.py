# Real Time Facial Recognition Using Webcam


import cv2
import numpy as np
import face_recognition
import os

path = 'photos for training'  # Path for the photos to train the model.
training_photos = []  # Photos in the central Database
student_names = []  # To capture the names from the photos from the database.
l1 = os.listdir(path)

for i in l1:
    current_image = cv2.imread(f'{path}/{i}')  # Current image is read
    training_photos.append(current_image)  # and appended to this list
    student_names.append(os.path.splitext(i)[0])  # Names corresponding to the images are also appended to list


def encode_images(training_photos):  # function for the encoding of images
    encoded_images_list = []
    for img in training_photos:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Images are converted to RGB for better detection and recognition
        image_location = face_recognition.face_locations(img)[0]  # location of the face in the image
        # 0th index suggests that the first face that is detected in an image is encoded.
        image_encode = face_recognition.face_encodings(img)[0]  # images are encoded
        encoded_images_list.append(image_encode)  # and appended to this list
    return encoded_images_list


known_encoded_images_list = encode_images(training_photos)  # encoded images from the function are stored in this list
print('Encoding Complete')

webcam_capture = cv2.VideoCapture(0)  # Live feed initialization

while True:
    success, img = webcam_capture.read()  # Feed from Webcam is captured
    # (In this case I have used webcam, however in real-life implementation, we'd use a camera module which costs
    # around 500 rupees)
    reduced_image = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # The image from the live-feed is reduced in size
    # This is done in order to speed up the process of facial-detection and recognition. Puts less load on the
    # processors
    reduced_image = cv2.cvtColor(reduced_image, cv2.COLOR_BGR2RGB)  # reduced image converted to RGB

    current_frame_faces = face_recognition.face_locations(reduced_image)  # checks for the faces in current frame
    current_frame_encode = face_recognition.face_encodings(reduced_image, current_frame_faces)  # encodes the faces in
    # current frame

    for face_encode, face_location in zip(current_frame_encode, current_frame_faces):  # zip aggregates the
        # iterables and returns single iterator object
        matches = face_recognition.compare_faces(known_encoded_images_list, face_encode)  # we verify the faces in
        # the current frame with the faces we have in our database
        face_distance = face_recognition.face_distance(known_encoded_images_list, face_encode)  # we calculate the
        # distance i.e. the measure to which the faces match. Face-Recognition library uses a method in which it
        # takes in account 128 distinctive features of a human face that are computer generated measurements and
        # then calculates certain values corresponding to those features. It can then compare the two faces on the basis
        # of how much they match, and returns a value which can be achieved through face_distance method.

        matched_face_index = np.argmin(face_distance)  # finds the best match from our database. It'll be used to
        # return the name corresponding to the best match.

        if matches[matched_face_index]:
            name = student_names[matched_face_index].upper()  # returns the name of the best match
            y1, x2, y2, x1 = face_location  # for creating a rectangle around the face in current frame
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # since, we decreased the size of our image from the
            # feed earlier by 1/4th, we now have to increase the size of the coordinates by 4

            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
            cv2.rectangle(img, (x1, y2 - 25), (x2, y2), (255, 255, 255), cv2.FILLED)
            cv2.putText(img, name + " | PRESENT", (x1 + 3, y2 - 3), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (0, 0, 0), 2)
            # face recognized and marked present.

    cv2.imshow('Live Feed', img)
    cv2.waitKey(1)

# now I just have to integrate this with the attendance system, i.e. as soon as our attendance module detects and
# recognizes a face, an entry in a excel sheet will be made with the in-time of the student and if they entered the
# class on time, they'll be marked present, otherwise they'll be marked absent.
