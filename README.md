## Proyecto del Sprint 8: Ejercicio

### Tecnologías a usar en este proyecto
- Lenguaje de Programamcion "Python 3.12"
- Consola Pycharm Community Edition 2024.2.1

## Configuración
> Trabajarás con Git y GitHub en este proyecto. Sigue los pasos a continuación para configurar tu proyecto.

>  Paso 1: conecta tu GitHub
El primer paso es enlazar tu cuenta de GitHub a TripleTen. Para ello, haz clic en el botón "Enlazar la cuenta de GitHub" en el widget en la parte superior de esta página. Esto te llevará a una nueva pestaña del navegador donde se te pedirá que confirmes que deseas enlazar tu cuenta de GitHub. Si aún no has iniciado sesión en GitHub, se te pedirá que introduzcas tu nombre de usuario y contraseña. Al confirmarlo, tu perfil de TripleTen se conectará a tu perfil de GitHub a través de la API segura de GitHub. Esto te permitirá enviar tus proyectos automáticamente con tan solo hacer clic en un botón, directamente dentro de la plataforma de TripleTen.

> Paso 2. Clona el repositorio en tu computadora
Una vez que hayas vinculado tu cuenta de TripleTen con GitHub, se creará un repositorio automáticamente. El nombre del repositorio será qa-project-Urban-Grocers-app-es.

> Ve a GitHub y clona el nuevo repositorio en tu computadora local, siguiendo estos pasos:

> Abre la línea de comandos en tu computadora (Git Bash).
> Si aún no lo has hecho, crea un directorio para almacenar todos tus proyectos. Por ejemplo:
```sh
cd ~               # asegúrate de estar en tu directorio de inicio
mkdir projects     # crea una carpeta llamada projects
cd projects        # cambia el directorio a la nueva carpeta de proyectos
```

> Clona el repositorio con SSH.
```sh
git clone git@github.com:sanchezajose/qa-project-Urban-Routes-es.git
```
> Paso 3. Trabaja con el proyecto de forma local
Ahora tienes una copia local del proyecto y puedes abrir la carpeta del proyecto en tu computadora.
```sh
💡 Puedes utilizar PyCharm para trabajar en el proyecto localmente. Simplemente abre PyCharm y selecciona Archivo → Abrir y luego selecciona la carpeta qa-project-Urban-Routes-es que clonaste en tu computadora.
```

#### Cuando puedas comenzar a trabajar, presiona el botón "Iniciar el servidor" para obtener la URL de tu servidor.
```sh
Necesitarás una URL de servidor para que tu código pueda acceder al servidor. Continúa y obtén una URL utilizando el botón a continuación.

Servidor

Iniciar
En data.py, reemplaza la URL base con la URL de Urban Routes generada anteriormente.
```

## Dentro de Pycharm Community Edittion 2024 2.1
### Pasos previos :
- Instalar la libreria "Pytest":
    - A través de la interfaz de PyCharm en "Python Packages":
    - En tu proyecto de PyCharm, dirígete al panel inferior y selecciona la pestaña "Python Packages".
    - En el campo de búsqueda, introduce "Pytest".
    - Localiza y selecciona el paquete "Pytest" de la lista y haz clic en el botón "Install".
    

- Instalar la libreria "Selenium":
    - A través de la interfaz de PyCharm en "Python Packages":
    - En tu proyecto de PyCharm, dirígete al panel inferior y selecciona la pestaña "Python Packages".
    - En el campo de búsqueda, introduce "Selenium".
    - Localiza y selecciona el paquete "Pytest" de la lista y haz clic en el botón "Install".
    

- Instalar la libreria "Self":
    - A través de la interfaz de PyCharm en "Python Packages":
    - En tu proyecto de PyCharm, dirígete al panel inferior y selecciona la pestaña "Python Packages".
    - En el campo de búsqueda, introduce "Self".
    - Localiza y selecciona el paquete "Pytest" de la lista y haz clic en el botón "Install".


