import face_recognition
import cv2
import numpy as np
import os

KNOWN_FACES_DIR = "known_faces"

known_face_encodings = []
known_face_names = []

for filename in os.listdir(KNOWN_FACES_DIR):
    path = os.path.join(KNOWN_FACES_DIR, filename)
    image = face_recognition.load_image_file(path)
    encoding = face_recognition.face_encodings(image)[0]
    
    known_face_encodings.append(encoding)
    known_face_names.append(os.path.splitext(filename)[0])

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    rgb = frame[:, :, ::-1]

    locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, locations)

    for encoding, location in zip(encodings, locations):
        matches = face_recognition.compare_faces(known_face_encodings, encoding)
        name = "Unknown"

        distances = face_recognition.face_distance(known_face_encodings, encoding)
        if len(distances) > 0:
            best = np.argmin(distances)
            if matches[best]:
                name = known_face_names[best]

        top, right, bottom, left = location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("AI Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
