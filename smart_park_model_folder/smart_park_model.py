from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on our parking_dataset for 100 epochs
results = model.train(
    data="dataset_config.yaml", 
    epochs=100, 
    imgsz=640, 
    batch=16,
    save_period=5, 
    project="smart_park_model_folder",
    name="saved_models")