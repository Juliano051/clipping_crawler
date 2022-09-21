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
        "download.default_directory": r'.', #Change default directory for downloads
        "download.prompt_for_download": True, #To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
        })
        
        self.driver = webdriver.Chrome(executable_path="../../../../chromedriver/chromedriver.exe", options=self.options)
        
        self.driver.get("https://www.pmf.sc.gov.br/governo/index.php?pagina=govdiariooficial")
        self.driver.get_screenshot_as_file('screenshot.png')
        #diario = self.driver.find_element(By.ID, "baixar-diario-completo")
        diario = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div/div[5]/ul/li[1]/a")
        sleep(3)
        diario.click()
        sleep(60) # substituir por espera automática do final do download
        # print(self.driver.title)
Bot()
