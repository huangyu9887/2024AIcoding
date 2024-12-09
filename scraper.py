import requests
from bs4 import BeautifulSoup

def get_motorola_models():
    url = "https://www.gsmarena.com/motorola-phones-4.php"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    models = []
    phone_list = soup.find_all('div', class_='makers')
    
    if phone_list:
        for phone in phone_list[0].find_all('li'):
            model_name = phone.find('span').text.strip()
            model_link = phone.find('a')['href']
            models.append((model_name, "https://www.gsmarena.com/" + model_link))
    
    return models

def main():
    motorola_models = get_motorola_models()
    if motorola_models:
        print("List of Motorola:")
        for i, (name, link) in enumerate(motorola_models, 1):
            print("{}. {}".format(i, name))
            print("   Link: {}".format(link))
    else:
        print("Can't find Motorola Phonepy")

if __name__ == "__main__":
    main() 