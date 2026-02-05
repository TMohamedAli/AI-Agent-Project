import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:

        abs_path_work_directory = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_path_work_directory, file_path))
        valid_target_path = os.path.commonpath([abs_path_work_directory, target_path]) == abs_path_work_directory

        if not valid_target_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(os.path.dirname(target_path), exist_ok = True)

        with open(target_path, "w") as file:
            file.write(content)
            if file.write(content) == len(content):
                return f'Successfully wrote "{file_path}" ({len(content)} characters written)'


    except Exception as e:
        return f'Error: {e}'

schema_write_file = types.FunctionDeclaration(
            name = "write_file",
            description = "Write content to a file. If file does not exist, create it at file_path",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                required=["file_path", "content"],
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="Path to the file to write or overwrite, relative to the working directory.",
                    ),
                    "content": types.Schema(
                        type=types.Type.STRING,
                        description="Content to be written to the file."
                    ),
                }
            )
        )