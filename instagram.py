from instagramUserİnfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()
        self.followers = []
        self.follows = []
        self.unfollowers = []

    def signIn(self):
        # Instagram ana sayfasını aç
        self.browser.get('https://www.instagram.com/')
        time.sleep(3)
        self.browser.maximize_window()

        # Kullanıcı adı ve şifre giriş alanlarını bul ve giriş yap
        username_input = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_input = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(20)

    def getFollowers(self):
        # Profil sayfasına git
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(5)

        # Takipçiler bağlantısını bul ve tıkla
        followers_link = self.browser.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div")
        followers_link.click()
        time.sleep(5)

        # İlk sayfa takipçi listesini al
        elements = self.browser.find_elements(By.XPATH, "//*[contains(@class, '_ap3a') and contains(@class, '_aaco') and contains(@class, '_aacw') and contains(@class, '_aacx') and contains(@class, '_aad7') and contains(@class, '_aade')]")
        print(f"Başlangıçta alınan takipçi sayısı: {len(elements)}")

        # Kaydırma yapılacak div
        scrollable_div = self.browser.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")

        # Kaydırma işlemi
        last_height = self.browser.execute_script("return arguments[0].scrollHeight", scrollable_div)
        while True:
            #ojini yerine getirme
            self.browser.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scrollable_div)
            time.sleep(3)

            # Yeni yükseklik kontrolü
            new_height = self.browser.execute_script("return arguments[0].scrollHeight", scrollable_div)
            if new_height == last_height:
                break  # Daha fazla yüklenmediyse çık
            last_height = new_height

        # Tüm takipçileri yeniden çek
        followers = self.browser.find_elements(By.XPATH, "//*[contains(@class, '_ap3a') and contains(@class, '_aaco') and contains(@class, '_aacw') and contains(@class, '_aacx') and contains(@class, '_aad7') and contains(@class, '_aade')]")
        print(f"Toplam takipçi sayısı: {len(followers)}")

        # Takipçileri yazdır
        for user in followers:
            self.followers.append(user.text)
    
    def getFollows(self):
        # Profil sayfasına git
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(15)

        # Takipçiler bağlantısını bul ve tıkla
        follows_link = self.browser.find_element(By.XPATH, "//*[contains(@id, 'mount_0_0_')]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div")
        follows_link.click()
        time.sleep(5)

        # İlk sayfa takipçi listesini al
        elements = self.browser.find_elements(By.XPATH, "//*[contains(@class, '_ap3a') and contains(@class, '_aaco') and contains(@class, '_aacw') and contains(@class, '_aacx') and contains(@class, '_aad7') and contains(@class, '_aade')]")
        print(f"Başlangıçta alınan takipçi sayısı: {len(elements)}")

        # Kaydırma yapılacak div
        scrollable_div = self.browser.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")

        # Kaydırma işlemi
        last_height = self.browser.execute_script("return arguments[0].scrollHeight", scrollable_div)
        while True:
            # Div'i aşağı kaydır
            self.browser.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scrollable_div)
            time.sleep(3)

            # Yeni yükseklik kontrolü
            new_height = self.browser.execute_script("return arguments[0].scrollHeight", scrollable_div)
            if new_height == last_height:
                break  # Daha fazla yüklenmediyse çık
            last_height = new_height

        # Tüm takipçileri yeniden çek
        follows = self.browser.find_elements(By.XPATH, "//*[contains(@class, '_ap3a') and contains(@class, '_aaco') and contains(@class, '_aacw') and contains(@class, '_aacx') and contains(@class, '_aad7') and contains(@class, '_aade')]")
        print(f"Toplam takipçi sayısı: {len(follows)}")

        # Takipçileri yazdır
        for user in follows:
            self.follows.append(user.text)
        

    def getUnfallowers(self):
        i = 0
        while i < len(self.followers):
            try:
                if self.followers[i] in self.follows:
                    i += 1
                else:
                    self.unfollowers.append(self.followers[i])
                    i += 1
            except Exception as e :
                print(f"Hata: {e}")
                break
        for i in self.unfollowers:
            print(f"unfollower: {i}")
    



# Instagram sınıfını çalıştır
instagram = Instagram(username, password)
instagram.signIn()
instagram.getFollowers()
instagram.getFollows()
instagram.getUnfallowers()


