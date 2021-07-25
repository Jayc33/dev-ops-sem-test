import requests
import random
import time

if __name__ == '__main__':
    
    base_url = "http://127.0.0.1:8000/"
    while True:
        num = random.random()
        print(num)
        url = ""
        if num < 0.1:
            url = base_url + "definitelyworks"
        elif num < 0.3:
            url = base_url + "worksfast"
        else:
            url = base_url + "noproblem"
            
        print("Pinging at " + url + "\n")
        res = requests.get(url)
        
        print(res)
        
        sleep_for = random.randrange(5, 15)
        
        print(f"Sleeping for {sleep_for} s\n")
        time.sleep(sleep_for)
        
        