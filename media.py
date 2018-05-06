import webbrowser

class Movie():
	""" Class for symbolize a movie """
	
	def __init__(self, title, poster_url, trailer_url):
		""" 
		Initialize a Movie object 
			title = a string of the movie title
			poster_url = a string containing a URL to a poster image
			trailer_url = a string containing a youtube URL trailer
        """
		
		self.title = title
		self.poster_image_url = poster_url
		self.trailer_youtube_url = trailer_url
		
	def show_trailer(self):
		""" Opens trailer in a browser """
		webbrowser.open(self.trailer_url)	
		
	

