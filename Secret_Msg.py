import os
import string
def rename_files():
   file_list= os.listdir(r"E:\Python Udacity\prank\prank")
   print(file_list)
   for file_name in file_list:
       file_name.lstrip("0123456789")
       os.chdir(r"E:\Python Udacity\prank\prank")
       os.rename(file_name,file_name.lstrip("0123456789"))
       
    
rename_files()
