import os
import errno

#defining  source and target folders
source = "C:/Users/joshu/Downloads"
target = "C:/Users/joshu/Downloads/Downloaded_images"

# Creating target folder if not there (compatible with older Python)
try:
    os.makedirs(target)
except OSError as e:
    # If the directory already exists, ignore the error; otherwise re-raise
    if e.errno != errno.EEXIST:
        raise

#loop through downloads folder
for file in os.listdir(source):
    #check for image file extensions
    if file.lower().endswith((".jpg", ".jpeg", '.png', '.webp')):
        #defining full file paths
        src_path = os.path.join(source, file)
        dest_path = os.path.join(target, file)

        #move file
        os.rename(src_path, dest_path)
        print(f'Moved: {file}')

print ('All images have been moved to Downloaded_images folder.')
