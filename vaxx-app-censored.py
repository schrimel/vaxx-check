from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=options)

while(True):
    driver.get("https://www.qtermin.de/Kommunales_Impfzentrum_StaedteRegionAachen")
    driver.implicitly_wait(15)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[5]/div[2]/div/div[2]/div/div[3]/div[2]").click()
    time.sleep(1)
    driver.implicitly_wait(15)
    count = 0
    while(count < 3):
        table = driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[5]/div[3]/div/div[2]/div[3]/div[1]/div/table")
        driver.implicitly_wait(15)
        body = table.find_element(By.TAG_NAME, "tbody")

        rows = body.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                if col.get_attribute("onclick") == None:
                    continue
                print(col.get_attribute("onclick"))
                if "jQuery" in col.get_attribute("onclick"):
                    senderEmail = "<youremail>"
                    msg = MIMEMultipart()
                    msg["Subject"] = "Free Vaxx 420 gg"
                    recvEmail = "<receiveremail>"
                    msg["From"] = senderEmail
                    msg["To"] = recvEmail
                    text = "vaxx available on " + col.text
                    msg.attach(MIMEText(text))
                    server = smtplib.SMTP("mail.gmx.net", 587)
                    server.starttls()
                    server.login(senderEmail, "<yourpassword>")
                    text = msg.as_string()
                    server.sendmail(senderEmail, recvEmail, text)
                    server.quit()
                    print("Free vaxx available gz 420")
                    exit(0)
        count = count + 1
        driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[5]/div[3]/div/div[2]/div[3]/div[1]/div/div/a[2]").click()
    time.sleep(3600)