import requests, re

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
    try: 
        header = {
            'Referer': 'https://www.xlaxiata.co.id/registrasi', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"macOS"',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        }
        bear = re.search(r'concat\("([^"]+)"\)', requests.get('https://www.xlaxiata.co.id/registrasi/_next/static/chunks/pages/regbypuk/regbypukform-b0a844f3483c094b.js', headers=header).text.strip()).group(1)
    except: bear = "VzNicHIzR24wbjEzaW8yMDI0OmJ5ZHQybzI0KiE="
    try: return requests.post('https://jupiter-ms-webprereg.xlaxiata.id/generate-jwt', headers=headers(bear)).json()['encryptToken']
    except: return "Ln9YN5trk3UUGHnHXoV8644+QEDWRf8qpLJ0tovzrhQVRjJKzRulyHxNIa8eos0pH7iNIePuPNOxNmY4sRnHZIPEPD7iKAX2Z8Z2qOucrAQ+h6Z98l7GQEoIrDwRTXAD7nLAyRnH9dVwzmidCPSH9dwWBE31I739FGTNKJdqB44Ieq3PIs1y1ay6eZgmNBY84QrE22qRYOzUFWX/68cCNwFoJJdf0BdZeKclWxJAasfLAHR1bnM5V8VkNiC+CZlWe08UiEGaltTDcp2hoLGsaYshcy48PIefK3WseHwQn1SvSERWWNbHO0F70RLz7V0CXOg222YN7LQdwhm2Nv1tiw=="

token, number = bearer(), input("NUMBER: ")
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
