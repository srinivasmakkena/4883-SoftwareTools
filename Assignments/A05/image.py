from PIL import Image
import os


currentlocation=os.path.dirname(os.path.abspath(__file__))
folder_path = currentlocation+'\\resources\\images\\'
target_size = (400, 400)

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    image = Image.open(file_path)
    
    resized_image = image.resize(target_size)
    
    resized_image.save(file_path)

print("Image resizing complete.")
