import os

def split_labels_to_files(input_file, output_dir):
    """
    Splits a single text file containing all labels into individual label files,
    one for each image. If an image has multiple labels, they are added to the same file.

    Args:
        input_file (str): Path to the input text file.
        output_dir (str): Directory to save the individual label files.
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Read the input file
    with open(input_file, "r") as file:
        lines = file.readlines()

    # Process each line
    for line in lines:
        # Split the line into components
        parts = line.strip().split()
        if not parts:
            continue  # Skip empty lines

        # Extract the image file name and annotations
        image_name = parts[0]
        annotations = parts[1:]

        # Create a label file for the image
        label_file = os.path.join(output_dir, os.path.splitext(image_name)[0] + ".txt")

        # Write the annotations to the label file (one object per line)
        with open(label_file, "a") as f:  # Use 'a' mode to append if the file already exists
            for i in range(0, len(annotations), 5):
                object_line = " ".join(annotations[i:i+5])
                f.write(object_line + "/n")

    print(f"Created individual label files in '{output_dir}'.")

# Example usage
input_file = r"C:/Projects/ultralytics/smart_park_model_folder/val_labels.txt"  # Path to the single label file
output_dir = r"C:/Projects/ultralytics/smart_park_model_folder/val_labels"  # Directory to save individual label files
split_labels_to_files(input_file, output_dir)