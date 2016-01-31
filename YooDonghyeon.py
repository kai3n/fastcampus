# class Calculator():
#     def __init__(self):
#         pass
#
#     def add(self, x, y):
#         '두 매개변수 x, y를 더해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
#         return int(x+y)
#
#     def subtract(self, x, y):
#         '두 매개변수 x, y를 빼서 결과를 실수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
#         return float(x-y)
#
#     def multiply(self, x, y):
#         '두 매개변수 x, y를 곱해서 결과를 정수형으로 반환하는 함수이다. 난이도:★☆☆☆☆'
#         return int(x*y)
#
#     def divide(self, x, y):



#         '두 매개변수 x, y를 나눠서 결과를 소수점 첫째자리에서 반올림하여 정수형으로 반환하는 함수이다. 난이도:★★☆☆☆'
#        return(x / y)
#     def expCalc(self,expStr):
#         """숫자 표현식을 문자열로 받아서 표현식에 대한 결과를 정수형으로 변환하는 함수이다. 난이도:★★★☆☆'
#         ex) expCalc('1+3-5')는 -1을 반환한다.
#         ex) expCalc('1+3*5')는 20을 반환한다.
#         ex) expCalc('1+3+5-0')는 9을 반환한다.
#         ex) expCalc('4+3+5/3')는 4을 반환한다.
#         """
#         return
#     def expCalcAdvanced(self,expStr):
#         """숫자 표현식을 문자열로 받아서(이 때 *와 / 연산자는 우선순위로 계산함, ()괄호에 대한 우선순위도 매김)표현식에
#         대한 결과를 소수점 둘째자리에서 반올림하여 실수형으로 변환하는 함수이다. 난이도:★★★★★
#         여기까지 실습시간 내에 완성하시는분은 제가 소고기 사드립니다.
#
#         ex) expCalc('1+3-5')는 -1을 반환한다.
#         ex) expCalc('1+3*5')는 16을 반환한다.
#         ex) expCalc('100+3+5-0')는 108을 반환한다.
#         ex) expCalc('(100+3)*5+300-(200+10)/2')는 710을 반환한다.
#         ex) expCalc('4+3+5/3')는 8.67을 반환한다.
#         """
#         return
#
# > > > calc = Calculator()
# > > > calc.add(1,2)
# > > > calc.subtract(3,2)
#
#



#
# from selenium import webdriver
#
# driver = webdriver.PhantomJS("/Users/RDH/Downloads/phantomjs-2.0.0-macosx/bin/phantomjs")
# driver.get("http://www.naver.com")
# driver.save_screenshot('naver.jpg')



#
#
#
#
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.PhantomJS("/Users/RDH/Downloads/phantomjs-2.0.0-macosx/bin/phantomjs")
# driver.get('http://www.naver.com')
# driver.find_element_by_id('id').send_keys('jkoon2013')
# driver.find_element_by_id('pw').send_keys('wkdsks12')
# driver.find_element_by_id('pw').send_keys(Keys.RETURN)
# driver.save_screenshot('naver_login.jpg')
#
# elements = driver.find_elements_by_tag_name('input')
# for element in elements:
#    if element.get_attribute('value') =='로그인':
#        element.click()
#        break
# driver.save_screenshot('naver_login2.jpg')
# driver.switch_to.frame('minime')
# a = driver.find_elements_by_tag_name('span')
# for b in a:
#    if b.get_attribute('class') == 'cnt':
#        print(b.text)
#






















#
#
#
#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
#
# driver=webdriver.PhantomJS("/Users/RDH/Downloads/phantomjs-2.0.0-macosx/bin/phantomjs")
# driver.get("https://www.facebook.com/")
#
# driver.find_element_by_id("email").send_keys("jkoon2013@gmail.com")
# driver.find_element_by_id('pass').send_keys("wkdsks21!!")
# #driver.save_screenshot("facebook log_in.jpg")
# driver.find_element_by_id("u_0_o").click()
# #driver.find_element_by_id("u_0_c").text("패스트캠퍼스")
# driver.find_element_by_id("q").send_keys("강진현")
# # time.sleep(5)
# # driver.save_screenshot("facebook.log_i.jpg")
#
# driver.find_element_by_class_name("searchIcon").click()
#
#
# # time.sleep(5)
# # driver.save_screenshot("facebook.log_i.jpg")
# driver.find_element_by_class_name("_5d-5").click()
# # time.sleep(5)
# # driver.save_screenshot("facebook.log_iii.jpg")
# driver.find_element_by_class_name("_45m__2vxa").send_keys("안녕진현")
# driver.find_element_by_tag_name("span").click()
# time.sleep(5)
# driver.save_screenshot("facebook.log_iii.jpg")
#
# driver.quit()


import socket
import sys
import argparse
host = "localhost"
date_payload = 2048
backlog = 5

def echo_server(port):
    """ A sumple echo server"""
    #Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Bind the socket to the port
    server_address = (host, port)
    print("Starting up echo server on %s port %s" % server_address)
    sock.bind(server_address)
    #Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog)
    while True:
        print("Waiting to receive message from client")
        client, address = sock.accept()
        date = client.recv(date_payload)
        if date:
            print("Date:%s" % date)
            client.send(date)
            print("sent %s bytes back to %s" % (date,address))
        # end connection
        client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "Socket Server Example")
    parser.add_argument('--port', action="store", dest = "port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)


import socket
import sys

import argparse

host = 'localhost'

def echo_client(port):
    """A simple echo client"""
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)

    #Send date
    try:
        #Send date
        message = "Test message. This will be echoed"
        print("Sending %s" % message)
        sock.sendall(message)
        #Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            date = sock.recv(16)
            amount_received += len(date)
            print("Received: %s" % date)
    except socket.errno:
        print("Socket error : %s" %str(socket.errno))
    except Exception:
        print("Other exception: %s" % str(Exception))
    finally:
        print("Closing connection to the server")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'Socket Server Example')
    parser.add_argument('--port', action= "store", dest="port", type=int, required= True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
    