## Ejercicio:
```sh
 1_ Vas a escribir varias pruebas para comprobar la funcionalidad de Urban Routes. Escribe tus pruebas en el archivo main.py
 ```
 ```sh
2_ Define los localizadores y métodos necesarios en la clase UrbanRoutesPage y las pruebas en la clase TestUrbanRoutes.
```
```sh
3_ Escribe pruebas automatizadas que cubran el proceso completo de pedir un taxi. Las pruebas deben cubrir estas acciones:
   -Configurar la dirección (esta parte se ha escrito para ti como ejemplo).
   -Seleccionar la tarifa Comfort.
   -Rellenar el número de teléfono.
   -Agregar una tarjeta de crédito. (Consejo: el botón 'link' (enlace) no se activa hasta que el campo CVV de la tarjeta en el modal 'Agregar una tarjeta', id="code" class="card-input", pierde el enfoque. Para cambiar el enfoque, puedes simular que el usuario o usuaria presiona TAB o hace clic en otro lugar de la pantalla).
```
```sh
4_ Escribir un mensaje para el controlador.
```
```sh
5_ Pedir una manta y pañuelos.
```
> El repositorio tiene preparada la función retrieve_phone_code() que intercepta el código de confirmación requerido para agregar una tarjeta.
```sh
6_ Pedir helados.
```
```sh
7_ Escribir un mensaje para el controlador.
```
```sh
8_ Pedir una manta y pañuelos.
```
```sh
9_ Pedir 2 helados.
```
> Aparece el modal para buscar un taxi.
Esperar a que aparezca la información del conductor en el modal (opcional). Además de los pasos anteriores, hay un paso opcional que puedes comprobar; este es un poco más complicado que los demás, pero es una buena práctica, ya que es probable que en tu trayectoria profesional encuentres tareas más difíciles.
### Ejecución de pruebas
Tienes dos opciones para ejecutar tus pruebas: directamente desde la consola de PyCharm o utilizando su interfaz gráfica.

1️⃣ Desde la terminal de PyCharm

Dirígete a la pestaña "Terminal" en la parte inferior de PyCharm. Por defecto, esta terminal se ubica en el directorio de tu proyecto. 

Para ejecutar todas las pruebas de tu proyecto, simplemente escribe:
```sh
pytest
```
Luego ejecuta las pruebas desde el archivo main.py:
```sh
pytest main.py
```
### Ejecuta todas las pruebas del proyecto:

- En el menú "Run", selecciona "Edit Configurations" (Editar configuraciones).
- Haz clic en "+ (Add New Configuration)" (Agregar nueva configuración). Se abrirá una ventana nueva.
- Selecciona "Python tests → pytest" (Pruebas de Python → Pytest) en la lista de configuraciones.
Aparecerá una ventana nueva. 
- Selecciona "Custom" (Personalizar) en la línea "Target" (Objetivo).
- Haz clic en "Apply" (Aplicar) y luego en "OK" (Aceptar).
- Ahora haz clic en el ícono de la flecha verde para iniciar la configuración y observa los resultados.

### Ejecuta el Commit y el push desde Pycharm:

- En la barra "Archivos de arbol del proyecto", selecciona el boton "Commit", se despliega una ventana con una barra de seleccion con todos los archivos del proyecto.
- Haz clic en la casilla para seleccionar todos los archivos.
- Agrega un comentario "Entrega proyecto 7".
- Haz clic en el boton inferor izquierdo "Commit and Push"
- Se abrira una panttalla emergente y haz clic en el boton "Push".
- Ahora los archivos se han actualizado en el GitHuB ahora el equipo puedo ver este proyecto.


### Archivos dentro del proyecto (qa-project-Urban-Grocers-app-es)
- Main.py 
- Data.py
- Metodos.py
- Telephone_code.py
- .gitignore
- ReadMe.md


