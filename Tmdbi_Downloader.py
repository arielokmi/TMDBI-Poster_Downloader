from imdb import Cinemagoer

class tmdbi_download():
    def __init__(self):
        pass
    def __id_mdbi__(self,movie_name):
        ia = Cinemagoer()
        movies = ia.search_movie(movie_name)
        print(movies[0])
        return movie_name
    


new_movie = tmdbi_download()
new_movie.__id_mdbi__("spiderman")

