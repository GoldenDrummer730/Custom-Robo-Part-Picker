import time
import pymem
import pygame
import json

pm = pymem.Pymem('Dolphin.exe')
pygame.init()

SELECT = 6
DOWNPAD = 0
MEMADD = 'INSERT MEM ADDRESS FROM CHEAT ENGINE HERE'

class PyGameHelper:
    """
    A class used to help setup the joystick used by the player when running the game.

    Attributes
    ----------
    N/A

    Methods
    -------
    init()
        Sets up the joystick array
    
    getJoystick()
        Gets a list of all joysticks connected and returns that to the user
    """

    def __init__(self):
        """Set up the joystick array."""
        self.joysticks = []

    def getJoystick(self):
        """
        Iterate all total joysticks that are connected to the PC and return to the user a list of them.

        @returns joysticks: a list of all joysticks
        """
        # for all the connected joysticks
        for i in range(0, pygame.joystick.get_count()):
            # create an Joystick object in our list
            self.joysticks.append(pygame.joystick.Joystick(i))
            # initialize them all (-1 means loop forever)
            self.joysticks[-1].init()
            # print a statement telling what the name of the controller is
            print ("Detected joystick "),self.joysticks[-1].get_name(),"'"
        return self.joysticks


class CustomRoboPart:
    """
    Class to get the current custom robo part when plaing the GBC version of Custom Robo.
    
    Requires that the user uses CheatEngine to get the correct starting memory address
    
    Attributes:
    -----------
    pyg: the PyGameHelper object

    Methods
    -------
    getPartFromMemory(address, length)
        Reads the Dolphin process memory to return to the user the current part
    clearMemory(address, length)
        Clears the memory of any persistent data
    """

    pyg = PyGameHelper()

    def getPartFromMemory(address: int, length: int) -> str:
        """
        Read from the Dolphin memory the value at an address. Used to grab the current robo part you have selected.

        @param address: the memory address represented as an integer
        @param length: the number of bytes to read from the address

        @return a string representation of the value from address + length
        """

        return pm.read_bytes(address, length).decode('utf-8', 'ignore').strip('\x00')

    def clearMemory(address: int, length: int):
        """
        After reading a robo part, we need to clear the memory one byte at a time.
        
        The reason for this is that very long names have their tail ends stay in memory
        EX: Right Flank Bomb H --> Gatling Gun will leave the "Bomb H" in memory
        
        @param address: the memory address represented as an integer
        @param length: the number of bytes to read from the address
        """
        for i in range(length):
            pm.write_bytes(address + i, b'\x00', 1)
        time.sleep(0.50)


    if __name__ == '__main__':
        intAdd = int(MEMADD, 16)
        flag = ''
        joystick = pyg.getJoystick()

        with open('allParts.json') as j:
            allParts = json.load(j)
            partTypes = allParts.keys()

        clearMemory(intAdd,24)
        while True:
            for event in pygame.event.get():
                try:
                    if joystick[-1].get_button(SELECT):
                        currPart = getPartFromMemory(intAdd, 24)
                        print(currPart)
                        for k in partTypes:
                            if currPart in allParts.get(k):
                                flag = k
                                print(flag)
                            else:
                                clearMemory(intAdd,24)

                        if flag == 'robo':
                            with open('results/body.txt', 'w') as b:
                                b.write(currPart)
                                print("Body Set")
                        elif flag == 'gun':
                            with open('results/gun.txt', 'w') as g:
                                g.write(currPart)
                                print("Gun Set")
                        elif flag == 'bomb':
                            with open('results/bomb.txt', 'w') as o:
                                o.write(currPart)
                                print("Bomb Set")
                        elif flag == 'pod':
                            with open('results/pod.txt', 'w') as p:
                                p.write(currPart)
                                print("Pod Set")
                        elif flag == 'legs':
                            with open('results/legs.txt', 'w') as l:
                                l.write(currPart)
                                print("Leg Set")
                        flag = ''
                        clearMemory(intAdd,24)
                    elif tuple(joystick[-1].get_hat(DOWNPAD)) == (0,-1):
                        print('Memory cleared')
                        clearMemory(intAdd,24)
                except Exception as e:
                    print(e)
                    print('Something went really wrong if you made it here')
                    clearMemory(intAdd, 24)
            