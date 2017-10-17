from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()
#driver.set_window_size(800,300)
USUARIO = input("Digite a Matricula")
SENHA = input("Digite a senha")
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

#dados.find("div",{"class":"t1"}) titulos pendentes
#dados.find_all("a",{"class":"txt_azul"}) livros
contBooks=1
count=3
aux=0
for conteudo in livros:
  print("\n{}: {}".format(contBooks,conteudo.text.replace("\t","")))
  print("Data de Devolucao {}".format(datas[count].get_text()))
  print("Valor da multa:"+str(multas[aux].get_text()))
  count=count+3
  aux=aux+1
  contBooks=contBooks+1
  #print(soup.find("td",{"class":"txt_cinza_10"}))
driver.quit()
