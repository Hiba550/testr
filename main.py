import cv2
import mediapipe as mp
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh()

while True:
    _, frame = cam.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multiface_landmarks
    print(landmark_points)
    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)


