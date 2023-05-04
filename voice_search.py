from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Define o nome do arquivo de controle que será usado para encerrar o script
control_file = 'D:\projetos\Hand-Signals\stop_voice_search.txt'

# Cria uma instância do driver do navegador com as configurações necessárias
options = webdriver.ChromeOptions()
options.add_argument('--use-fake-ui-for-media-stream')  # Adiciona a opção para usar a UI falsa
options.add_experimental_option('prefs', {'profile.default_content_setting_values.media_stream_mic': 1})  # Permite o acesso ao microfone sem pedir permissão
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Navega até a página do Google
driver.get('https://www.google.com.br')
time.sleep(1.5)

# Início da busca por voz
voice_search_button = driver.find_element(By.XPATH, '//div[@aria-label="Pesquisar por voz"]')
voice_search_button.click()

# Espera até o botão de "Ouvindo" desaparecer
while True:
    try:
        driver.find_element(By.XPATH, '//div[contains(text(), "Ouvindo...")]')
        time.sleep(1)
    except:
        break

# Espera até que a página de resultados seja carregada completamente
while True:
    try:
        driver.find_element(By.XPATH, '//div[@id="search"]')
        break
    except:
        time.sleep(1)

# Loop para manter a página de resultados aberta até receber um comando de outro script para encerrar
while True:
    # Verifica se o arquivo de controle existe
    if os.path.exists(control_file):
        # Remove o arquivo de controle e encerra a execução do script
        driver.quit()
        os.remove(control_file)
    else:
        # Aguarda 60 segundos antes de verificar novamente
        time.sleep(20)
