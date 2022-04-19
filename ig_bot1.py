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
		
		#Following List
		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div').click()
		following = self._get_names_following()

		sleep(2)

		#FOllowers List
		self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div").click()
		followers = self._get_names_followers()

		#List of not following back
		not_following_back = [user for user in following if user not in followers]
		print(not_following_back)

		for usuario in not_following_back:
			self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(usuario)
			sleep(4)
			self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div[1]').click()
			sleep(4)
			self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button/div/div/span').click()
			sleep(4)
			self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
			sleep(4)
		
		# Get List Function

	def _get_names_followers(self):

		sleep(2)

		# List Scroll Box
		scroll_box = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]')
		last_ht, ht = 0, 1
		
		# Scrolling Action
		while last_ht != ht:
			last_ht = ht
			sleep(2)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;

				""", scroll_box)
		
		# Name List Creation
		links = scroll_box.find_elements_by_tag_name('a')
		names = [name.text for name in links if name.text != '']

		#Quitting Scroll Box
		self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button').click()

		return names 

	def _get_names_following(self):

		sleep(2)

		# List Scroll Box
		scroll_box = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]')
		last_ht, ht = 0, 1
		
		# Scrolling Action
		while last_ht != ht:
			last_ht = ht
			sleep(2)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;

				""", scroll_box)
		
		# Name List Creation
		links = scroll_box.find_elements_by_tag_name('a')
		names = [name.text for name in links if name.text != '']

		#Quitting Scroll Box
		self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button').click()

		return names 

#Initaliazing
my_bot = InstaBot('YOUR USERNAME','YOUR PASSWORD')
my_bot.get_unfollowed()


