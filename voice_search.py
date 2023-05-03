from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Cria uma instância do driver do navegador com as configurações necessárias
options = webdriver.ChromeOptions()
options.add_argument('--use-fake-ui-for-media-stream')  # Adiciona a opção para usar a UI falsa
options.add_experimental_option('prefs', {'profile.default_content_setting_values.media_stream_mic': 1})  # Permite o acesso ao microfone sem pedir permissão
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Navega até a página do Google
driver.get('https://www.google.com.br')

# Início da busca por voz
voice_search_button = driver.find_element(By.XPATH, '//div[@aria-label="Pesquisar por voz"]')
voice_search_button.click()
time.sleep(7)

# Aguarda uma entrada de teclado antes de encerrar o script
try:
    input('Pressione qualquer tecla para encerrar o script...')
except KeyboardInterrupt:
    pass

# Encerra a sessão do driver e fecha a janela
driver.close()
