import re
import os

class Utils:
    def __init__(self):
        print("constructor")

    def get_user_id(self, email):
        user_id = re.sub('@.+$', '', email)

        return user_id
    
    def write_document(self,path,file_name,text,mode):
        try:
            entire_path = os.path.join(path,file_name+".txt")
            with open(entire_path, mode) as file:
                file.write("-".join(text))
        except Exception as e:
            print("An error", e)

    def files_exist(self, file, folder_name):
        path_folder = os.path.join(os.environ["GENERAL_PATH"],folder_name)
        path_file = os.path.join(path_folder,file)
        is_exist = os.path.exists(path_file)

        return is_exist
    
    def get_document_type(self,file_name):
        array_name = file_name.split(".")
        format_doc = array_name[1].lower()

        return format_doc


