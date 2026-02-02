import os
from config import MAX_CHARACTERS

def get_file_content(working_directory, file_path):
    try:

        abs_path_work_directory = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_path_work_directory, file_path))
        valid_target_path = os.path.commonpath([abs_path_work_directory, target_path]) == abs_path_work_directory

        if not valid_target_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_path, "r") as file:
            file_content = file.read(MAX_CHARACTERS)
            if file.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARACTERS} characters]'
                return file_content
        return file_content
    except Exception as e:
        return f'Error: {e}'



    

    