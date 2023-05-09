from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class Voice():
    
    def __init__(self):
        # Cria uma instância do driver do navegador com as configurações necessárias
        options = webdriver.ChromeOptions()
        options.add_argument('--use-fake-ui-for-media-stream')  # Adiciona a opção para usar a UI falsa
        options.add_experimental_option('prefs', {'profile.default_content_setting_values.media_stream_mic': 1})  # Permite o acesso ao microfone sem pedir permissão
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

        # Navega até a página do Google
        self.driver.get('https://www.google.com.br')
        time.sleep(1.5)


    def abrir(self):
        # Início da busca por voz
        voice_search_button = self.driver.find_element(By.XPATH, '//div[@aria-label="Pesquisar por voz"]')
        voice_search_button.click()

        # Espera até o botão de "Ouvindo" desaparecer
        while True:
            try:
                self.driver.find_element(By.XPATH, '//div[contains(text(), "Ouvindo...")]')
                time.sleep(1)
            except:
                break

        # Espera até que a página de resultados seja carregada completamente
        while True:
            try:
                self.driver.find_element(By.XPATH, '//div[@id="search"]')
                break
            except:
                time.sleep(1)


    # Loop para manter a página de resultados aberta até receber um comando de outro script para encerrar
    def fechar(self, key):
        if key == 'y':
            # Remove o arquivo de controle e encerra a execução do script
            self.driver.quit()