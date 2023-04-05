from selenium.webdriver.common.by import By
class registerpage:
    myaccountlink = "My Account"
    registerlink = "Register"
    firstname = "input-firstname"
    lastname = "input-lastname"
    emailid = "input-email"
    password = "input-password"
    newsletter = "input-newsletter-yes"
    checkbox = "//input[@type='checkbox']"
    continuebutton = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def clickonmyaccountlink(self):
        self.driver.find_element(By.LINK_TEXT, self.myaccountlink).click()

    def clickonregisterlink(self):
        self.driver.find_element(By.LINK_TEXT, self.registerlink).click()

    def enterthefirstname(self,firstname):
        self.driver.find_element(By.ID, "input-firstname").send_keys(firstname)

    def enterthelastname(self, lastname):
        self.driver.find_element(By.ID, "input-lastname").send_keys(lastname)

    def enteremail(self, email):
        self.driver.find_element(By.ID, self.emailid).send_keys(email)

    def enterpassword(self, password):
        self.driver.find_element(By.ID, self.password).send_keys(password)

    def clickonnewsletter(self):
        self.driver.find_element(By.ID, "input-newsletter-yes").click()

    def clickoncheckbox(self):
        self.driver.find_element(By.XPATH, self.checkbox).click()

    def clickoncontinue(self):
        self.driver.find_element(By.XPATH, self.continuebutton).click()
