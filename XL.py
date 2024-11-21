import requests

number = input("NUMBER: ")
with open('nik.txt', 'r') as file:
    for line in file:
        NIK, KK = line.strip().split('|')
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer Ln9YN5trk3UUGHnHXoV8644+QEDWRf8qpLJ0tovzrhQVRjJKzRulyHxNIa8eos0pH7iNIePuPNOxNmY4sRnHZIPEPD7iKAX2Z8Z2qOucrAQ+h6Z98l7GQEoIrDwRTXAD7nLAyRnH9dVwzmidCPSH9dwWBE31I739FGTNKJdqB44tShoH6VUKbX3LMBfkEZROdHYk9EIJ9XEjLEWWRpL41G/iTXxEHPUaM6Q8zBfyAVVrYPKEi+FSopBoSpM1+V4WkXSHV70nXqOeB3jEF9a7GWuuxh4eMOMvF7YFGtw2D+Ptz0BrBDYFd66x4km2mC7SBcyOUfjjWXYGSTWwHpvgIQ==',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://www.xlaxiata.co.id',
            'priority': 'u=1, i',
            'referer': 'https://www.xlaxiata.co.id/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }
        response_otp_request = requests.post('https://jupiter-ms-webprereg.xlaxiata.id/request-otp', headers=headers, json={ "msisdn": number })
        OTP = input(f"NIK: {NIK} KK: {KK} OTP: ")
        response_otp_verification = requests.post('https://jupiter-ms-webprereg.xlaxiata.id/submit-registration-otp-non-biometric', headers=headers, json={ "msisdn": number, "nik": NIK, "kk": KK, "otpCode": OTP })
        try:
            if 'Success' in response_otp_verification.json():
                print(f"{number} SUCCESSFULLY REGISTERED")
                break
            else: print(f"{NIK} CAN'T BE USED TO REGISTER")
        except: pass
