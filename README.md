# My-Dear-Friend-File-Renaming-Tool
This is a v001 version of the my dear friend renaming tool.

INSTRUCTION: 
1. paste the 'saveFileAndAssets' folder to C:\Users\User\OneDrive\Documents\maya\<your maya version>\scripts

2. paste the code below into script editor.

import maya.cmds as cmds
import importlib
from saveFileAndAssets import save_file_and_assets

importlib.reload(save_file_and_assets)
save_file_and_assets.save_UI()

3. run the script or, in the script editor select file>save script to shelf and, create a tool shortcut on your shelf. 
