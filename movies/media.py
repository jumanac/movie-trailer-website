import webbrowser

#The class Movie represents all the attributes for a movie
class Movie():
    #Initializes a new instance of the Movie class.
    #movie_title is the name of the movie.
    #movie_storyline is the central plot of the movie.
    #poster_image is the image file for the movie poster.
    #trailer_youtube is the link of the movie trailer in youtube.
    #release_date is the date the movie was released.
    #actors is the list of the main actors appearing in the movie.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,
                 release_date = "", actors = ""):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        self.actors = actors

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
