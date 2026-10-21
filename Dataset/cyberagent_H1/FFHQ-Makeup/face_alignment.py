import cv2
from mtcnn import MTCNN
from mtcnn.utils.plotting import plot
from keras_facenet import FaceNet
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("C:/Users/doron/Bilder/kim_is_calling.png")

# set BGR -> RGB for plotter
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

# Initialize MTCNN detector and FaceNet extractor
mtcnn = MTCNN(device="CPU:0")
embedder = FaceNet()

# Detect faces and landmarks
detection = mtcnn.detect_faces(image, threshold_onet=0.85)

if detections:
    # Extract the bounding box of the first detected face
    x, y, w, h = detections[0]['box']
    
    # Ensure coordinates don't fall outside the image boundaries
    x1, y1 = max(0, x), max(0, y) 
    
    # Crop the face from the RGB image
    face_crop = image_rgb[y1:y1+h, x1:x1+w]
    
    # FaceNet requires a standard input size of 160x160 pixels
    face_resized = cv2.resize(face_crop, (160, 160))
    
    # Generate the embedding (convert single image to a batch of 1 using expand_dims)
    embedding = embedder.embeddings(np.expand_dims(face_resized, axis=0))
    
    print(f"Success! Generated an embedding vector of shape: {embedding.shape}")
    # Print the first few numbers to verify it worked
    print(f"First 5 embedding values: {embedding[0][:5]}")
else:
    print("No faces detected in the image.")

# Plot the results
plt.imshow(plot(image_rgb, detection))
plt.show()