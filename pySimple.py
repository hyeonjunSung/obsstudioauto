import PySimpleGUI as sg
import os.path
import psutil


sg.theme('DarkAmber')

# Font list check
#print(sg.Text.fonts_installed_list())

refreshList = [5, 10, 20, 30, 60]

# Define the layout
def blank_frame():
    return sg.Frame("", [[]], pad=(5, 3), expand_x=True, expand_y=True, background_color='#404040', border_width=0)
def padding_frame():
    return [sg.T(" ", font="맑은고딕 5")]

# OBS Studio Process 찾기 Frame
frame0_1 = [sg.T(" OBS Studio PID 입력 :", font='맑은고딕 13'), sg.Input(size=(40,1), key='-inputPID-'), sg.Button("적용", font="맑은고딕", size=(9,1))]
frame0_2 = [sg.Push(),sg.T("연동 완료", key='-isConnet-', size=(10,1)), sg.Button("PID 찾기", font="맑은고딕", key='-findPIDbtn-',size=(9,1), pad=(10,10))]

# 화면 새로고침 주기 변경 Frame
frame1_1 = [sg.T(" 화면 새로고침 주기 입력 : ", font='맑은고딕 13'), sg.Combo(values=(30, 60, 120, 180, 240, 300, 360), key='-RefreshViewList-', enable_events=True, size=(28, 1)),sg.T('초', font="맑은고딕"), sg.B('적용', font="맑은고딕", size=(9,1))]

# 화면전환 주기 변경 Frame
frame2_1 = [sg.T(" 화면전환 주기 입력 : ", font='맑은고딕 13'), sg.Combo(values=(5, 10, 20, 30, 60), key='-ChangeViewList-', enable_events=True, size=(35, 1), pad=(0,0)), sg.T('초', font="맑은고딕"),sg.B('적용', font="맑은고딕", size=(9,1))]

# 에러 로그 Frame

# 현재 설정 Frame
frame4_1 = [sg.T("")]
# 하단 버튼
row5 = [sg.Push(), sg.Button('실행', font="맑은고딕", size=(9,2)), sg.Button('종료', font="맑은고딕", size=(9,2)), sg.T("")]



layout_frame0 = [
    [blank_frame()]
]

layouts = [
    [sg.Push(), sg.Frame('OBS Studio Process 찾기', [padding_frame(), frame0_1, frame0_2, padding_frame()], font='HY견고딕 15 bold', size=(580,120))],
    [sg.Push(),sg.Frame('화면 새로고침 주기 변경', layout=[padding_frame(), frame1_1, padding_frame()], font='HY견고딕 15 bold', size=(580,100))],
    [sg.Push(),sg.Frame('화면전환 주기 변경', [padding_frame(), frame2_1, padding_frame()], font='HY견고딕 15 bold', size=(580,100))],
    [sg.Push(),sg.Frame('에러 로그', [[blank_frame()]], font='HY견고딕 15 bold', size=(580,300))],
    [sg.Push(),sg.Frame('현재 설정', [[blank_frame()]], font='HY견고딕 15 bold', size=(580,100))],
    row5
]

# Create the window
window = sg.Window('OBS Studio Auto Control @Innonet', layouts, grab_anywhere=True, size=(600, 800), margins=(2,2))

obsPID = 0





# Event Loop
while True:
    event, values = window.Read()

    if event in (sg.WIN_CLOSED, '종료'):
        break
    
    if event == "-findPIDbtn-":
        for proc in psutil.process_iter():
            if (proc.name() == "obs64.exe"):
                print(str(proc.pid) + "\t" +proc.name())
                values["-inputPID-"] = proc.pid
                window["-inputPID-"].update(values["-inputPID-"])
window.close()