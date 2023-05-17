import PySimpleGUI as sg
import time

class Display():
    
    def processbar(texto, ms):
        layout = [[sg.Text(texto),
                 sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESSBAR-')]]
        
        window = sg.Window('', layout, no_titlebar=True, finalize=True)
        
        for i in range(100):
            time.sleep(ms/100)
            window['-PROGRESSBAR-'].update_bar(i + 1)
            
        window.close()