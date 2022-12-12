from os import getcwd, chdir, rename
import glob


directory = "PDF's"
extension = 'pdf'

current_dir = getcwd()
chdir(directory)

pdf_list = glob.glob('*.' + extension)
chdir(current_dir)


for pdf in pdf_list:
  new_name = input("Please enter the last name of client:") + input("Enter File Type:") +".pdf"
  new_file_name = new_name
  rename(directory + "/" + pdf, directory + "/" + new_file_name)


