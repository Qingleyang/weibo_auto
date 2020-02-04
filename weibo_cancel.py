# 模拟微博自动登录
from selenium import webdriver
import time
browser = webdriver.Chrome('/Users/amy/Downloads/chromedriver')
# 登陆微博
def weibo_login(username, password):
    # 打开微博登录页
    browser.get('https://passport.weibo.cn/signin/login')
    browser.implicitly_wait(5)
    time.sleep(1)
    # 填写登录信息：用户名、密码
    browser.find_element_by_id("loginName").send_keys(username)
    browser.find_element_by_id("loginPassword").send_keys(password)
    time.sleep(1)
    # 点击登录
    browser.find_element_by_id("loginAction").click()
    time.sleep(1)
# 设置用户名、密码
username = '**********'
password = '**********'
weibo_login(username, password)
# 取消指定的用户
def out_follow(uid):
    browser.get('https://m.weibo.cn/u/' + str(uid))
    time.sleep(1)
    # browser.find_element_by_id("follow").click()
    out_follow_button = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[4]/div[2]/div/div[1]/div/span/h4')
    out_follow_button.click()
    time.sleep(1)

    # 点击取消关注
    out_button1 = browser.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[4]/div[2]/div/div[1]/div/div/ul/li[2]/div/h4')
    out_button1.click()

    # 再次确认取消关注
    out_button2 = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[2]/footer/div[2]/a')
    out_button2.click()
    time.sleep(1)


# 每天学点心理学 UID
uid = '1890826225'
out_follow(uid)