### Contenido del archivo Main.py
Este archivo contiene los Test Cases de la pagina Urban Routes
```sh
import data
import time
from selenium import webdriver
from Metodos import UrbanRoutesPage
from Telephone_code import retrieve_phone_code
from Telephone_code import wait_for_load_page
from Telephone_code import wait_for_driver_arrival_message


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

    def setup_method(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)
        wait_for_load_page(self.driver, UrbanRoutesPage.from_field)

    # 1 Coloca la ruta del taxi
    def test_set_route(self):
        self.setup_method()
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to
        time.sleep(7)

    # 2 Selecciona la opción Comfort
    def test_request_taxi_comfort(self):
        self.test_set_route()
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_button()
        taxi_type = self.routes_page.get_comfort_taxi()
        assert 'Comfort' == taxi_type
        time.sleep(7)

    # 3 Agrega el número telefonico
    def test_add_phone_number(self):
        self.test_request_taxi_comfort()
        self.routes_page.click_phone_number_button()
        phone_number = data.phone_number
        self.routes_page.set_phone_number(phone_number)
        self.routes_page.click_phone_number_next_button()
        confirmation_code = retrieve_phone_code(self.driver)
        self.routes_page.set_code_sms(confirmation_code)
        self.routes_page.click_code_confirmation_button()
        phone_number_added = self.routes_page.get_phone_number()
        assert phone_number_added == phone_number
        time.sleep(7)

    # 4 Agrega una tarjeta al método de pago
    def test_add_card(self):
        self.test_add_phone_number()
        self.routes_page.click_payment_method_button()
        self.routes_page.click_add_card_number_button()
        card_number, card_code = data.card_number, data.card_code
        self.routes_page.set_card(card_number, card_code)
        element = self.routes_page.card_1_added
        assert element is not None
        card_checkbox_checked = self.routes_page.is_card_1_checked()
        assert card_checkbox_checked
        self.routes_page.click_close_payment_method_window()
        time.sleep(7)

    # 5 Envía un mensaje al conductor
    def test_send_driver_message(self):
        self.test_add_card()
        msg = data.message_for_driver
        self.routes_page.set_driver_msg(msg)
        driver_msg = self.routes_page.get_driver_msg()
        assert driver_msg == msg
        time.sleep(7)

    # 6 Agrega pañuelos y mantas
    def test_order_handkerchief_blanket(self):
        self.test_send_driver_message()
        self.routes_page.click_handkerchief_blanket()
        switch_checked = self.routes_page.is_switch_checked()
        assert switch_checked, "El checkbox de la clase 'switch-input' no está encendido"
        time.sleep(7)

    # 7 Agrega la cantidad de helado
    def test_order_icecream(self):
        self.test_send_driver_message()
        icecream_amount = '2'
        self.routes_page.add_icecream_amount(icecream_amount)
        icecream_value = self.routes_page.get_icecream_amount()
        assert icecream_value == icecream_amount
        time.sleep(7)

    # 8 Pedir el taxi ya con todos los items solicitados
    def test_order_taxi(self):
        self.test_order_icecream()
        self.routes_page.click_order_taxi_button()
        wait_for_driver_arrival_message(self.driver, UrbanRoutesPage.order_header_title)
        arrival_message = self.routes_page.get_driver_arrival_message()
        assert "El conductor llegará" in arrival_message
        time.sleep(7)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
```
### Contenido del archivo Data.py
Contiene los datos necesarios parea ejecutarr el proyeecto
```sh
urban_routes_url = 'https://cnt-1df75b2b-901a-4afb-b565-d5780cd56308.containerhub.tripleten-services.com?lng=es'
address_from = 'East 2nd Street, 601'
address_to = '1300 1st St'
phone_number = '+1 123 123 12 12'
card_number, card_code = '1234 5678 9100', '112'
message_for_driver = 'Traiga un Aperitivo'
```
### Contenido del Archivo Metodos
Coontiene los Localizadores y las fuunciones para ejecutar las pruebas de los elementos
```sh
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



# CORRECCION: Creación del archivo urban_routes_page donde están las funciones de la página
class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    ask_taxi_button = (By.XPATH, ".//div[@class='workflow']//button[text()='Pedir un taxi']")
    comfort_button = (By.XPATH, ".//div[@class='tcard-icon']//img[@alt='Comfort']")
    phone_number_button = (By.XPATH, ".//div[@class='np-text']")
    phone_number_field = (By.XPATH, ".//input[@id='phone']")
    phone_number_next_button = (By.XPATH, ".//div[@class='modal']//button[text()='Siguiente']")
    code_sms_field = (By.XPATH, ".//input[@id='code']")
    confirm_code_button = (By.XPATH, ".//div[@class='modal']//button[text()='Confirmar']")
    payment_method_button = (By.CSS_SELECTOR, '.pp-button')
    add_card_number_button = (By.CSS_SELECTOR, '.disabled.pp-row')
    card_number_field = (By.XPATH, ".//input[@id='number']")
    card_code_field = (By.XPATH, ".//div[@class='card-code-input']/input[@id='code']")
    add_card_confirmation_button = (By.XPATH, ".//div[@class='pp-buttons']//button[text()='Agregar']")
    card_1_added = (By.ID, 'card-1')
    close_payment_method_window = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active .close-button.section-close')
    driver_msg_button = (By.ID, 'comment')
    handkerchief_blanket = (By.CSS_SELECTOR, '.reqs-body .r-type-switch:nth-of-type(1) .slider')
    switch_checkbox = (By.CSS_SELECTOR, 'input.switch-input')
    icecream_value = (By.CSS_SELECTOR, '.r-group-items .r-type-counter:nth-of-type(1) .counter-value')
    order_taxi_button = (By.CSS_SELECTOR, '.smart-button-main')
    order_header_title = (By.CSS_SELECTOR, '.order-header-title')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_request_taxi_button(self):
       return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.ask_taxi_button)).click()

    def click_comfort_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.comfort_button)).click()

    def get_comfort_taxi(self):
        return self.driver.find_element(*self.comfort_button).get_property('alt')

    def click_phone_number_button(self):
       return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.phone_number_button)).click()

    def set_phone_number(self, phone_number):
        phone_number_field = WebDriverWait(self.driver, 15).until(
           EC.visibility_of_element_located(self.phone_number_field))
        phone_number_field.send_keys(phone_number)

    def click_phone_number_next_button(self):
       return self.driver.find_element(*self.phone_number_next_button).click()

    def set_code_sms(self, code_sms):
       return self.driver.find_element(*self.code_sms_field).send_keys(code_sms)

    def click_code_confirmation_button(self):
       return self.driver.find_element(*self.confirm_code_button).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_button).text

    def click_payment_method_button(self):
       return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.payment_method_button)).click()

    def click_add_card_number_button(self):
       return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.add_card_number_button)).click()

    def set_card_number(self, card_number):
        card_number_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.card_number_field))
        card_number_field.send_keys(card_number)

    def set_card_code(self, card_code):
        card_code_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.card_code_field))
        card_code_field.send_keys(card_code)

    def click_add_card_confirmation_button(self):
       return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.add_card_confirmation_button)).click()

    def send_tab(self):
      return  self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)

    def set_card(self, card_number, card_code):
        self.set_card_number(card_number)
        self.set_card_code(card_code)
        self.send_tab()
        self.click_add_card_confirmation_button()

    def get_card_id(self):
        return self.driver.find_element(*self.card_1_added)

    def is_card_1_checked(self) -> object:
        card_checkbox = self.driver.find_element(*self.card_1_added)
        return card_checkbox.is_selected()

    def click_close_payment_method_window(self):
        self.driver.find_element(*self.close_payment_method_window).click()

    def set_driver_msg(self, msg):
        driver_msg_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.driver_msg_button))
        driver_msg_field.send_keys(msg)
        self.send_tab()

    def get_driver_msg(self):
        return self.driver.find_element(*self.driver_msg_button).get_property('value')

    def click_handkerchief_blanket(self):
       return self.driver.find_element(*self.handkerchief_blanket).click()

    def is_switch_checked(self):
        checkbox = self.driver.find_element(*self.switch_checkbox)
        return checkbox.is_selected()

    def add_icecream_amount(self, new_value):
        counter_element = self.driver.find_element(*self.icecream_value)
        self.driver.execute_script("arguments[0].textContent = arguments[1];", counter_element, new_value)

    def get_icecream_amount(self):
        return self.driver.find_element(*self.icecream_value).text

    def click_order_taxi_button(self):
       return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.order_taxi_button)).click()

    def get_driver_arrival_message(self):
        return self.driver.find_element(*self.order_header_title).text
```
### Contenido del archivo Telephone_code.py
Contiene el codigo para extraer un ID o Codigo numerico para el campo "Numero de Telefono"
```sh
import json
import time
from selenium.common import WebDriverException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
    if not code:
        raise Exception("No se encontró el código de confirmación del teléfono.\n"
                        "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
    return code

def wait_for_load_page(driver, from_field):
    WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(from_field))


def wait_for_driver_arrival_message(driver, order_header_title):
    WebDriverWait(driver, 60).until(
        expected_conditions.text_to_be_present_in_element(order_header_title, "El conductor llegará"))
```
### Contenido del Archivo ".GitIgnore"
ontiene todas los archivos no necesarios o a ignorar dentro del proyecto
```sh
.pytest/
venv/
.idea/
.pytest_cache/
__pycache__/
```
### Contenido del Archivo "ReadMe.md"
Finalmente este archivo donde encontraras la informacion detallada de este proyecto
```sh
REadMe.mD
```
José Sánchez, 14Avo grupo,sprint 8
PROYECTO SPRINT 8

**Espero con gusto tu Feedback Te leo**










