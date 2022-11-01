import keys
import requests
import imdb
import os
class tmdbi_downloder:

    def __init__(self,title):
        self.title = title
        self.api_response = None
        self.Config_Pattern = 'http://api.themoviedb.org/3/configuration?api_key={key}'
        self.KEY =keys.TMDBI_KEY
        self.url = self.Config_Pattern.format(key=self.KEY)
        self.r = requests.get(self.url)
        self.config = self.r.json()
        self.base_url = self.config['images']['secure_base_url']
        self.sizes = self.config['images']['poster_sizes']
        self.max_size = 'original'
        self.IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'



    def __get_imbid__(self):
        ia = imdb.IMDb()
        search = ia.search_movie(self.title)
        self.imdb_id = "tt" + str(search[0].movieID)
        r = requests.get(self.IMG_PATTERN.format(key=self.KEY, imdbid=self.imdb_id))
        self.api_response = r.json()
        return self.api_response

    def __poster_download__(self):
        posters = self.api_response['posters']
        self.poster_urls = []
        for poster in posters:
            rel_path = poster['file_path']
            self.url = "{0}{1}{2}".format(self.base_url, self.max_size, rel_path)
            self.poster_urls.append(self.url)
        return self.poster_urls

    def __save_to__(self):
        r = requests.get(self.poster_urls[0])
        filetype = r.headers['content-type'].split('/')[-1]
        filename = '{0}.{1}'.format(self.title, filetype)
        filepath = os.path.join('.', filename)
        with open(filepath, 'wb') as w:
            w.write(r.content)



new_movie = tmdbi_downloder("spiderman")
new_movie.__get_imbid__()
new_movie. __poster_download__()
new_movie.__save_to__()