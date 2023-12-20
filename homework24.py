"""Automated contact management script."""


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем веб-драйвер
browser = webdriver.Chrome()

# Открываем страницу с логином
browser.get('https://thinking-tester-contact-list.herokuapp.com/')
sleep(2)

# Открываем страницу с регистрацией - не нужно, если вы уже зарегистрированы
# buttonSignup = browser.find_element(By.ID, 'signup')
# buttonSignup.click()
# sleep(5)

# Заполняем форму регистрации - если аккаунт уже зарегистрирован, то регистрация будет ошибочной,
# если вы хотите зарегистрироваться, то отредактируйте закоментированные данные ниже:

# firstName = browser.find_element(By.ID, 'firstName')
# firstName.send_keys('Ivan')
# lastName = browser.find_element(By.ID, 'lastName')
# lastName.send_keys('Ivanov')
# email = browser.find_element(By.ID, 'email')
# email.send_keys('ivan.ogurtsov@gmail.com')
# password = browser.find_element(By.ID, 'password')
# password.send_keys('Vania1996123qwe')
# # Нажимаем на кнопку Submit
# buttonSubmit = browser.find_element(By.ID, 'submit')
# buttonSubmit.click()
# sleep(5)

# Логин в систему
loginEmail = browser.find_element(By.ID, 'email')
loginEmail.clear()
sleep(1)
loginEmail.send_keys('jjgraffity@gmail.com')
loginPassword = browser.find_element(By.ID, 'password')
loginPassword.clear()
sleep(1)
loginPassword.send_keys('Vania1996123qwe')
buttonSubmit = browser.find_element(By.ID, 'submit')
buttonSubmit.click()
sleep(2)

# Добавляем новый контакт
buttonAddANewContact = browser.find_element(By.ID, 'add-contact')
buttonAddANewContact.click()
sleep(1)
firstName = browser.find_element(By.ID, 'firstName')
firstName.send_keys('Ivan')
sleep(1)
lastName = browser.find_element(By.ID, 'lastName')
lastName.send_keys('Ivanov')
sleep(1)
birthdate = browser.find_element(By.ID, 'birthdate')
birthdate.send_keys('1996-11-26')
sleep(1)
email = browser.find_element(By.ID, 'email')
email.send_keys('example@example.com')
sleep(1)
phone = browser.find_element(By.ID, 'phone')
phone.send_keys('1234567890')
sleep(1)
street1 = browser.find_element(By.ID, 'street1')
street1.send_keys('Test1')
sleep(1)
street2 = browser.find_element(By.ID, 'street2')
street2.send_keys('Test2')
sleep(1)
city = browser.find_element(By.ID, 'city')
city.send_keys('Minsk')
sleep(1)
stateProvince = browser.find_element(By.ID, 'stateProvince')
stateProvince.send_keys('Minsk')
sleep(1)
postalCode = browser.find_element(By.ID, 'postalCode')
postalCode.send_keys('220069')
sleep(1)
country = browser.find_element(By.ID, 'country')
country.send_keys('Belarus')
sleep(1)
buttonSubmit = browser.find_element(By.ID, 'submit')
buttonSubmit.click()
sleep(5)

# Обновляем контакт
contactTableBodyRow = browser.find_element(By.CLASS_NAME, 'contactTableBodyRow')
contactTableBodyRow.click()
editContactButton = browser.find_element(By.ID, 'edit-contact')
editContactButton.click()
firstName = browser.find_element(By.ID, 'firstName')
sleep(1)
firstName.clear()
sleep(1)
firstName.send_keys('Ivan')
lastName = browser.find_element(By.ID, 'lastName')
lastName.clear()
sleep(1)
lastName.send_keys('Ivanov')
birthdate = browser.find_element(By.ID, 'birthdate')
birthdate.clear()
sleep(1)
birthdate.send_keys('1996-11-27')
email = browser.find_element(By.ID, 'email')
email.clear()
sleep(1)
email.send_keys('test@example.com')
phone = browser.find_element(By.ID, 'phone')
phone.clear()
sleep(1)
phone.send_keys('1234567891')
street1 = browser.find_element(By.ID, 'street1')
street1.clear()
sleep(1)
street1.send_keys('Test3')
street2 = browser.find_element(By.ID, 'street2')
street2.clear()
sleep(1)
street2.send_keys('Test4')
city = browser.find_element(By.ID, 'city')
city.clear()
sleep(1)
city.send_keys('Minsks')
stateProvince = browser.find_element(By.ID, 'stateProvince')
stateProvince.clear()
sleep(1)
stateProvince.send_keys('Minsks')
postalCode = browser.find_element(By.ID, 'postalCode')
postalCode.clear()
sleep(1)
postalCode.send_keys('220089')
country = browser.find_element(By.ID, 'country')
country.clear()
sleep(1)
country.send_keys('Russia')
buttonSubmit = browser.find_element(By.ID, 'submit')
buttonSubmit.click()
sleep(5)

# Удаляем контакт
deleteContactButton = browser.find_element(By.ID, 'delete')
deleteContactButton.click()
sleep(2)
browser.switch_to.alert.accept()
sleep(5)
browser.quit()
