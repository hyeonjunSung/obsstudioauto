import tkinter as tk
import tkinter.font as font

window = tk.Tk()
window.title('OBS Studio 자동제어 프로그램')        # 타이틀
window.geometry('600x900')                         # Window 크기

# Sub Title
subtitleFrame = tk.Frame(window, width=600, height=30)
subtitleFrame.pack(fill='both')
subtitleLabel = tk.Label(subtitleFrame, text='고성 OBS Studio 제어'
                                , font=('Consolas bold', 20))
subtitleLabel.pack(pady=20)                               # 가운데 정렬

# Process Finder
processRootFrame = tk.Frame(window, width=600, height=30)
processRootFrame.pack(fill='both')

processChildTitleFrame = tk.Frame(processRootFrame)
processChildTitleFrame.pack(side='left', padx=5, pady=10)
processLabel = tk.Label(processChildTitleFrame, text='Process 찾기'
                                , font=('Consolas bold', 15))
processLabel.pack(side='left', padx=10, pady=20)


# Refresh
refreshFrame = tk.Frame(window, width=600, height=30, relief='solid', bd=2)
refreshFrame.pack(fill='both') 
refreshLabel = tk.Label(refreshFrame, text='새로고침 주기'
                                , font=('Consolas bold', 15))
refreshLabel.pack(side='left', padx=10, pady=20)
window.mainloop()