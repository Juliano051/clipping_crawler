import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import shutil
from time import sleep

class Bot:
    def __init__(self) -> None:
        user_agent = '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 
        (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'''
        self.options = webdriver.ChromeOptions()
        self.options.headless = False
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        
        self.options.add_experimental_option('prefs', {
        "download.default_directory": r'./', #Change default directory for downloads
        "download.prompt_for_download": False, #To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": False #It will not show PDF directly in chrome
        })
        
        self.driver = webdriver.Chrome(executable_path="../../../../chromedriver/chromedriver.exe", options=self.options)
        
        self.driver.get("http://sga.aracaju.se.gov.br:5011/legislacao/faces/diario_form_pesq.jsp")
        self.driver.get_screenshot_as_file('screenshot.png')
        # sleep(3)
        #botao = self.driver.find_element('xpath', '// div [@class="parte-textual"]').click()
        sleep(1)
        # link = self.driver.find_element(By.CLASS_NAME, 'parte-textual')
        check_mes_ano = self.driver.find_element(By.XPATH, '//*[@id="formPesquisarDiario:j_id_jsp_1760165330_6:1"]')
        check_mes_ano.click()
        sleep(1)
        submit = self.driver.find_element(By.CLASS_NAME, 'botaoCadastrarPesq')
        submit.click()
        sleep(1)
        nome_arq_diario = "aracaju_"+self.driver.find_element(By.XPATH, '/html/body/div[2]/form/span[2]/table/tbody/tr[1]/td[1]/div/div[1]').get_attribute('innerHTML').replace('/', '-')+'.pdf'
        
        botao_diario_pdf = self.driver.find_element(By.XPATH, '//html/body/div[2]/form/span[2]/table/tbody/tr[1]/td[1]/div/div[2]/table[2]/tbody/tr/td/a/img')
        botao_diario_pdf.click()
        sleep(25)
        pdf_url = self.driver.find_element(By.ID, 'pdf')
        print(pdf_url.get_attribute("src"))
        with urllib.request.urlopen(pdf_url.get_attribute('src')) as response, open(nome_arq_diario, 'wb') as pdf_file:
            shutil.copyfileobj(response, pdf_file)

        # /html/body/div[2]/table/tbody/tr/td/iframe
        # //*[@id="open-button"]
        # diario.click()
        sleep(60) # substituir por espera automática do final do download
        # print(self.driver.title)
Bot()
