import os

def rename_files():
    #(1) get file names from a given folder
    file_list = os.listdir(r"C:\Users\Sebastian Bethell\Desktop\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is "+saved_path)
    os.chdir(r"C:\Users\Sebastian Bethell\Desktop\prank")
    #(2) rename files
    for file_name in file_list:
        print("Old file name "+file_name)
        print("New file name "+ file_name.translate(None,"0123456789"))
        os.rename(file_name, file_name.translate(None,"0123456789"))


rename_files()
