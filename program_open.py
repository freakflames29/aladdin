import os
try:
    def open(program):
        os.system(program)
except Exception as e:
    print("There is an error opening the program: ")
