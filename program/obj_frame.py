# from ultralytics import YOLO
# from IPython.display import display, Image
# import subprocess

# # Assuming you have already loaded the YOLO model
# model = YOLO('yolov8n.pt')

# # Define the YOLO command as a list of arguments
# yolo_command = [
#     'yolo',
#     'task=detect',
#     'mode=predict',
#     'model=yolov8n.pt',
#     'conf=0.25',
#     'source=./trafic.png',
#     'save=True'
# ]

# # Run the YOLO command using subprocess
# subprocess.run(yolo_command, shell=True)

# # Display the resulting image
# Image(filename='runs/detect/predict/trafic.png', height=600)
