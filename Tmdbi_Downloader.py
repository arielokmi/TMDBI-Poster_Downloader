import requests
from imdb import Cinemagoer
from keys import  TMDBI_KEY

class tmdbi_download():
    def __init__(self):
        self.max_size = "original"
        self.IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
    def __id_imdb__(self,movie_name):
        ia = Cinemagoer()
        movies = ia.search_movie(movie_name)
        print(movies[0])
        return movie_name
    def __get__movie__file_path__(self):
        format_url = requests.get(self.IMG_PATTERN.format(key=TMDBI_KEY,imdbid='tt0095016'))
        api_response = format_url.json()
        posters = api_response['posters']
        first_poster = posters[0]
        file_path = first_poster["file_path"]
        print (file_path)
        return file_path




new_movie = tmdbi_download()
new_movie.__id_imdb__("spiderman")
new_movie.__get__movie__urls__()

