import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent  # Make sure to install this library

def get_ticket_info(url):
    ua = UserAgent()
    headers = {"User-Agent": ua.random}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        html_text = response.text
        soup = BeautifulSoup(html_text, "html.parser")

        a_tags = soup.find_all("span", {"class": "btn-item"})

        ticket_info_list = []
        for tag in a_tags:
            onclick = tag.a["onclick"]
            onclick = onclick.split("$app.popup.signin('https://booking.thaiticketmajor.com/booking/3m/zones.php?query=")[1]
            onclick = onclick.split("');")[0]
            onclick = onclick.split("&rdId=")

            # Assuming you want to store the extracted information in a list
            ticket_info_list.append({
                "query": onclick[0],
                "rdId": onclick[1]
            })

        return ticket_info_list

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Example usage
url = "https://www.thaiticketmajor.com/concert/bruno-mars-live-in-bangkok.html"
ticket_info = get_ticket_info(url)

if ticket_info:
    print(ticket_info)