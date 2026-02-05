import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_work_path_dir = os.path.abspath(working_directory)
        abs_file_path= os.path.normpath(os.path.join(abs_work_path_dir, file_path))
        valid_target_path = os.path.commonpath([abs_work_path_dir, abs_file_path]) == abs_work_path_dir

        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not abs_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", abs_file_path]

        if args:
            command.extend(args)
        result = subprocess.run(
            command,
            cwd=abs_work_path_dir, 
            capture_output=True,
            text=True, 
            timeout= 30
        )
        output = []
        if result.returncode != 0:
            output.append(f'Process exited with code {result.returncode}')
        if  not result.stdout and not result.stderr:
            output.append('No output produced')
        if result.stdout:
            output.append(f'STDOUT: \n{result.stdout}')
        if result.stderr:
            output.append(f'STDERR: \n{result.stderr}')
        return "\n".join(output)
    except Exception as e:
        return f'Error: executing python file: {e}'

schema_run_python_file = types.FunctionDeclaration(
            name = "run_python_file",
            description = "Exectute a python file at the given file_path with optional command-line arguments",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                required=["file_path"],
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="the path to the Python file to execute, relative to the working directory",
                    ),
                    "args":types.Schema(
                        type=types.Type.ARRAY,
                        items=types.Schema(type=types.Type.STRING),
                        description="optional arguments passed to the script "
                    )
                }
            )
        )    

