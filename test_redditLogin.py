#login into reddit.com and upvote the first new post in r/SimonFraser
import unittest
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class TestReddit(unittest.TestCase):
    def setUp(self):
        #set username and password
        self.username = "ENTER YOUR USERNAME HERE"
        self.password = "ENTER YOUR PASSWORD HERE"

        #Path to ChromeDriver
        PATH = "C:\Program Files (x86)\chromedriver.exe" #change path to local chromedriver
        
        #setting-up instance of Chrome
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.reddit.com/login/")

    def test_invalid_login(self):
        #filling username and password into the fields
        usrNameField = self.driver.find_element_by_id("loginUsername")
        usrNameField.clear()
        usrNameField.send_keys("hjjkhj$k#5sad58*f65")

        passField = self.driver.find_element_by_id("loginPassword")
        passField.clear()
        self.driver.implicitly_wait(5)
        passField.send_keys("asdfsadfsdf656", Keys.RETURN)

        #check if credentials not accepted
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_id("header-search-bar")

    def test_enter_valid_login(self):
        #filling username and password into the fields
        usrNameField = self.driver.find_element_by_id("loginUsername")
        usrNameField.clear()
        usrNameField.send_keys(self.username)

        self.driver.implicitly_wait(5)
        passField = self.driver.find_element_by_id("loginPassword")
        passField.clear()
        passField.send_keys(self.password, Keys.RETURN)

        #check if the password and username are valid
        try:
            searchBar = self.driver.find_element_by_id("header-search-bar")
        except NoSuchElementException:
            self.assertFalse(0)
      
    def test_subbreddit_search(self):
        #filling username and password into the fields
        usrNameField = self.driver.find_element_by_id("loginUsername")
        usrNameField.clear()
        usrNameField.send_keys(self.username)

        self.driver.implicitly_wait(5)
        passField = self.driver.find_element_by_id("loginPassword")
        passField.clear()
        passField.send_keys(self.password, Keys.RETURN)
        
        #go to the subreddit
        self.driver.implicitly_wait(5)
        searchBar = self.driver.find_element_by_id("header-search-bar")
        searchBar.send_keys("r/simonfraser", Keys.RETURN)
        try:
            desiredSub = self.driver.find_element_by_link_text("r/simonfraser")
            desiredSub.send_keys(Keys.RETURN)
        except NoSuchElementException:
            self.assertFalse(0)

    def test_upvoting_newest_post(self):
        #filling username and password into the fields
        usrNameField = self.driver.find_element_by_id("loginUsername")
        usrNameField.clear()
        usrNameField.send_keys(self.username)

        self.driver.implicitly_wait(5)
        passField = self.driver.find_element_by_id("loginPassword")
        passField.clear()
        passField.send_keys(self.password, Keys.RETURN)
        
        #go to the subreddit
        self.driver.implicitly_wait(5)
        searchBar = self.driver.find_element_by_id("header-search-bar")
        searchBar.send_keys("r/simonfraser", Keys.RETURN)
        self.driver.implicitly_wait(10)
        desiredSub = self.driver.find_element_by_link_text("r/simonfraser")
        desiredSub.send_keys(Keys.RETURN)
        
        #filter by new
        self.driver.implicitly_wait(10)
        desiredSub = self.driver.find_element_by_link_text("New")
        desiredSub.send_keys(Keys.RETURN)

        #find and upvote first post
        try:
            self.driver.implicitly_wait(10)
            upPost = self.driver.find_element_by_css_selector('[aria-label="upvote"]')
            upPost.send_keys(Keys.RETURN)
        except NoSuchElementException:
            self.assertFalse(0, "Failure to upvote post")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()