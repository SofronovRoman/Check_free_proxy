import time
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver
import socket


def bypass_cloudflare(driver):
    start = time.time()
    while (time.time()-start < 10):
        try:
            driver.find_element(By.CLASS_NAME, 'hcaptcha-box').click()
        except:
            pass
        try:
            driver.find_element(By.CLASS_NAME, 'big-button.pow-button').click()
        except:
            pass
        time.sleep(2)


def check_blocking(driver):
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'tbody')))
        return False
    except:
        return True


def get_proxy(driver, url: str, col_ip: int, col_port: int) -> list:
    driver.get(url)
    if not check_blocking(driver):
        pass
    else:
        bypass_cloudflare(driver)
    list_of_proxy = []
    trs = WebDriverWait(driver, 10).until(lambda d: d.find_elements(By.TAG_NAME, "tr"))
    for i in range(len(trs)):
        try:
            tds = trs[i].text.split()
            if col_ip == col_port:
                ip = tds[col_ip].split(':')[0]
                port = tds[col_port].split(':')[1]
            else:
                ip = tds[col_ip]
                port = tds[col_port]
            socket.inet_aton(ip)
            dictionary = {'ip': ip, 'port': port}
            list_of_proxy.append(dictionary)
        except:
            pass
    return list_of_proxy


def check_proxy(proxy):
    try:
        print(f'Проверяемый прокси: {proxy}')
        with requests.Session() as s:
            response = s.get('https://iplocation.com/', proxies=proxy, timeout=20).text
            tags = {'ip': '<td><b class="ip">',
                    'country': '<td><span class="country_name">',
                    'region': '<td><span class="region_name">',
                    'city': '<td class="city">',
                    'company': '<td class="company">'}
            out = {}
            for key, value in tags.items():
                index_start = response.find(value)
                index_end = response.find('</', index_start)
                out[key] = response[index_start+len(value): index_end]
            print(f'\033[0;92mРезультат проверки: {out}\033[00m')
    except:
        print('\033[1;31mРезультат проверки: Соединение не установлено\033[00m')
    print()


def main():
    driver = undetected_chromedriver.Chrome()
    urls = ['https://www.sslproxies.org/',
            'https://hidemy.name/ru/proxy-list/?type=s#list']
    lists = []
    for url in urls:
        list_of_proxy = get_proxy(driver, url, 0, 1)
        lists += list_of_proxy
    driver.close()
    for item in lists:
        proxy = {'https': item['ip'] + ':' + item['port']}
        check_proxy(proxy)


if __name__ == '__main__':
    main()