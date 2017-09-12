# An introduction to programming: Finch Robots
# Huskie Robotics 9/27/17


import Finch
import time

class Finch():
    def __init__(self):
        self.connection = finchconnection.ThreadedFinchConnection()
        self.connection.open()


    def go(self):
        """this is where instructions for the finch robot will go"""





    
def main():
    finch = Finch()
    finch.go()
    finch.halt()
    finch.close()

main()
