# Custom Robo Gamecube Part Picker

The purpose of this repo is to allow users to extract a player's current robo setup to display in recordings while the game is running using Python, PyMem, PyGame, and CheatEngine. 

A jypyter notebook is included for additonal experimentation/figuring out which button SELECT and D-PAD Down refer to

## Usage

### Joystick Config
1. Open *Custom Robo Experimentation Ground.ipynb* (requires jupyter)
2. Run the following two cells
![Joystick Config](/img/readme_screenshots/joystickConfig.png)
3. What we're looking for here is what is defined as SELECT and D-PAD DOWN<br>
For SELECT, this is the type of message that the event will show:<br>
```<Event(1540-JoyButtonUp {'joy': 0, 'instance_id': 0, 'button': 6})>```<br><br>
For D-PAD DOWN, this is the type of message that the event will show:<br>
```<Event(1538-JoyHatMotion {'joy': 0, 'instance_id': 0, 'hat': 0, 'value': (0, -1)})>```

### Memory Searching
1. First open up CheatEngine and open the Dolphin process
![Process Picker](/img/readme_screenshots/cheatEngineProcessPicker.png)
2. Input a robo name as your First Scan (make sure the Value Type is set to String)
![First Scan](/img/readme_screenshots/cheatEngineFirstScan.png)
3. Then pick another part as your Next Scan to narrow down the results
![Next Scan](/img/readme_screenshots/cheatEngineNextScan.png)
4. Pick any of the given addresses (I usually pick the first) and copy/paste it into the MEMADD line in *customRoboScript.py*<br>
(I would also hit Ctrl + B on the memory address to bring up the memory  viewer)
```python
9 | SELECT = 0  # INSERT BUTTON NUMBER FOR SELECT 
10| DOWNPAD = 0 # INSERT BUTTON FOR DPAD DOWN 
11| MEMADD = '' # INSERT MEM ADDRESS FROM CHEAT ENGINE HERE 
```
![Mem View](/img/readme_screenshots/cheatEngineMemView.png)

5. At this point you can start the script by either hitting the run button on your IDE or by running
```
python .\custromRoboScript.py
```
6. As you navigate the menu, verify on the memory viewer that the full name of the part is there and no extra data is there in the first three rows
![New Part](/img/readme_screenshots/cheatEngineNewPart.png)
7. Once you have a part, hit SELECT on your gamepad to lock in the part and update the results
![Old Part](/img/readme_screenshots/oldPart.png)<br>
![New Part](/img/readme_screenshots/newPart.png)
8. If there is data left over as seen below, hit D-PAD Down to clear the memory manually<br>
*This happens because the register gets updated each time you navigate the menus, including opponent configurations*
![Messy Memory](/img/readme_screenshots/messyMemory.png)<br>
![Clean Memory](/img/readme_screenshots/cleanMemory.png)

## Possible Enchancement Ideas
- See if there is a way to remove CheatEngine from the equation
    - If so, then find a way to make sure that no data persists as you navigate the menu
- There has to be a place somewhere where the setup is stored rather than that one random register, so I claim there has to be a way to disassemble the game and just pull that information
- Other ways of saving out the configuration rather than using SELECT and D-PAD DOWN

## References
[Cheat Engine](https://www.cheatengine.org/)<br>
[Python](https://www.python.org/)<br>
[PyMem](https://github.com/srounet/Pymem)<br>
[PyGame Joystick](https://www.pygame.org/docs/ref/joystick.html)