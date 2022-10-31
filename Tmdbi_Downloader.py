import requests
from imdb import Cinemagoer
from keys import  TMDBI_KEY

class tmdbi_download():
    def __init__(self,movie_name):
        self.movie_name = movie_name
        self.base_url = 'http://d3gtl9l2a4fn1j.cloudfront.net/t/p/'
        self.max_size = "original"
        self.url = ''
        self.rel_path = ''
        self.movie_id = ''
        self.IMG_PATTERN ='http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'

      # search the id of movie from imdb.
    # then set it with to tt to search on tmdb
    def __id_imdb__(self):
        ia = Cinemagoer()
        movies = ia.search_movie(self.movie_name)
        self.movie_id = "tt"+movies[0].movieID
        return self.movie_id

    # search from tmdb the file path
    def __get__movie__file_path__(self):
        api_request = requests.get(self.IMG_PATTERN.format(key=TMDBI_KEY,imdbid=self.movie_id))
        api_response = api_request.json()
        posters = api_response['posters']
        first_poster = posters[0]
        self.rel_path = first_poster["file_path"]
        return self.rel_path

    # set the url =  <base_url> + <max_size> + <rel_path>
    def __set__movie_poster_url__(self):
        self.url = "{0}{1}{2}".format(self.base_url, self.max_size, self.rel_path)
        return self.url
    def __download_movie_poster__(self):
        r = requests.get(self.url)
        filetype = r.headers['content-type'].split('/')[-1]
        filename = 'poster_{0}.{1}'.format(self.movie_name, filetype)
        with open(filename, 'wb') as w:
            w.write(r.content)


new_movie = tmdbi_download("spiderman")
new_movie.__id_imdb__()
new_movie.__get__movie__file_path__()
new_movie.__set__movie_poster_url__()
new_movie.__download_movie_poster__()
