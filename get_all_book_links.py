import requests
from bs4 import BeautifulSoup

def get_all_book_links(total_pages: int) -> list:

    cookies = {
        'ccsid': '577-8436894-7675609',
        '__qca': 'P0-453162199-1728591063416',
        'csm-sid': '110-8430706-6566999',
        'logged_out_browsing_page_count': '2',
        'ubid-main': '134-8252618-0657059',
        'lc-main': 'en_US',
        'srb_10': '1_wl',
        '_session_id2': '609671ad4bd2d992705d3c2388888fb7',
        'allow_behavioral_targeting': 'true',
        'session-id': '135-0370233-2675602',
        'csm-hit': 'tb:s-8Q61DVY5Q18SNQEXR734|1731590280130&t:1731590280130',
        'JSESSIONID': 'A67F52732EC5A12B83B7A7923DADC433',
        'session-id-time': '2362310311l',
        'session-token': '"MKcwR3dhahVvffrUPLm+j3aWG03W/5CWlNQgRKyaafk4q9ZaweKaAUt3axy7p0XB/cTaa/hxk162qPFj+XaB9Q1UYyJ97FAxtf5sJa+7LcIqqhUkmYkANr3zvpaT+/0CnJR7fb6tVZ+OT1lHiphKWHQmrVrNVr+zIB8Qal8SHDvWZQ7uG1JIN4adJqugvkEjpLwk34H8s4ML6H6vKmse+RslApsrWz5vQMM0/LJnl8qhVlruSHsir8vGQt4BFrY3Cfx8m7UgMJe2T1Y/gp1EWN6Y6UsjHJPmtU9Frpbah12svFfA3OyuX0L++eDUkT0wwhqXYqAXO1xP5vU+gw+T8q4oaH1etUVkVM4rbSJTk2KjgltGDbUiMw=="',
        'x-main': '"3?rWlMOrrhOPKHoAjSRl4JvzfhtXpxvSafg0ZL1mqZznDonnQeJPXtM@idDNHCSK"',
        'at-main': 'Atza|IwEBIJ0SpyiNT7PWAUBfBRP71W0B1HfwW8ldTpbcOp9zoF7ym9VoVJxmI_y6_p3BVY52drvGEQ0wrCGrv8R79cznkjmLH7EacBWXT8N2cQehZ_rrSybHb_U1VOIny_koahXD2MbuVZFIKqXb3wNchBQ6jwYPmLXXzjLr_Or7buh1Od5qUXcZ4_YwMxk88qTPz9y5rdsSMzjuBeG5fzYtjXGVdd8HpwK75lN0f1l3NTf5_0uqY8AEMDwNZZ6mtCs3TYFxbNo',
        'sess-at-main': '"gik+UXcfPNtcqpJned438JTgKe3wcVMnEdMu8L/5kMA="',
        'locale': 'en',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'fr-FR,fr;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'ccsid=577-8436894-7675609; __qca=P0-453162199-1728591063416; csm-sid=110-8430706-6566999; logged_out_browsing_page_count=2; ubid-main=134-8252618-0657059; lc-main=en_US; srb_10=1_wl; _session_id2=609671ad4bd2d992705d3c2388888fb7; allow_behavioral_targeting=true; session-id=135-0370233-2675602; csm-hit=tb:s-8Q61DVY5Q18SNQEXR734|1731590280130&t:1731590280130; JSESSIONID=A67F52732EC5A12B83B7A7923DADC433; session-id-time=2362310311l; session-token="MKcwR3dhahVvffrUPLm+j3aWG03W/5CWlNQgRKyaafk4q9ZaweKaAUt3axy7p0XB/cTaa/hxk162qPFj+XaB9Q1UYyJ97FAxtf5sJa+7LcIqqhUkmYkANr3zvpaT+/0CnJR7fb6tVZ+OT1lHiphKWHQmrVrNVr+zIB8Qal8SHDvWZQ7uG1JIN4adJqugvkEjpLwk34H8s4ML6H6vKmse+RslApsrWz5vQMM0/LJnl8qhVlruSHsir8vGQt4BFrY3Cfx8m7UgMJe2T1Y/gp1EWN6Y6UsjHJPmtU9Frpbah12svFfA3OyuX0L++eDUkT0wwhqXYqAXO1xP5vU+gw+T8q4oaH1etUVkVM4rbSJTk2KjgltGDbUiMw=="; x-main="3?rWlMOrrhOPKHoAjSRl4JvzfhtXpxvSafg0ZL1mqZznDonnQeJPXtM@idDNHCSK"; at-main=Atza|IwEBIJ0SpyiNT7PWAUBfBRP71W0B1HfwW8ldTpbcOp9zoF7ym9VoVJxmI_y6_p3BVY52drvGEQ0wrCGrv8R79cznkjmLH7EacBWXT8N2cQehZ_rrSybHb_U1VOIny_koahXD2MbuVZFIKqXb3wNchBQ6jwYPmLXXzjLr_Or7buh1Od5qUXcZ4_YwMxk88qTPz9y5rdsSMzjuBeG5fzYtjXGVdd8HpwK75lN0f1l3NTf5_0uqY8AEMDwNZZ6mtCs3TYFxbNo; sess-at-main="gik+UXcfPNtcqpJned438JTgKe3wcVMnEdMu8L/5kMA="; locale=en',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }


    links = []
    MAX_RETRIES = 5

    for page in range(1, total_pages + 1):
        params = {
            'page': page,
        }
        success = False
        retry = 0
        while not success and retry < MAX_RETRIES:
            try:
                response = requests.get('https://www.goodreads.com/shelf/show/classics', headers=headers, cookies=cookies, params=params, timeout=3)
                response.raise_for_status()
                success = True
                html_content = response.content
                soup = BeautifulSoup(html_content, 'html.parser')

                book_containers = soup.find_all("div", class_="elementList")
                for container in book_containers:
                    book_link = container.find("a", class_="bookTitle")
                    if book_link:
                        href = book_link.get("href")
                        if href and not href.startswith('http'):
                            link = "https://www.goodreads.com" + href
                            links.append(link)
                            print(f"Added link: {link}")

            except requests.Timeout:
                success = False
                print(f"Timeout occurred on page {page}")   
            except Exception as e:
                success = False
                print(f"An error occurred on page {page}: {e}")
            retry += 1

    print(f"Total links collected: {len(links)}")
    return links
