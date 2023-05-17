import PySimpleGUI as sg
import time


class Display():
    
    def processbar(texto):
        layout = [[sg.Text(texto, key='-TEXT-')],
                [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='-PROGRESSBAR-')]]
        
        window = sg.Window('', layout, no_titlebar=True, finalize=True)
        
        for i in range(1000):
            time.sleep(0.005/1000)
            window['-PROGRESSBAR-'].update_bar(i + 1)
            
        window.close()