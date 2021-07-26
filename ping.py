import requests
import random
import time

if __name__ == '__main__':
    
    base_url = "http://127.0.0.1:8000/"
    ping_count = 0
    exc_pings = 0
    wait_pings = 0
    norm_pings = 0
    while True:
        ping_count += 1
        print(f"Total pings: {ping_count}")
        num = random.random()
        url = ""
        if num < 0.15:
            url = base_url + "definitelyworks"
            exc_pings += 1
            print(f"Pings for this url: {exc_pings}")
        elif num < 0.2:
            url = base_url + "worksfast"
            wait_pings += 1
            print(f"Pings for this url: {wait_pings}")
        else:
            url = base_url + "noproblem"
            norm_pings += 1
            print(f"Pings for this url: {norm_pings}")
            
        print("Pinging at " + url)
        res = requests.get(url)
        
        print(res)
        
        sleep_for = random.randrange(5, 10)
        
        print(f"Sleeping for {sleep_for} s\n")
        time.sleep(sleep_for)
        
        