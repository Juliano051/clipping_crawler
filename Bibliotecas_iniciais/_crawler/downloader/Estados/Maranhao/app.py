from selenium import webdriver
from selenium.webdriver.common.by import By
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
        "download.default_directory": r'E:\clipping\crawler\downFiles\downFiles\downloads\Espirito_Santo', #Change default directory for downloads
        "download.prompt_for_download": False, #To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
        })
        
        self.driver = webdriver.Chrome(executable_path="../../../chromedriver/chromedriver.exe", options=self.options)
        
        self.driver.get("https://www.diariooficial.ma.gov.br/public/index.xhtml")
        # self.driver.get_screenshot_as_file('screenshot.png')
        caderno = self.driver.find_element(By.ID, "formPesq:comboCaderno")
        data_inicio = self.driver.find_element(By.ID, "formPesq:calendarInic_input")
        data_fim = self.driver.find_element(By.ID, "formPesq:calendarFim_input")
        
        caderno.send_keys("exec")
        data_inicio.send_keys("07/07/2022")
        data_fim.send_keys("07/07/2022")
        # sleep(3)
        botao = self.driver.find_element('xpath', '//*[@id="formPesq"]/table[2]/tbody/tr[1]/td/input').click()
        link = self.driver.find_element('xpath', "//td[@role='gridcell']").click()
        
        # botao.click()
        # diario.click()
        sleep(60) # substituir por espera automática do final do download
        # print(self.driver.title)
Bot()