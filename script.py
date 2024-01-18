from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuração do WebDriver (escolha o navegador que você deseja usar)
driver = webdriver.Chrome()

# URL do site
url = "https://gshow.globo.com/realities/bbb/"

# Número total de iterações que você deseja fazer
total_iteracoes = 5

# Contador para controlar as iterações
contador_iteracoes = 0

# Loop principal
while contador_iteracoes < total_iteracoes:
    try:
        # Navega até o site
        driver.get(url)

        # Espera até que o elemento seja localizado
        botao = driver.find_element(By.CSS_SELECTOR, '[data-nome="Davi"]')

        # Clique no botão
        botao.click()

        # Adicione pausas conforme necessário
        time.sleep(2)  # Aguarda 5 segundos, ajuste conforme necessário

    except Exception as e:
        print(f"Exceção: {e}")

    finally:
        # Atualiza o contador de iterações
        contador_iteracoes += 1
