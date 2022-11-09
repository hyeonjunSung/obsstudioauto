import PySimpleGUI as sg
import os.path

sg.theme('DarkAmber')

# Font list check
#print(sg.Text.fonts_installed_list())

refreshList = [5, 10, 20, 30, 60]

# Define the layout
def blank_frame():
    return sg.Frame("", [[]], pad=(5, 3), expand_x=True, expand_y=True, background_color='#404040', border_width=0)

frame0_top = [sg.T(" ", font="맑은고딕 5")]
frame0_1 = [sg.T(" OBS Studio PID 입력 : ", font='맑은고딕 13'), sg.Input(), sg.Button("적용", font="맑은고딕")]
frame0_2 = [sg.Button("PID 찾기"), sg.T("연동 완료", key='-isConnet-', size=(10,1))]
frame0_bottom = [sg.T(" ", font="맑은고딕 5")]

frame1_top = [sg.T(" ", font="맑은고딕 5")]
frame1_1 = [sg.T(" 화면 새로고침 주기 입력 : ", font='맑은고딕 13'), sg.Combo(values=(30, 60, 120, 180, 240, 300, 360), key='-RefreshViewList-', enable_events=True, size=(20, 1)),sg.T('초', font="맑은고딕"), sg.B('적용', font="맑은고딕")]
frame1_bottom = [sg.T(" ", font="맑은고딕 5")]

frame2_top = [sg.T(" ", font="맑은고딕 5")]
frame2_1 = [sg.T(" 화면전환 주기 입력 : ", font='맑은고딕 13'), sg.Combo(values=(5, 10, 20, 30, 60), key='-ChangeViewList-', enable_events=True, size=(20, 1)), sg.T('초', font="맑은고딕"),sg.B('적용', font="맑은고딕")]
frame2_bottom = [sg.T(" ", font="맑은고딕 5")]



row5 = [sg.Button('실행', font="맑은고딕"), sg.Button('종료', font="맑은고딕")]



layout_frame0 = [
    [blank_frame()]
]

layouts = [
    [sg.Frame('OBS Studio Process 찾기', [frame0_top, frame0_1, frame0_2, frame0_bottom], font='HY견고딕 15 bold', size=(580,120))],
    [sg.Frame('화면 새로고침 주기 변경', layout=[frame1_top, frame1_1, frame1_bottom], font='HY견고딕 15 bold', size=(580,100))],
    [sg.Frame('화면전환 주기 변경', [frame2_top, frame2_1, frame2_bottom], font='HY견고딕 15 bold', size=(580,100))],
    [sg.Frame('에러 로그', [[blank_frame()]], font='HY견고딕 15 bold', size=(580,300))],
    [sg.Frame('현재 설정', [[blank_frame()]], font='HY견고딕 15 bold', size=(580,100))],
    row5
]

# Create the window
window = sg.Window('OBS Studio Auto Control @Innonet', layouts, grab_anywhere=True, size=(600, 800), margins=(2,2))





# Event Loop
while True:
    event, values = window.Read()

    if event in (sg.WIN_CLOSED, '종료'):
        break

window.close()