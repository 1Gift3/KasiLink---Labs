import os 
#Checking working dir
#print(os.getcwd())

for file in os.listdir("C:/Users/joshu/Downloads"):
    if file.endswith(".jpg"):
        os.rename(f"C:/Users/joshu/Downloads/{file}", f"C:/Users/joshu/Pictures/{file}")

