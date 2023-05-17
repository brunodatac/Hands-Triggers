import PySimpleGUI as sg
import time

class Display():
    
    def processbar(texto, ms):
        layout = [[sg.Text(texto),
                 sg.ProgressBar(1000, orientation='h', size=(20, 20), key='-PROGRESSBAR-')]]
        
        window = sg.Window('', layout, no_titlebar=True, finalize=True)
        
        for i in range(1000):
            time.sleep(ms/1000)
            window['-PROGRESSBAR-'].update_bar(i + 1)
            
        window.close()

























