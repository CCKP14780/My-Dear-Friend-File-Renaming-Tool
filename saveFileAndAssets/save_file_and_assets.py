import maya.cmds as cmds
from functools import partial

'''
#PASTE THIS CODE TO SCRIPT EDITOR
import maya.cmds as cmds
import importlib
from saveFileAndAssets import save_file_and_assets

importlib.reload(save_file_and_assets)
save_file_and_assets.save_UI()
'''

def get_current_file_name():
    current_file_name = cmds.file(q=True,sn=True,shn=True)
    return current_file_name

def set_current_prefix(version = 1,padding = 3):
    for multiple in range(1,padding):
        
        prefix = '0'*multiple
        current_prefix = f'{prefix}{version}'
                
        if len(current_prefix)==padding+1:
            current_prefix = version
            return current_prefix
        
        elif len(current_prefix)>padding+1:
            cmds.error('Version exceeds padding limits.')

        elif len(current_prefix) is not padding:
            continue

        else:
            break

    return current_prefix

def save_UI():
    if cmds.window('save_UI_window',q=1,ex=1):
        cmds.deleteUI('save_UI_window',window = 1)
    cmds.window('save_UI_window',t='SAVE FILE')

    cmds.columnLayout(adj=1)
    cmds.frameLayout('STATE PREFIX')
    
    cmds.rowLayout(numberOfColumns = 2)
    cmds.text('mainPrefixText',l = 'Main Prefix:NONE')
    cmds.setParent('..')

    cmds.gridLayout(numberOfColumns = 4,numberOfRows = 4,cellWidthHeight=(80, 25))
    cmds.button('ZA_button',l='ZONE A',c=partial(setMainPrefix,'ZA'))
    cmds.button('ZB_button',l='ZONE B',c=partial(setMainPrefix,'ZB'))
    cmds.button('ZC_button',l='ZONE C',c=partial(setMainPrefix,'ZC'))
    cmds.button('HEx_button',l='House Ext',c=partial(setMainPrefix,'HEx'))
    cmds.button('HIn_button',l='House Int',c=partial(setMainPrefix,'HIn'))
    cmds.button('MC_button',l='Main Char',c=partial(setMainPrefix,'MC'))
    cmds.button('SC_button',l='Sub Char',c=partial(setMainPrefix,'SC'))
    cmds.button('PM_button',l='Pao Mu',c=partial(setMainPrefix,'PM'))
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns = 2)
    cmds.text('modelPrefixText',l='Model Type:NONE')
    cmds.setParent('..')

    cmds.gridLayout(numberOfColumns = 4,numberOfRows = 4,cellWidthHeight=(80, 25))
    cmds.button('MainBD_button',l='Main Build',c=partial(setModelPrefix,'MainBD'))
    cmds.button('MarkBD_button',l='Market Build',c=partial(setModelPrefix,'MarkBD'))
    cmds.button('SBD_button',l='Sub Build',c=partial(setModelPrefix,'SBD'))
    cmds.button('Prp_button',l='Props',c=partial(setModelPrefix,'Prp'))
    cmds.button('Layout_button',l='Layout',c=partial(setModelPrefix,'Layout'))
    cmds.button('Mdl_button',l='Modular',c=partial(setModelPrefix,'Mdl'))
    cmds.button('Shot_button',l='Shot',c=partial(setModelPrefix,'Shot'))
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns = 3)
    cmds.text('Building Number: ')
    cmds.intField('buildingVersion_intField',min=0,v=1)
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns = 1)
    cmds.text('')
    cmds.setParent('..')

    cmds.frameLayout('SAVE OPTION')

    cmds.rowLayout(numberOfColumns = 3)
    cmds.text('Version Number: ')
    cmds.intField('version_intField',min=0,v=1)
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns = 3)
    cmds.text('WIP Number:       ')
    cmds.intField('WIP_intField',min=0,v=1)
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns = 1)
    cmds.text('')
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns = 4)
    cmds.text('\t      ')
    cmds.button('RENAME',w = 200,h=50,c=renameFile)
    cmds.setParent('..')

    cmds.window('save_UI_window',e=1,wh=[322,400])
    cmds.showWindow('save_UI_window')

def setMainPrefix(*args):
    cmds.text('mainPrefixText',e=True,l = f'Main Prefix:{args[0]}')

def setModelPrefix(*args):
    cmds.text('modelPrefixText',e=True,l=f'Model Type:{args[0]}')

def renameFile(*args):
    raw_main_prefix = cmds.text('mainPrefixText',q=True,l=1)
    raw_model_prefix = cmds.text('modelPrefixText',q=True,l=1)
    raw_building_version = cmds.intField('buildingVersion_intField',q=1,v=1)
    raw_file_version = cmds.intField('version_intField',q=1,v=1)
    raw_file_WIP = cmds.intField('WIP_intField',q=1,v=1)

    main_prefix = raw_main_prefix.split(':')[1]
    model_prefix = raw_model_prefix.split(':')[1]

    model_version = f'{model_prefix}{set_current_prefix(version = raw_building_version,padding = 3)}'

    file_version = set_current_prefix(version = raw_file_version,padding = 3)
    wip_version = set_current_prefix(version = raw_file_WIP,padding = 3)
    
    new_file_name = f'{main_prefix}_{model_version}_v{file_version}_wip{wip_version}'

    cmds.warning(f'RENAME FILE TO: {new_file_name}')
    cmds.file(rename=new_file_name)