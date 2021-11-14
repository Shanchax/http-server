import sys
import os
import requests
import random
import threading
import unittest
# from server import httpServer

 

class test_01(unittest.TestCase):
    def runTest(self):
        geturl = "http://127.0.0.1:8888/"     
        print("Testing GET")
        try:
            headers = {
                'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                'Accept-Encoding': 'gzip;q=1.0,br;q=0.7',
                'Accept': '/',
                'Connection': 'keep-alive'
                'If-Modified Since : Wed, 21 Oct 2015 07:28:00 GMT'

            }
            r = requests.get(geturl , headers = headers)
            # print(f"Status : {r.status_code} {r.reason}")
            # print("Headers:", r.headers)
            if(r.status_code == 200):
                print('\n\nSuccesss!!', r.status_code)
        except Exception as ex:
            print('\n\nOops something is not working\n\n', ex)
            print(os.getcwd())
        finally:
            # Stop all running threads
            return


class test_02(unittest.TestCase):
    def runTest(self):
        geturl = "http://127.0.0.1:8888" + str(os.getcwd()) + "/http.log"    
        print("Testing HEAD")
        try:
            headers = {
                'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                'Accept-Encoding': 'gzip;q=1.0,br;q=0.7',
                'Accept': '/',
                'Connection': 'keep-alive'
            }
            r = requests.head(geturl , headers = headers)
            # print(f"Status : {r.status_code} {r.reason}")
            if(r.status_code == 200):
                print('\n\nSuccess!!!', r.status_code)
        except Exception as ex:
            print('\n\nOoops, something is wrong', ex)
            print(os.getcwd())
        finally:
            # Stop all running threads
            return

class test_03(unittest.TestCase):
    def runTest(self):
        geturl = "http://127.0.0.1:8888" + str(os.getcwd()) + "/http.log"    
        print("Testing normal get request")
        try:
            headers = {
                'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                'Accept-Encoding': 'gzip;q=1.0,br;q=0.7',
                'Accept': '/',
                'Connection': 'keep-alive'
            }
            r = requests.post(geturl , headers = headers)
            # print(f"Status : {r.status_code} {r.reason}")
            # print("Headers:", r.headers)
            if(r.status_code == 200):
                print('\n\nGET TEST-01 PASS', r.status_code)
        except Exception as ex:
            print('\n\nGET TEST-01 FAIL', ex)
            print(os.getcwd())
        finally:
            # Stop all running threads
            return


class test_03(unittest.TestCase):
    
    def runTest(self):
        posturl = "http://127.0.0.1:8888" + str(os.getcwd()) + "/post.txt"
        try:
            print("\nTesting POST")
            data = dict(
                key1='data',
                value1='value'
            )

            # headers = {'content-type': 'text/html'}
            r = requests.post(posturl,
                data=data,
                 
            )
            print(f"Status : {r.status_code} {r.reason}")
            
        except Exception as ex:
            print('Oops, something is wrong!', ex)
        finally:
            return


class test_04(unittest.TestCase):
    
    def runTest(self):
        posturl = "http://127.0.0.1:8888" + str(os.getcwd()) + "/put.txt"
        try:
            print("\nTesting PUT")
            data = dict(
                key1='data',
                value1='value'
            )

            headers = {'content-type': 'text/html' , 'If-Match' : "bfc13a64729c4290ef5b2c2730249c88ca92d82d"}
            r = requests.put(posturl,
                data=data,
                 headers=headers
            )
            print(f"Status : {r.status_code} {r.reason}")
        except Exception as ex:
            print('Oops, something is wrong!', ex)
        finally:
            return
class test_05(unittest.TestCase):
    
    def runTest(self):
        posturl = "http://127.0.0.1:8888" + str(os.getcwd()) + "/post.txt"
        try:
            print("\nTesting PUT")
            data = dict(
                key='data',
                value='value'
            )

            headers = {'content-type': 'text/html'}
            r = requests.put(posturl,
                data=data,
                 headers=headers
            )
            print(f"Status : {r.status_code} {r.reason}")
            print("Headers:", r.headers)
        except Exception as ex:
            print('Something went horribly wrong!', ex)
        finally:
            return

class test_06(unittest.TestCase):
    
    def runTest(self):
        delurl = "http://127.0.0.1:8888" + str(os.getcwd()) + "/output.csv"

        print("\nTesting DELETE")
        try:
             
            r = requests.delete(delurl)
            print(f"Status code : {r.status_code} {r.reason}")
        except Exception as ex:
            print('Oops, something is wrong', ex)
        finally:
            return




if __name__ == "__main__":
    

    n_clientThreads = 4
    unittest.main()