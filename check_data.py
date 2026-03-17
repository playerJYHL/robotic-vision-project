import cv2
import os

# Define directories for images and labels
image_dir = 'dataset/train/images'
label_dir = 'dataset/train/labels'

# Get the filename of the first image in the directory
img_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.png')]
if not img_files:
    print("Error: No images found. Please check the directory path or file extensions!")
    exit()

sample_img_name = img_files[0]
sample_label_name = os.path.splitext(sample_img_name)[0] + '.txt'

img_path = os.path.join(image_dir, sample_img_name)
label_path = os.path.join(label_dir, sample_label_name)

# 1. Read the image using OpenCV
img = cv2.imread(img_path)
h, w, _ = img.shape  # Extract image height (h) and width (w)

print(f"Displaying image: {sample_img_name} | Resolution: {w}x{h}")

# 2. Read the corresponding label file
if os.path.exists(label_path):
    with open(label_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        # Parse YOLO format: class_id, x_center, y_center, width, height
        parts = line.strip().split()
        class_id = int(parts[0])
        x_center, y_center, box_width, box_height = map(float, parts[1:])

        # Core Math Logic: Convert normalized ratios (0~1) to absolute pixel coordinates
        # Calculate the absolute pixel coordinates of the bounding box center
        cx, cy = int(x_center * w), int(y_center * h)
        # Calculate the absolute pixel width and height of the bounding box
        bw, bh = int(box_width * w), int(box_height * h)

        # Compute the top-left (x1, y1) and bottom-right (x2, y2) coordinates
        x1 = int(cx - bw / 2)
        y1 = int(cy - bh / 2)
        x2 = int(cx + bw / 2)
        y2 = int(cy + bh / 2)

        # 3. Draw the bounding box (Color: Green, Thickness: 2)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Put the Class ID text above the bounding box
        cv2.putText(img, f"Class: {class_id}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
else:
    print("Warning: No corresponding label file found for this image.")

# Display the image with bounding boxes
cv2.imshow('Data Sanity Check', img)
cv2.waitKey(0)  # Wait indefinitely until a key is pressed
cv2.destroyAllWindows()
