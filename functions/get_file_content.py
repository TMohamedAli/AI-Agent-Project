import os
from config import MAX_CHARACTERS
from google.genai import types

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

schema_get_file_content = types.FunctionDeclaration(
            name = "get_file_content",
            description = "Read the contents of a file at the given file_path",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                required=["file_path"],
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="File path to the file to read contents from, relative to the working directory (default is the working directory itself)",
                    )
                }
            )
        )


    

    