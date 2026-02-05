import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        abs_path_work_directory = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path_work_directory, directory))
        valid_target_path = os.path.commonpath([abs_path_work_directory, target_dir]) == abs_path_work_directory

        if not valid_target_path:
            return f'Error: Cannot list "{directory}" as it is a outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{target_dir}" is not a directory'
        
        directory_contents =[]
        for item in os.listdir(target_dir):
            name = item
            file_size = os.path.getsize(os.path.join(target_dir, item))
            is_dir = os.path.isdir(os.path.join(target_dir, item))
            directory_contents.append(f"- {name}: file_size={file_size} bytes, is_dir={str(is_dir)}")
        return "\n".join(directory_contents)
    except Exception as e:
        return f"Error: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
            name = "get_files_info",
            description = "List files in a specified directory relative to the working directory, providing file size and directory status",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "directory": types.Schema(
                        type=types.Type.STRING,
                        description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
                    )
                }
            )
        )