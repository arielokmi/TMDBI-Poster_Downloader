import json
from flask import Flask, request, render_template, Response
from MongoDBDAL import MongoDb
from Tmdbi_Downloader import  tmdbi_downloder



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
              print(movie_data)
              if movie_data is None:
                  print("movie was not found in db")
                  new_movie = tmdbi_downloder(moviename)
                  new_movie.__get_imbid__()
                  new_movie.__poster_download__()
                  new_movie.__save_To__()
                  connect.write_image( moviename +".jpeg",moviename,'tt0145487')
              else:
                  if movie_data["moviename"] == moviename:
                      print("the movie found found in mongo db")

          return render_template('website.html')



    app.run(debug=True)
