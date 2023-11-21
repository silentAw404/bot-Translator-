from requests import get, post,options,delete
from os.path import exists
from os import system
from time import sleep
from json import dumps

B_red="\033[1;31m"
B_green="\033[1;32m"
B_purple="\033[1;34m"
D_off="\033[0m"

class Liara ():

    def __init__(self, app_name):
        self.app_name = app_name

        if not exists(f"{app_name}.json"):    
            self.email = input(B_purple+"Enter Your Email : ")
            self.password = input(B_purple+"Enter Your Password : ")

            # Login TO Account
            try:
                self.api_token = post("https://api.iran.liara.ir/v1/login", json={"email": self.email, "password": self.password}).json()['api_token']
                
                with open(f"{app_name}.json","wb") as file:
                    file.write(dumps({"api_token":self.api_token}).encode('utf-8'))
                
                print(B_green+"Login successfully")
                sleep(3)
                system("clear")

            except:
                print(B_red+"ERROR In Login")
                exit()
        else:
            with open(f"{app_name}.json","r") as file:
                self.api_token = eval(file.read())['api_token']
                

    @staticmethod
    def _sendRequest(self,url: str,option : int = None, data: dict = None):

        header = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,fa;q=0.6',
            'Authorization': f"Bearer {self.api_token}",
            'If-None-Match': 'W/"177-eBIRLwNKEIVW/xRxStiDEmuoT/A"',
            'Origin': 'https://console.liara.ir',
            'Referer': 'https://console.liara.ir/',
            'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        
        if option == 1:
            return post(url, json=data, headers=header)
        elif option == 2:
            return get(url, headers=header).json()
        elif option == 3:
            return delete(url,headers=header)
        elif option == 4:
            return options(url,headers=header).text


    # خاموش کردن برنامه
    def OffService(self, service_name : str):
        self._sendRequest(self,f"https://api.iran.liara.ir/v1/projects/{service_name}/actions/scale",1, {'scale': '0'})

    # روشن کردن برنامه
    def OnService(self, service_name : str):
        self._sendRequest(self,f"https://api.iran.liara.ir/v1/projects/{service_name}/actions/scale",1, {'scale': '1'})

    # دریافت برنامه ها
    def getServices(self):
        return self._sendRequest(self,"https://api.iran.liara.ir/v1/projects",2)

    # ری استارت کردن سرویس
    def restartService(self, service_name : str):
        self.OffService(service_name)
        self.OnService(service_name)

    # پاک کردن سرویس
    def deleteService(self,service_name : str):
        self._sendRequest(self,f"https://api.iran.liara.ir/v1/projects/{service_name}",3)

    # دریافت اطلاعات لحظه ای
    def getProcess(self, service_name : str):
        return self._sendRequest(self,f"https://api.iran.liara.ir/v1/projects/{service_name}/metrics/summary",2)
    
    # دریافت سرویس ها
    def getServiceCount(self):
        return self._sendRequest(self,"https://api.iran.liara.ir/v1/service-count",2)
    
    # دریافت اطلاعات شخصی
    def getMe(self):
        return self._sendRequest(self,"https://api.iran.liara.ir/v1/me",2)
    
    # دریافت موجودی
    def getBalance(self):
        return self.getMe()['user']['balance']
        
        