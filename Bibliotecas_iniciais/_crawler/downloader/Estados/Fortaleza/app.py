from PIL import Image
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import urllib.request
from twocaptcha import TwoCaptcha

class Bot:
    def __init__(self) -> None:
        solver = TwoCaptcha('ff2183fe73f4f011378a7e442932e5b9')

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
        #"download.default_directory": r'C:\clipping\crawler\downFiles\downFiles\downloads\Palmas', #Change default directory for downloads
        "download.default_directory": r'./', #Change default directory for downloads
        "download.prompt_for_download": False, #To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
        })
        
        self.driver = webdriver.Chrome(executable_path="../../../../chromedriver/chromedriver.exe", options=self.options)
        
        self.driver.get("https://diariooficial.fortaleza.ce.gov.br/")
       
        self.driver.get_screenshot_as_file('screenshot.png')
        captcha = self.driver.find_element(By.XPATH, "//*[@id='searchFilter']/fieldset/div[5]/p/img")
        campo =  self.driver.find_element(By.XPATH, '//*[@id="searchFilter"]/fieldset/div[6]/input')
        botao = self.driver.find_element(By.ID, "submit-diario")
        
        sleep(3)
        
        # download the captcha image
        def get_captcha(driver, element, path):
            # now that we have the preliminary stuff out of the way time to get that image :D
            location = element.location
            size = element.size
            # saves screenshot of entire page
            driver.save_screenshot(path)

            # uses PIL library to open image in memory
            image = Image.open(path)

            left = location['x']
            top = location['y'] #+ 140
            right = location['x'] + size['width']
            bottom = location['y'] + size['height'] #+ 140
            print(f'left top {left}, {top}')
            image = image.crop((left, top, right, bottom))  # defines crop points
            image.save(path, 'png')  # saves new cropped image
        
        get_captcha(self.driver, captcha, "captcha.png" )
     
        # envia pro captcha solver
        result = solver.normal('captcha.png')

        sleep(2)
        # print(f"Código decifrado: {result['code']}")
        campo.send_keys(result['code'])
        botao.click()        
        sleep(10)
        
        diario = self.driver.find_element(By.XPATH, "//*[@id='diarios-oficiais']/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/a")
        data_diario = self.driver.find_element(By.XPATH, '//*[@id="diarios-oficiais"]/div/div[2]/div[2]/table/tbody/tr[1]/td[2]')
        data_diario = data_diario.get_attribute("innerHTML").replace('/','-')

        # src_diario = diario.get_attribute('src')
        
        # with urllib.request.urlopen(src_diario) as response, open(f"{data_diario}.pdf", 'wb') as out_file:
        #     shutil.copyfileobj(response, out_file)

        diario.click()
        print(f'Saldo: {solver.balance}')
        sleep(30) # substituir por espera automática do final do download
        # print(self.driver.title)
        
Bot()