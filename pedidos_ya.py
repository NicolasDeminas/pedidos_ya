from selenium import webdriver
import paths
from data import username, password
from time import sleep


class PedidosOnLine:
    def Inicio(self):
        self.driver = webdriver.Chrome(paths.path)
        self.driver.implicitly_wait(20)
        self.driver.get("https://portal.pedidosya.com/")

    def login(self, username, password):
        self.driver.find_element_by_id("email").send_keys(username)
        self.driver.find_element_by_id("passwordLogin").send_keys(password)
        self.driver.find_element_by_id("loginButton").click()

    def seleccionarSemanaActual(self):
        self.driver.find_element_by_xpath(paths.menuPedidos).click()                                    
        self.driver.find_element_by_xpath(paths.menuDesplegable).click()
        self.driver.find_element_by_xpath(paths.semanaActual).click()
        
    def leerPedidos(self):
        sleep(15)
        cantidadPedidos = self.driver.find_element_by_xpath("/html/body/main/div[5]/section/div/div/div/div/ul/li[2]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/h1")
        cant = int(cantidadPedidos.text)
        with open("pedidosya.csv", "w") as ped:
            for e in range(1,cant, 1):
                for i in range(1, 6, 1):
                    try:
                        pedido = self.driver.find_element_by_xpath("/html/body/main/div[5]/section/div/div/div/div/ul/li[2]/div/div/div[1]/div[4]/ul[2]/li["+str(e)+"]/div[1]/div["+str(i)+"]")
                        if i == 1:
                            referencia = pedido.text
                        elif i == 2:
                            fecha = pedido.text
                        elif i == 3:
                            local = pedido.text
                        elif i == 4:
                            formaPago = pedido.text
                        elif i == 5:
                            importe = pedido.text
                    except:
                        continue
                    
                print(referencia + ";"+fecha+";" + local + ";" + formaPago + ";"+ importe, file=ped)
                if e % 20 == 0:
                    self.driver.execute_script("window.scrollBy(0,1000);")
    def prueba(self):
        sleep(15)
        cantidadPedidos = self.driver.find_element_by_xpath("/html/body/main/div[5]/section/div/div/div/div/ul/li[2]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/h1")
        print(cantidadPedidos.text)
        print(type(cantidadPedidos.text))

    def cerrar(self):
        self.driver.close()
                    
    def __init__(self, username, password):
        self.Inicio()
        self.login(username, password)
        self.seleccionarSemanaActual()
        self.leerPedidos()
        #self.prueba()
        self.cerrar()


if __name__=="__main__":
    pedidosOnLine = PedidosOnLine(username, password)

