from functions.write_file import write_file

def test():
    print('\nTEST 1:\n')
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    print('\nTEST 2:\n')
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    print('\nTEST 3:\n')
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
    test()