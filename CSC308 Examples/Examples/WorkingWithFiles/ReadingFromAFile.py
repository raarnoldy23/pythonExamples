# Program to read from a file 


def main():
    name = open ('hello.txt', 'r')
    contents = name.read ()
    name.close
    print(contents)
    



main()