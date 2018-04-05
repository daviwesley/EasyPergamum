import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def renewAllBooks(arg):
    tam = len(arg)
    btn = arg
    for i in range(0,tam):
        btn[i].click()
        driver.back()
        btn = driver.find_elements_by_class_name("btn_renovar")
        time.sleep(4)

chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=800,300")

driver = webdriver.Chrome(executable_path="./chromedriver")

USUARIO = str(sys.argv[1])
SENHA = str(sys.argv[2])
driver.get("https://pergamum.ufc.br/pergamum/biblioteca_s/php/login_usu.php")

usuario = driver.find_element_by_id("id_login")
senha = driver.find_element_by_id("id_senhaLogin")
acessar = driver.find_element_by_id("button")
usuario.send_keys(USUARIO)
senha.send_keys(SENHA)
acessar.click()

soup = BeautifulSoup(driver.page_source,"html.parser")
print(soup.find(id="nome").get_text())
livros = soup.find_all("a",{"class":"txt_azul"})
datas = soup.find_all('td',class_='txt_cinza_10')
multas = soup.find_all('td',class_='txt_magenta')

botao = driver.find_elements_by_class_name("btn_renovar")
#dados.find("div",{"class":"t1"}) titulos pendentes
#dados.find_all("a",{"class":"txt_azul"}) livros
contBooks=1
count=3
aux=0
for conteudo in livros:
  print(conteudo.text.replace("\t", "",))
  print("Data de Devolucao:"+" ".join(datas[count].get_text().split()))
  print("Valor da multa: "+" ".join(multas[aux].get_text().split()))
  count= count+3
  aux= aux+1
  contBooks= contBooks+1


renewAllBooks(botao)
driver.quit()
