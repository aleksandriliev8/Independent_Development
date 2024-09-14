import os

folder_original = 'C:\\Users\\1\\Desktop\\Programming\\Development\\Python\\Python_Fundamentals\\file_clean_up\\files_to_be_cleaned'
folder_destination = 'C:\\Users\\1\\Desktop\\Programming\\Development\\Python\\Python_Fundamentals\\file_clean_up\\cleaned_up'

# Create the new directory
os.mkdir(folder_destination)

for entry in os.scandir(folder_original):
    
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)

    if os.path.isfile(location_original):
        os.rename(location_original, location_destination)