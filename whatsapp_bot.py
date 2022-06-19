from time import sleep

from selenium import webdriver

# LOGIN


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox()
    # GET SITE
        self.driver.get("https://web.whatsapp.com/")
        sleep(20)
        self.driver.find_elements_by_xpath(
        '/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[7]/div/div/div[1]/div[2]/div[1]/div[1]/span/span').click()
    # SEND MESSAGE
        msg_input = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
        msg_input.send_keys('msg')
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[2]/button/span').click


def main():
    myBot = Bot()


if __name__ == "__main__":
    main()