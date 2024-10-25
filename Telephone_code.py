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