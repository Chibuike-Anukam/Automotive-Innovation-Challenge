import os

# Paths from dataset_config.yaml
path = r"C:/Projects/ultralytics/parking_dataset"  # Use raw string (r"") to avoid escape characters
train_images = os.path.join(path, "train_images")  # Correct relative path
val_images = os.path.join(path, "val_images")      # Correct relative path

# Check if directories exist
print("Train images directory exists:", os.path.exists(train_images))
print("Validation images directory exists:", os.path.exists(val_images))

# Check if directories contain images
if os.path.exists(train_images):
    print("Number of training images:", len(os.listdir(train_images)))
else:
    print("Training images directory not found.")

if os.path.exists(val_images):
    print("Number of validation images:", len(os.listdir(val_images)))
else:
    print("Validation images directory not found.")