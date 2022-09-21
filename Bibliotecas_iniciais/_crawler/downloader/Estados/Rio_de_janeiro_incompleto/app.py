from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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
        "download.default_directory": r'C:\clipping\crawler\downFiles\downFiles\downloads\Goias', #Change default directory for downloads
        "download.prompt_for_download": False, #To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
        })
        
        self.driver = webdriver.Chrome(executable_path="../../../chromedriver/chromedriver.exe", options=self.options)
        
        self.driver.get("http://www.ioerj.com.br/portal/modules/conteudoonline/do_ultima_edicao.php")

        # Setup wait for later
        wait = WebDriverWait(self.driver, 10)

        sleep(5)

        # Store the ID of the original window
        original_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        self.driver.get_screenshot_as_file('screenshot.png')

        diario = self.driver.find_element(By.XPATH, '//*[@id="xo-content"]/div[3]/ul/li[1]/a')
        sleep(2)
        diario.click()
        sleep(25) # substituir por espera automática do final do download

        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        self.driver.get_screenshot_as_file('screenshot2.png')
        link = self.driver.find_element(By.ID, "download")
       
        sleep(10)
        link.click()
        link.send_keys(Keys.ESCAPE).perform()
        sleep(1)
        print(len(self.driver.window_handles))
        sleep(100)
        '''print(self.driver.window_handles[-1])
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(2)
        arquivo = self.driver.find_element(By.ID, "open-button")
        arquivo.click()
        sleep(10)'''
        # print(self.driver.title)
Bot()
