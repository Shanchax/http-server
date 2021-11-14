import sys
import os
import requests
import random
import threading
import unittest

class test_07(unittest.TestCase):
    
    def runTest(self):
        

        print("\nSending {} PUT Request Threads".format(client_Threads))
        puturl = "http://127.0.0.1:8888" + str(os.getcwd()) + "/put.txt"
        request_threads = []
        try:
            def put_test(fileno):
                data = dict(
                    key1='new',
                    value1='put'
                )
                try:
                    r = requests.put(puturl ,
                        data=data
                    )
                    print(f"Status : {r.status_code} {r.reason}")
                except:
                    print("Error in making request, maybe server queue is full")
            
            
            for i in range(client_Threads):
                t = threading.Thread(target=put_test, args=(i+1,))
                request_threads.append(t)
                t.start()

            # Wait until all of the threads are complete
            for thread in request_threads:
                thread.join()
            
        except Exception as ex:
            print('Ooops , something seems out of place ;-;!', ex)
        finally:
            # Stop all running threads
            return

class test_08(unittest.TestCase):
    
    def runTest(self):
        

        print("\nSending{} POST Request Threads".format(client_Threads))
        posturl = "http://127.0.0.1:8888" + str(os.getcwd()) + "/post.txt"
        request_threads = []
        try:
            def put_test(fileno):
                data = dict(
                    key='new',
                    value='put'
                )
                try:
                    r = requests.post(posturl ,
                        data=data,

                    )
                    print(f"Status : {r.status_code} {r.reason}")
                except:
                    print("Error in making request, maybe server queue is full")
            
            
            for i in range(client_Threads):
                t = threading.Thread(target=put_test, args=(i+1,))
                request_threads.append(t)
                t.start()

            # Wait until all of the threads are complete
            for thread in request_threads:
                thread.join()
            
        except Exception as ex:
            print('Ooops , something seems out of place ;-;!', ex)
        finally:
            # Stop all running threads
            return

class test_09(unittest.TestCase):
    
    def runTest(self):
        

        print("\n Sending {} DELETE Request Threads".format(client_Threads))
        posturl = "http://127.0.0.1:8888" + str(os.getcwd()) 
        request_threads = []
        try:
            def put_test(fileno):
                data = dict(
                    key='new',
                    value='put'
                )
                try:
                    r = requests.delete(posturl + "delete{}.txt".format(fileno) ,
                        data=data,

                    )
                    print(f"Status : {r.status_code} {r.reason}")
                except:
                    print("Error in making request, maybe server queue is full")
            
            
            for i in range(client_Threads):
                t = threading.Thread(target=put_test, args=(i+1,))
                request_threads.append(t)
                t.start()

            # Wait until all of the threads are complete
            for thread in request_threads:
                thread.join()
            
        except Exception as ex:
            print('Ooops , something seems out of place ;-;!', ex)
        finally:
            # Stop all running threads
            return



if __name__ == "__main__":
    

    client_Threads = 3
    unittest.main(verbosity=2)
