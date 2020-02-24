from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

from time import sleep

from login_info import username, password


class TwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        


    def login(self):
        self.driver.get("https://twitter.com")
        self.driver.maximize_window()

        sleep(2)

        loginButton = self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div[2]/a[2]/div/span/span')
        loginButton.click()

        sleep(2)

        uNameField = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/main/div/div/form/div/div[1]/label/div[2]/div/input')
        uNameField.send_keys(username)

        passField = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/main/div/div/form/div/div[2]/label/div[2]/div/input')
        passField.send_keys(password)

        loginButton = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/main/div/div/form/div/div[3]/div/div')
        loginButton.click()

        sleep(5)

        self.getTrendingTopics()
        self.getNumberofNotifications()

        home = self.driver.find_element_by_xpath('/html/body/div/div/div/div/header/div/div/div/div/div[2]/nav/a[1]/div/div[2]/span')
        home.click()

    def sendTweet(self, tweet, picture_path):
        if (tweet==None):
            print("You need to input a tweet to do this!")
        elif (picture_path==None):
            print("Tweeting: " + tweet)

            textField = self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div')
            textField.send_keys(tweet)

            tweetButton = self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
            tweetButton.click()


            print("Tweet sent!")
        else:
            print("Tweeting: \"" + tweet + "\" with a picture")

            textField = self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div')
            textField.send_keys(tweet)

            upload = self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[1]/input')
            upload.send_keys(picture_path)

            tweetButton = self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
            tweetButton.click()

            print("Tweet sent!")

    def getTrendingTopics(self):
        print("This is what's trending:")

        for x in range(2, 7):
            trending = self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/section/div/div/div/div/div[' + str(x) + ']/div/div/div[2]/span')
            print(trending.text)

    def logout(self):
        print("Logging you out!")

        more = self.driver.find_element_by_xpath('/html/body/div/div/div/div/header/div/div/div/div/div[2]/nav/div/div/div[2]/span')
        more.click()

        sleep(2)

        logout = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div/div[12]/a/div/div/span')
        logout.click()

        sleep(2)

        confirm = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/span/span')
        confirm.click()

        sleep(2)

        self.driver.get("https://twitter.com")

    def getNumberofNotifications(self):
        try:
            notifications = self.driver.find_element_by_xpath('/html/body/div/div/div/div/header/div/div/div/div/div[2]/nav/a[3]/div/div[1]/div')

            notiNum = int(notifications.text)

            if(notifications.text != '0'):
                print("You have " + notifications.text + " notifications.")

                notiButton = self.driver.find_element_by_xpath('/html/body/div/div/div/div/header/div/div/div/div/div[2]/nav/a[3]/div/div[2]/span')
                notiButton.click()

                sleep(5)

                for x in range(1, notiNum+1):
                    print("NOTIFICATION NUMBER: " + str(x))
                    self.readNotification(x)

                print("Now you're all up to date!")
            else:
                print("No new notifications, you're all up to date!")
        except:
            print("No notifications!")

    def readNotification(self, num):
        try:
            notification = self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[' + str(num) + ']/div/article/div[1]/div[2]/div[3]/div/span')

            print(notification.text)
        except:
            try:
                notification = self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[' + str(num) + ']/div/article/div/div[2]/div/span/span/span')

                print(notification.text)
            except:
                print("There was an error reading this notification")
                pass