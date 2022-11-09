<div align="center">  
  <h1> TMDBI-Poser Downloader</h1>
</div>


## About 
  web application based on flask writting in python.<br/>
  give you option to search poster of movie for your choice from your mongodb.<br/>
  also you can do crud actions from mongodb include:create,update,read and delete using simple api routeing.<br/>
  and it build as :whale: docker image so it ready to use.<br/> 
 
 ## Future
 * :rocket: based on flask writting in python.
 * :rocket: using with object-oriented programming and using class method.
 * :rocket: using mongoDb and using Gridfs solution.
 
## Installation
   1. first clone the project to your text editor.
      ```
      git clone https://github.com/arielokmi/TMDBI-Poster_Downloader.git
      ```
   2. download and update the necessary plugins for the project
      ```
      apt update
      ```
   3. build the docker imgae using:
      ```
      docker build . -t app:latest
      ```
   4. run the docker.compose file:
   
      ```
      docker-compose -f docker_compose.yaml up
      ```
   5. now you can access the website:
      ```
      localhost:5001
      ```
 ## Use case:
 ###  Search:
      ```
      '/search/<movie_name>'
      ```
 
