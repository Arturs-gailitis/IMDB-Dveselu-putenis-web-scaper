import requests
from bs4 import BeautifulSoup


# URL of the IMDb page to scrape
URL = 'https://www.imdb.com/title/tt6084202/'

# Headers to mimic a request from a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

# Sending a GET request to the URL and parsing the HTML content
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Extracting the director from the page
director_section = soup.find('a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link', href=True)
if director_section:
    director = director_section.text.strip()

# Extracting the writers from the page
writter_section = soup.find_all('a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link', )
if writter_section:
    writter = writter_section[1].text.strip()
    writter1 = writter_section[2].text.strip()

# Extracting the actors from the page
actor_section = soup.find_all('div', class_='ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid')
if actor_section:
    actor = actor_section[0].text.strip()
    actor_parts = actor.split(maxsplit=21) 

    if len(actor_parts) >= 22:
        actor_part1 = actor_parts[0]
        actor_part2 = actor_parts[1]
        actor_part3 = actor_parts[2]
        actor_part4 = actor_parts[3]
        actor_part5 = actor_parts[4]
        actor_part6 = actor_parts[5]
        actor_part7 = actor_parts[6]
        actor_part8 = actor_parts[7]
        actor_part9 = actor_parts[8]
        actor_part10 = actor_parts[9]
        actor_part11 = actor_parts[10]
        actor_part12 = actor_parts[11]
        actor_part13 = actor_parts[12]
        actor_part14 = actor_parts[13]
        actor_part15 = actor_parts[14]
        actor_part16 = actor_parts[15]
        actor_part17 = actor_parts[16]
        actor_part18 = actor_parts[17]
        actor_part19 = actor_parts[18]
        actor_part20 = actor_parts[19]
        actor_part21 = actor_parts[20]
        actor_part22 = actor_parts[21]

    actor1 = actor_part1 + actor_part2
    actor_1 = actor[:14]
    actor2 = actor_part3[6:] + ' ' + actor_part4[:7]
    actor3 = actor_part4[12:] + ' ' + actor_part5[:7]
    actor4 = actor_part5[13:] + ' ' + actor_part6[:7]
    actor5 = actor_part6[13:] + ' ' + actor_part7[:5]
    actor6 = actor_part8[6:] + ' ' + actor_part9[:6]
    actor7 = actor_part9[15:] + ' ' + actor_part10 [:4]
    actor8 = actor_part10[11:] + ' ' + actor_part11[:7]
    actor9 = actor_part11[13:] + ' ' + actor_part12[:8]
    actor10 = actor_part13[4:] + ' ' + actor_part14[:8]
    actor11  = actor_part14[14:] + ' ' + actor_part15[:4] 
    actor12 = actor_part15[7:] + ' ' + actor_part16[:4]
    actor13 = actor_part16[8:] + ' ' + actor_part17[:9]
    actor14 = actor_part17[16:] + ' ' + actor_part18[:5]
    actor15 = actor_part18[10:] + ' ' + actor_part19[:5]
    actor16 = actor_part19[14:] + ' ' + actor_part20[:6]
    actor17 = actor_part20[6:] + ' ' + actor_part21[:10]
    actor18 = actor_part21[10:] + ' ' + actor_part22

# Extracting the awards and nominations
award_section = soup.find('span', class_="ipc-metadata-list-item__list-content-item")
for award in award_section:
    if "9 wins" in award.text:
        wins_nominations = award.text.strip()

# Printing out the extracted information
print(f"Director: {director}")
print(f"Writters: {writter}, {writter1}")
print(f'Actors: {actor_1}, {actor2}, {actor3}, {actor4}, {actor5}, {actor6}, {actor7}, {actor8}, {actor9}, {actor10}, {actor11}, {actor12}, {actor13}, {actor14}, {actor15}, {actor16}, {actor17}, {actor18}')
print(f'Awards: {wins_nominations}')