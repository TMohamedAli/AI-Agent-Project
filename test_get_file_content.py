from functions.get_file_content import get_file_content

def test():
    print("INITIAL TEST:\n")
    print(get_file_content("calculator", "lorem.txt"))
    
    print("\nTESTING MAIN:\n")
    print(get_file_content("calculator", "main.py"))

    print("\nTESTING CALCULATOR.PY:\n")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\nTEST DIRECTORY 1:\n")
    print(get_file_content("calculator", "/bin/cat"))

    print("\nTESTING INVALID FILE:\n")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    test()