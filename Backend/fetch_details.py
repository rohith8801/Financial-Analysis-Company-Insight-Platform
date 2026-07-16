import requests

API_URL = "https://bluemutualfund.in/server/api/company.php"
API_KEY = "ghfkffu6378382826hhdjgk"

def fetch_company_data(company_id):
    params = {
        "id": company_id,
        "api_key": API_KEY
    }

    response = requests.get(API_URL, params=params)

    print("\n==============================")
    print("REQUESTED COMPANY ID:", company_id)
    print("FINAL URL:", response.url)
    print("STATUS CODE:", response.status_code)
    print("RESPONSE LENGTH:", len(response.text))
    print("==============================\n")

    return response.text
