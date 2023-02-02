from bs4 import BeautifulSoup
import requests as req

res = req.get('https://www.billboard.com/charts/hot-100/')

hot_100_page = res.text

soup = BeautifulSoup(hot_100_page, 'html.parser')

# Getting all song titles
song_titles_parsed = soup.select('li .c-title')

# Get all artist
song_artists_parsed = soup.find_all(name='span', class_='a-no-trucate')

# Cleaning up the song titles into a list
song_titles = [song.getText().strip() for song in song_titles_parsed]
song_artists = [artist.getText().strip() for artist in song_artists_parsed]

for i in range(0, 100):
    print(f'{i+1}. {song_titles[i]} - {song_artists[i]}')