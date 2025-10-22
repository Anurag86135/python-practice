def myfun():
    print("Hello world!")


if __name__=="__main__":
    # ?if this code is directly excecuted by running the file its present in 
    print("We are directly running this code")
    myfun()
    print(__name__)


    # '__name__' evaluate to the name of the module in python from where the program is ran.

    # if the module is being run directly from the command line , the '__ name __ is set to string "__main__'.
    # Thus, this behaviour is used to check wehter the module is run directly or imported to another file.

