from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ddddocr
import onnxruntime


class Connect:
    def __init__(self, username, password, domain="vpn.szpt.edu.cn", debug=False):
        self.debug = debug
        self.domain = domain
        self.username = username
        self.password = password
        self.driver: webdriver.Chrome = None

        self.setting()

    def setting(self):
        # 屏蔽警告日志
        onnxruntime.set_default_logger_severity(3)
        options = webdriver.ChromeOptions()
        if self.debug is False:
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get("https://" + self.domain)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'input-txt'))
            )
            input_txt = self.driver.find_elements(by=By.CLASS_NAME, value='input-txt')

            # 输入用户名
            user_box = input_txt[0]
            user_box.send_keys(self.username)
            time.sleep(1)

            # 输入密码
            pwd_box = input_txt[1]
            pwd_box.send_keys(self.password)
            time.sleep(1)

            # 识别和输入验证码
            ocr = ddddocr.DdddOcr()
            code_pic = self.driver.find_element(by=By.CLASS_NAME, value='password__code__image')
            code_pic.screenshot('code.png')
            with open('code.png', 'rb') as f:
                code_img = f.read()
            code = ocr.classification(code_img)
            code_box = input_txt[2]
            code_box.send_keys(code)
            time.sleep(1)

            # 点击登录
            click_btn1 = self.driver.find_element(by=By.CLASS_NAME, value='checkbox__mark')
            click_btn2 = self.driver.find_element(by=By.CLASS_NAME, value='button')
            click_btn1.click()
            time.sleep(1)
            click_btn2.click()
            time.sleep(5)

            # 根据跳转页面状态码，判断是否登录成功
            if "/portal/#!/service" in self.driver.current_url:
                return True
            else:
                # 获取错误信息
                error = self.driver.find_elements(by=By.CLASS_NAME, value='enable-choose')[1]
                raise Exception(error.text)
        finally:
            self.driver.quit()
