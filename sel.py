import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('/Users/kemalsener/Downloads/chromedriver')
url = 'https://www.biletix.com/'

driver.implicitly_wait(5)

driver.get(url)
driver.find_element_by_xpath('//*[@id="_evidon-accept-button"]').click()
# driver.find_element_by_xpath('//div[@class="dialog_close"]').click() #

select = Select(driver.find_element_by_id('category_sb'))
select.select_by_value('MUSIC')

select = Select(driver.find_element_by_id('date_sb'))
select.select_by_value('next30days')

select = Select(driver.find_element_by_id('city_sb'))
select.select_by_value('-1')

driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@class="discoverbar__button"]').click()

events = driver.find_elements_by_xpath('//*[@class="grid_21 alpha omega listevent searchResultEvent"]/div')

status_list = []
name_list = []
date_list = []

for i in range(4):

    for event in events:

        names = event.find_elements_by_xpath('//*[@class="grid_5 omega searchResultInfo1b"]/a')
        dates = event.find_elements_by_xpath(
        '//*[@class="grid_3 alpha fld3 col-xs-12 searchResultInfo3 hiddenOnMobile"]/div')
        statuses = event.find_elements_by_xpath('//*[@class="grid_5 omega searchResultInfo1b"]/span')

        for name in names:
            fun = name.text
            print(fun)
            name_item = {
                fun
            }
            name_list.append(name_item)

        for date in dates:
            when = date.text
            print(when)
            date_item = {
                when
            }
            date_list.append(date_item)

        for status in statuses:
            stat = status.text
            print(stat)
            status_item = {
                stat
            }
            status_list.append(status_item)

    df = pd.DataFrame({
        "name": name_list,
        "date": date_list,
        "status": status_list
    })
    driver.find_element_by_xpath('// *[ @ id = "paginator"] / ul / li[6] / a').click()
    print(df)
    df.to_csv('/Users/kemalsener/Downloads/Activities.csv')

driver.quit()
