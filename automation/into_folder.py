import os

#defining  source and target folders
source = "C:/Users/joshu/Downloads"
target = "C:/Users/joshu/Downloads/Downloaded_images"

# Creating target folder if not there
os.makedirs(target, exists_ok=True)

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
