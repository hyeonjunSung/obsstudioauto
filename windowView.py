import time
import keyboard

def obs64WindowMaximize(dlg) :
    if dlg.is_maximized() == False :
        dlg.maximize()
    else :
        dlg.set_focus()

def changeView(dlg, changeInterval) :
    obs64WindowMaximize(dlg)
    sceneList = dlg.child_window(title="장면 목록:", auto_id="OBSBasic.scenesDock", control_type="Window").ListBox
    #print(sceneList.get_items())
    for scene in sceneList:
        if keyboard.is_pressed("F9"):
            break
        scene.click_input()
        time.sleep(int(changeInterval))

def refreshView(dlg) :
    obs64WindowMaximize(dlg)
    sceneList = dlg.child_window(title="장면 목록:", auto_id="OBSBasic.scenesDock", control_type="Window").ListBox
    sourceList = dlg.child_window(title="소스 목록:", auto_id="OBSBasic.sourcesDock", control_type="Window").ListBox
    #dlg.print_control_identifiers()
    for scene in sceneList :
        if keyboard.is_pressed("F9"):
            break
        scene.click_input()
        
        for source in sourceList :
            if "VLC" in source.texts()[0] :
                if keyboard.is_pressed("F9"):
                    break
                VLC_Source_Title = source.texts()[0]
                source.double_click_input()
                time.sleep(1)

                VLC_Source = dlg["'"+VLC_Source_Title+"'_속성"]
                VLC_Source.set_focus()    
                VLC_Source.child_window(title="확인", control_type="Button").click_input()
