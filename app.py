import codecs
import json
from flask import Flask, request, render_template, Response
from MongoDBDAL import MongoDb
from Tmdbi_Downloader import  tmdbi_downloder
import os



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = Flask(__name__)
    connect = MongoDb()

    @app.route('/')
    def index():
        return render_template('website.html')

    @app.route('/search', methods=["GET","POST"])
    def search():
          if request.method == "POST":
              moviename = request.form.get("name")
              movie_data = connect.__read_image__(moviename)
              if movie_data is None:
                  print("movie was not found in db")
                  new_movie = tmdbi_downloder(moviename)
                  new_movie.__get_imbid__()
                  new_movie.__poster_download__()
                  connect.__write_image__( moviename +".jpeg",moviename,'tt0145487')
                  return render_template('website.html')

              else:
                  if movie_data["moviename"] == moviename:
                      print("the movie found found in mongo db")
          return render_template('website.html')


    @app.route('/update/<movie_name>/<key_value>/<update_value>', methods=["GET"])
    def update(movie_name,key_value,update_value):
        if request.method == "GET":
            movie_data = connect.__read_image__(movie_name)
            update_movie_data = connect.__update_image__(movie_name,key_value,update_value)
            if movie_data is None:
                print("movie was not found in db")
        print(update_value)
        return render_template('website.html')


    @app.route('/delete/<movie_name>/', methods=["GET"])
    def delete(movie_name):
        if request.method == "GET":
            movie_data = connect.__read_image__(movie_name)
            movie_delete = connect.__delete_image__(movie_name)
            if movie_data is None:
                print("movie was not found in db")
        print(movie_name)
        render_template('website.html')








    app.run(host='0.0.0.0', port=5001)
