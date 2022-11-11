from pywinauto.application import Application
import pywinauto
import psutil

obsPID = 0

for proc in psutil.process_iter():
    if (proc.name() == "obs64.exe"):
        print(str(proc.pid) + "\t" +proc.name())
        obsPID = proc.pid
