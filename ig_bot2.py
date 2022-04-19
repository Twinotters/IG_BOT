from selenium import webdriver
from time import sleep


class InstaBot:
	def __init__(self, username, pw):
		
		# Opening browser
		self.driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
		self.username = username
		self.driver.get('https://www.instagram.com')
		
		sleep(4)

		#Accessing IG
		self.driver.find_element_by_xpath('//input[@name=\'username\']').send_keys(username)
		self.driver.find_element_by_xpath('//input[@name=\'password\']').send_keys(pw)
		self.driver.find_element_by_xpath("//button[@type='submit']").click()

		sleep(10)

		#'Not Now' pop ups
		self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
		sleep(4)
		self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()

		sleep(2)

		# Main Function
		
	def get_unfollowed(self):


		# Entering User Profile
		self.driver.find_element_by_xpath('//a[contains(@href,"/{}")]'.format(self.username)).click()

		sleep(2)

		self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div").click()

		sleep(4)

		to_unfollow = ['LIST PROVIDED BY FIRST BOT']


		for usuario in to_unfollow:
			self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(usuario)
			sleep(4)
			self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div[1]').click()
			sleep(4)
			self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button/div/div/span').click()
			sleep(4)
			self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
			sleep(4)



		
#Initaliazing
my_bot = InstaBot('YOUR USERNAME','YOUR PASSWORD')
my_bot.get_unfollowed()


