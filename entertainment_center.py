import media
import fresh_tomatoes

"""
declare favorite movies, with 3 args each:
title (movie title)
poster_url (url to poster image)
trailer_url (url to youtube trailer)
"""

interstellar = media.Movie(
    "interstellar",
    "http://bit.ly/interstellarPoster",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

beautiful_mind = media.Movie (
    "A Beautiful Mind",
    "http://bit.ly/BeautifulMindPoster",
    "https://www.youtube.com/watch?v=WFJgUm7iOKw")                          
                           
matrix = media.Movie (
    "Matrix ",
     "http://bit.ly/MatrixPoster",
     "https://www.youtube.com/watch?v=vKQi3bBA1y8") 

shawshank_Redemption = media.Movie(
    "The Shawshank Redemption",
    "http://bit.ly/TheShawshankRedemptionPoster",
    "https://www.youtube.com/watch?v=6hB3S9bIaco")                     
                      
silence_of_the_Lambs = media.Movie(
    "The Silence of the Lambs",
    "http://bit.ly/TheSilenceOfTheLambsPoster",
    "https://www.youtube.com/watch?v=ZWCAf-xLV2k") 
    
swordfish = media.Movie (
    "Swordfish ",
    "http://bit.ly/SwordfishPoster",
    "https://www.youtube.com/watch?v=dPE9tHhII5U")                                    
                                                                                  
                           
movies = [interstellar, beautiful_mind, matrix, shawshank_Redemption, 
     silence_of_the_Lambs, swordfish ] 
     
fresh_tomatoes.open_movies_page(movies)
                         
