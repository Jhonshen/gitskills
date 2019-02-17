from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from email.mime.text import MIMEText
import time
from selenium.webdriver.common.keys import Keys
while 2 > 1:
	print('start find')
	driver = webdriver.PhantomJS(executable_path = r'G:\python\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	driver.get("http://hr-welcometo.huawei.com/wcaportal")
	time.sleep(3)
	driver.find_element_by_id("uid").send_keys("Shen_Bin_")
	time.sleep(3)
	driver.find_element_by_id("password").send_keys('m18357303509jh21.')
	time.sleep(3)
	driver.find_element_by_xpath("//input[@class='login_submit_pwd']").click()
	time.sleep(3)	
	driver.find_element_by_id("cil3::icon").click();
	time.sleep(3)
	driver.find_element_by_id("r1:1:cb3").click()
	time.sleep(3)
	try:
		driver.find_element_by_id("r1:1:i1:0:i3:0:i4:0:i5")
		time.sleep(3)
		driver.find_element_by_id("r1:1:i1:0:i3:0:i4:1:i5")
		time.sleep(3)
		driver.find_element_by_id("r1:1:i1:0:i3:0:i4:2:i5")
		time.sleep(3)
		driver.find_element_by_id("r1:1:i1:0:i3:0:i4:3:i5")
		time.sleep(3)
		driver.find_element_by_id("r1:1:i1:0:i3:1:i4:0:i5")
		time.sleep(3)
		driver.find_element_by_id("r1:1:i1:0:i3:1:i4:1:i5")
		time.sleep(3)
		driver.find_element_by_id("r1:1:i1:0:i3:1:i4:2:i5")
		time.sleep(3)
		driver.find_element_by_id("r1:1:i1:0:i3:1:i4:3:i5")
		time.sleep(3)
	except NoSuchElementException:
		print('no element2')
		msg = MIMEText('hello jhon', 'plain', 'utf-8')
		from_addr = '3485814726@qq.com'
		password = 'nmrddmfahqhhchda'
		to_addr = '1002785627@qq.com'
		smtp_server = 'smtp.qq.com'
		import smtplib
		server = smtplib.SMTP(smtp_server, 25)
		server.login(from_addr, password)
		server.sendmail(from_addr, [to_addr], msg.as_string())
		server.quit()
	finally:
		driver.quit()
	time.sleep(3600)
