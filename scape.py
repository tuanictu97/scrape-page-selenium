import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from paddleocr import PaddleOCR


url_register = 'https://timhieuphapluatmoitruongmang.hanoi.gov.vn/binh-chon-video/dang-ky'
url_buff_like = 'https://timhieuphapluatmoitruongmang.hanoi.gov.vn/binh-chon-video/video/quy-tac-ung-xu-tren-mang-xa' \
                '-hoi-danh-cho-hoc-sinh-51.html '


class User:
    def __init__(self, name, date, email, phone, password):
        self.name = name
        self.date = date
        self.email = email
        self.phone = phone
        self.password = password


def register(user: User) -> bool:
    options = Options()
    options.add_argument('--headless')
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(chrome_options=options)
    try:
        driver.get(url_register)

        name_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=\"name\"]"))
        )
        if name_element is None:
            raise Exception('Can not find element name.')
        name_element.send_keys(user.name)

        birth_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=\"birth\"]"))
        )

        if birth_element is None:
            raise Exception('Can not find element birth.')

        birth_element.send_keys(user.date)

        email_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=\"email\"]"))
        )

        if email_element is None:
            raise Exception('Can not find element email.')

        email_element.send_keys(user.email)

        phone_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=\"phone\"]"))
        )

        if phone_element is None:
            raise Exception('Can not find element phone.')

        phone_element.send_keys(user.phone)

        password_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=\"password\"]"))
        )

        if password_element is None:
            raise Exception('Can not find element password.')

        password_element.send_keys(user.password)

        re_password_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=\"repassword\"]"))
        )

        if re_password_element is None:
            raise Exception('Can not find element re password.')

        re_password_element.send_keys(user.password)

        if re_password_element is None:
            raise Exception('Can not find re-password.')

        captcha_image_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "imgcapcha"))
        )
        result = captcha_image_element.screenshot('captcha.png')
        if not result:
            raise Exception('Can not save screenshot.')

        # pypass captcha
        ocr = PaddleOCR(use_angle_cls=True, lang='en')
        result = ocr.ocr('captcha.png', cls=True)

        if len(result) == 0:
            raise Exception('Can not save pypass captcha.')

        for line in result:
            print(line)

        captcha_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "capcha"))
        )

        if captcha_element is None:
            raise Exception('Can not find capcha.')

        captcha_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "capcha"))
        )

        captcha_element.send_keys(result[0][1][0])

        submit_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=\"submit\""))
        )
        if submit_element is None:
            raise Exception('Can not find capcha.')

        submit_element.click()
        time.sleep(5)

        # login
        login_username_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\""))
        )
        login_username_element.send_keys(user.email)

        login_pass_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"password\""))
        )
        login_pass_element.send_keys(user.password)

        login_submit_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=\"submit\""))
        )

        login_submit_element.click()
        # wait element
        time.sleep(10)

        driver.get(url_buff_like)

        # wait element redheart
        redheart = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "redheart"))
        )

        redheart.click()

        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()

        time.sleep(5)

        return True
    except Exception as e:
        print('register exception: ', e)
        return False

    finally:
        driver.close()
