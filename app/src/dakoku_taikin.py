import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':

    # Selenium サーバーへ接続する。
    driver = webdriver.Remote(
        command_executor=os.environ["SELENIUM_URL"],
        options=webdriver.ChromeOptions()
    )

    # Googleにアクセス
    driver.get("https://s2.kingtime.jp/independent/recorder/personal/")

    time.sleep(3)

    # id, パスワードの入力フォーム
    driver.find_element(by=By.CSS_SELECTOR, value='input#id').send_keys(os.environ["KING_OF_TIME_ID"])
    driver.find_element(by=By.CSS_SELECTOR, value='input#password').send_keys(os.environ["KING_OF_TIME_PASSWORD"])
    driver.find_element(by=By.CSS_SELECTOR, value='.btn-control-message').click() # サブミット

    time.sleep(3)

    # 退勤
    # driver.find_element(by=By.CSS_SELECTOR, value='.record-clock-out').click()

    driver.quit()

    print('退勤しました。')