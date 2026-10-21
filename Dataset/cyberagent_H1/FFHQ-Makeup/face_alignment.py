import cv2
import os
import numpy as np
from mtcnn import MTCNN
from keras_facenet import FaceNet

def align_face():
    folder_path = "C:/Users/doron/Bilder/test"

    # List to hold the cropped faces
    faces_list = []

    # Initialize MTCNN detector and FaceNet extractor
    mtcnn = MTCNN(device="CPU:0")
    embedder = FaceNet()

    for filename in os.listdir(folder_path):
        
        image_path = os.path.join(folder_path, filename)
        
        # Load the image
        image = cv2.imread(image_path)

        # set BGR -> RGB for plotter
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

        # Detect faces and landmarks
        detection = mtcnn.detect_faces(image, threshold_onet=0.85)

        if detections:
            # Get bounding box of the detected face
            x, y, w, h = detection[0]['box']
            x1, y1 = max(0, x), max(0, y)
            
            # Crop and resize
            face_crop = image_rgb[y1:y1+h, x1:x1+w]
            face_resized = cv2.resize(face_crop, (160, 160))
            
            # Add to list
            faces_list.append(face_resized)
        else:
            print("No faces detected in the image.")

    # Convert list of images to a real 4D batch array (N, 160, 160, 3)
    faces_array = np.array(faces_list)

    # Generate embeddings for all faces in one call (no expand_dims)
    embeddings = embedder.embeddings(faces_array)

if __name__ == "__main__":
    align_face()