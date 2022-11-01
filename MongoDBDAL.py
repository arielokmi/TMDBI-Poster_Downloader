import pymongo
import  gridfs

class MongoDb:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.client["mydatabase"]
        self.myfs =  gridfs.GridFS(self.mydb)
        self.mycol = self.mydb["fs.files"]
        self.id = "63468a36bd6a34742c3b365e"

    def __read_image__(self,moviename):
        image_file = self.mycol.find_one( {"moviename" : moviename})
        return image_file
         # for document in id_movie:
         #   print(document)
          #print(id_movie.get('__id'))

    def __write_image__(self,file,movie_name,movie_id):
        # Open the image in read-only format.
        with open(file, 'rb') as f:
            contents = f.read()
        # Now store/put the image via GridFs object.
        self.myfs.put(contents, moviename=movie_name,movieid=movie_id)

 #   def __insert_image__(self,**insert_dict):
        # need to convert picture to binary
        #we need to learn gred0
   #     self.mycol.insert_one(insert_dict)

    def __update_image__(self,moviename,key_to_update,val_to_update):
          self.mycol.update_many( {"moviename" : moviename},{"$set":{key_to_update : val_to_update}})



    def __delete_image__(self,moviename):
        print(moviename)
        image_id = self.mycol.find_one({"moviename": moviename})["_id"]
        print(image_id)
        self.myfs.delete(image_id)
        return moviename


#if __name__ == '__main__':

    #new_data = MongoDb()
    #new_data.write_image("test.jfif","spiderman", "tt0145487")
    #new_data.read_image("spiderman")

    #mdb = MongoDBDAL("localhost", 27017, "movies")

    #mdb.write_image_file(config.content_temp_path + "poster_star wars.jpeg", "spiderman", "tt0145487")
    #mdb.read_image_file("star wars")
    #mdb.del_image_file("spiderman")
