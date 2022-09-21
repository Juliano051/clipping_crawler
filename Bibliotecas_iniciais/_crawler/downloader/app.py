from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import random

class Bot:
    def __init__(self) -> None:
        url = "file:///C:/clipping/crawler/downloader/diarios/diarios.html"
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
        self.options.add_argument("--headless")
        
        self.options.add_experimental_option('prefs', {
        "download.default_directory": r'C:\clipping\crawler\downloader\downloads_diarios_hoje', #Change default directory for downloads
        "download.prompt_for_download": False, #To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
        })
        
        self.driver = webdriver.Chrome(executable_path="../../chromedriver/chromedriver.exe", options=self.options)
        
        estados =  ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MS','MT','MG','PA','PB','PR','PE','PI','RJ1','RJ2','RN','RS','RO','RR','SC','SP','SE1','TO']
        capitais = ["fortaleza","rio_branco", "maceio", "macapa", "manaus", "salvador", "vitoria", "goiania", "sao_luis", "campo_grande",  "cuiaba", "belo_horizonte", "belem", "joao_pessoa", "curitiba", "recife", "teresina", "rio_de_janeiro", "natal", "porto_alegre", "porto_velho", "boa_vista", "florianopolis", "sao_paulo", "palmas"]
        self.driver.get(url)
        sleep(5)
        print("\n*************************************************************************")
        print("Baixando diários oficiais dos estados")
        print("*************************************************************************\n")
        # self.driver.get_screenshot_as_file('screenshot.png')
        # for estado in estados:
        #     menu = self.driver.find_element(By.ID, estado.lower())
        #     sleep(1)
        #     print(f'Baixando {estado}... \n')
        #     sleep(random.randint(5, 15))
        #     menu.click()
            
        #     self.driver.get(url)
        
        print("\n*************************************************************************")
        print("* Baixando diários oficiais das capitais")
        print("*************************************************************************\n")
        for capital in capitais:
            menu = self.driver.find_element(By.ID, capital.lower())
            sleep(1)
            print(f'Baixando {capital}... \n')
            sleep(random.randint(5, 15))
            menu.click()
                        
            self.driver.get(url)


        print("\n*************************************************************************")
        print("* Baixando diário oficial da União")
        print("*************************************************************************\n")
        uniao = ["uniao0","uniao1","uniao2",]
        menu = self.driver.find_element(By.ID, uniao[0])
        sleep(1)
        print(f'Baixando DOU...\n')
        sleep(5)
        menu.click()

        # diario = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/span/div/div[3]/div/div[3]/a/span/i')
        
        # sleep(3) # substituir por espera automática do final do download
        # diario.click()
        # print(self.driver.title)
Bot()


'''
faltam

Rio branco
Porto Velho
Fortaleza
Aracaju

video 1 https://vimeo.com/729750850/7a89c572f0
video 2
'''
