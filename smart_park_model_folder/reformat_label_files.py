import os
from PIL import Image

def convert_to_yolo_format(label_folder, image_folder, output_folder):
    """
    Converts labels from `image_file class_id x_min y_min x_max y_max` format to YOLO format.
    
    Args:
        label_folder (str): Path to the folder containing the original labels.
        image_folder (str): Path to the folder containing the corresponding images.
        output_folder (str): Path to the folder where YOLO-formatted labels will be saved.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each label file in the label folder
    for label_file in os.listdir(label_folder):
        if not label_file.endswith(".txt"):
            print(f"Skipping non-text file: {label_file}")
            continue

        label_path = os.path.join(label_folder, label_file)
        image_file = label_file.replace(".txt", ".jpg")  # Assuming images are in .jpg format
        image_path = os.path.join(image_folder, image_file)

        # Check if the image file exists
        if not os.path.exists(image_path):
            print(f"Image file not found: {image_path}")
            continue

        # Open the image to get its dimensions
        try:
            with Image.open(image_path) as img:
                image_width, image_height = img.size
        except Exception as e:
            print(f"Error opening image {image_path}: {e}")
            continue

        # Read the original label file
        try:
            with open(label_path, "r") as file:
                lines = file.readlines()
        except Exception as e:
            print(f"Error reading label file {label_path}: {e}")
            continue

        # Process each line in the label file
        yolo_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) != 6:
                print(f"Skipping malformed line in {label_file}: {line}")
                continue

            image_file, class_id, x_min, y_min, x_max, y_max = parts
            try:
                x_min, y_min, x_max, y_max = float(x_min), float(y_min), float(x_max), float(y_max)
            except ValueError:
                print(f"Skipping line with invalid coordinates in {label_file}: {line}")
                continue

            # Calculate YOLO format values
            x_center = (x_min + x_max) / 2 / image_width
            y_center = (y_min + y_max) / 2 / image_height
            width = (x_max - x_min) / image_width
            height = (y_max - y_min) / image_height

            # Append the YOLO-formatted line
            yolo_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

        # Save the YOLO-formatted labels to the output folder
        output_path = os.path.join(output_folder, label_file)
        try:
            with open(output_path, "w") as file:
                file.writelines(yolo_lines)
            print(f"Converted {label_file} to YOLO format. {len(yolo_lines)} lines written.")
        except Exception as e:
            print(f"Error writing to {output_path}: {e}")

# Example usage
label_folder = "parking_dataset/train_labels"  # Folder containing original labels
image_folder = "parking_dataset/train_images"  # Folder containing corresponding images
output_folder = "parking_dataset/formatted_train_labels"  # Folder to save YOLO-formatted labels

convert_to_yolo_format(label_folder, image_folder, output_folder)