import os
import shutil

# Get the actual user home directory (e.g. C:\Users\Acer Aspire 3)
home = os.path.expanduser("~")

# Build paths safely
source = os.path.join(home, "Pictures", "source_folder")
destination = os.path.join(home, "Pictures", "automation_folder")

# Create destination folder
os.makedirs(destination, exist_ok=True)

# Copy only .jpg files
if os.path.isdir(source):
    for file in os.listdir(source):
        if file.lower().endswith(".jpg"):
            src_file = os.path.join(source, file)
            dest_file = os.path.join(destination, file)

            if os.path.isfile(src_file):
                shutil.copy(src_file, dest_file)

print("All .jpg files copied successfully!")


