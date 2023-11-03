print(" __   __                        _______                _   _                 _                 __\n \ \ / /                       |__   __|              | \ | |               | |               /_ |\n  \ V /_   _ _   _  ___ _ __      | |_ __ __ _ _ __   |  \| |_   _ _ __ ___ | |__   ___ _ __   | |\n   > <| | | | | | |/ _ \ '_ \     | | '__/ _` | '_ \  | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|  | |\n  / . \ |_| | |_| |  __/ | | |    | | | | (_| | | | | | |\  | |_| | | | | | | |_) |  __/ |     | |\n /_/ \_\__,_|\__, |\___|_| |_|    |_|_|  \__,_|_| |_| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     |_|\n              __/ |                                                                               \n             |___/                                                                                 ")
print("Version: 0.0.0.0.0")
# Template. DO NOT TOUCH
try:
    from os import system
    import pip
    system("pip install -r ETC/requirements.txt")
    print("Tải dữ liệu cần thiết thành công")
except:
    print("Lỗi trích xuất dữ liệu dòng 5")
try:
    from time import sleep
    print("Trích dữ liệu thành công #1")
except:
    print("Lỗi trích xuất dữ liệu dòng 11")
try:
    from bs4 import *
    print("Trích dữ liệu thành công #2")
except:
    print("Lỗi trích xuất dữ liệu dòng 15")
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    print("Trích dữ liệu thành công #3")
except:
    print("Lỗi trích xuất dữ liệu dòng 20")
try:
    import webbrowser
    print("Trích dữ liệu thành công #4")
except:
    print("Lỗi trích xuất dữ liệu dòng 28")
try:
    import socket
    print("Trích dữ liệu thành công #5")
except:
    print("Lỗi trích xuất dữ liệu dòng 33")
try:
    import random
    print("Trích dữ liệu thành công #6")
except:
    print("Lỗi trích xuất dữ liệu dòng 38")
try:
    import validators
    print("Trích dữ liệu thành công #7")
except:
    print("Lỗi trích xuất dữ liệu dòng 44")
# End template
system('title Tự động làm Hanoi Study. Made For: Xuyến Trần')

# URL
MathUrl = [
    '1'
]
PhysicalUrl = [
    'https://study.hanoi.edu.vn/huong-dan-thi/e-on-tap-vat-ly-chuong-2-khoi-6-2337',
    'https://study.hanoi.edu.vn/huong-dan-thi/e-on-tap-vat-ly-chuong-1-khoi-6-2335'
]
ChemistryhUrl = [
    ''
]
GDCDUrl = [
    ''
]
SinhUrl = [
    ''
]
EnUrl = [
    ''
]
DiaUrl = [
    'https://study.hanoi.edu.vn/huong-dan-thi/e-on-tap-ia-ly-khoi-6-chuong-2-2339'
]
SuUrl = [
    'https://study.hanoi.edu.vn/huong-dan-thi/e-on-tap-lich-su-khoi-6-chuong-4-2338'
]
# Random
MathUrl = random.choice(MathUrl)
PhysicalUrl = random.choice(PhysicalUrl)
GDCDUrl = random.choice(GDCDUrl)
SinhUrl = random.choice(SinhUrl)
EnUrl = random.choice(EnUrl)
DiaUrl = random.choice(DiaUrl)
SuUrl = random.choice(SuUrl)

# webbrowser.open_new('https://fnsurvival.github.io/o/XT')

# Choose Subject
print("\n\n\n\n\n\n\nPhần mềm sẽ chọn 1 bài ngẫu nhiên trong danh sách đã được cài trước để làm\nChọn môn muốn làm\n\t1.Toán   2.Lý   3.Hóa   4.GDCD   5.Sinh Học   6.Tiếng Anh  7.Địa lý  8.Sử")
try:
    ChooseSubject = int(input("Chọn số để bắt đầu làm: "))
    captchaInputText = input('Điền mã captcha: ')
except:
    system('cls')
    print('\nChọn hợp lý ko chọn ngốc')
    print('Đang khởi động lại')
    system("py Main.py")
    system('cls')
    
driver = webdriver.Chrome()
driver.maximize_window()
def SetUP():
    if ChooseSubject == 1:                                      # Math
        print('Chưa hỗ trợ')
        driver.quit()
        pass
    elif ChooseSubject == 2:                                    #Physic
        # Create session
        driver.implicitly_wait(30)
        driver.get(PhysicalUrl)

        # Find element with specelific id
        go = driver.find_element(By.ID, 'copyip')
        go.click()
        
    elif ChooseSubject == 3:                                      # Chemistry
        print('Chưa hỗ trợ')
        driver.quit()
        pass
    elif ChooseSubject == 4:                                      # GDCD
        print('Chưa hỗ trợ')
        driver.quit()
        pass
    elif ChooseSubject == 5:                                      # SInh
        print('Chưa hỗ trợ')
        driver.quit()
        pass
    elif ChooseSubject == 6:                                      # Eng
        print('Chưa hỗ trợ')
        driver.quit()
        pass
    elif ChooseSubject == 7:                                      # Dia
        # Create session
        driver.implicitly_wait(30)
        driver.get(DiaUrl)
        input('Đang đang đợi người dùng đăng nhập. Xong rồi hoặc đã đăng nhập từ trước thì ấn nút bất kỳ để tiếp tục')
        # Start 
        driver.find_element(By.ID, "start-test").click()
        driver.find_element(By.XPATH, "//a[@onclick='SubmitTestResultClick();']").click()
        sleep(0.2)
        driver.find_element(By.XPATH, '//input[@type="text"]').send_keys(captchaInputText)
        driver.find_element(By.XPATH, "//button[@type='submit' and text()='Xác nhận']").click()
    elif ChooseSubject == 8:                                      # Sử
        # Create session
        driver.implicitly_wait(30)
        driver.get(SuUrl)
        # Find element with specelific id
        go = driver.find_element(By.ID, 'copyip')
        go.click()
    else:
        print('Hãy nghĩ trước khi chọn ^^')
SetUP()