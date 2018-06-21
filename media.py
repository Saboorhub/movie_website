#the webbrowser module is imported so the open(url) function can be used to allow for displaying web page contents. 
import webbrowser 

#As the doc string states, this class is used to store movies-related information which are then used with other modules or files such as entertainment_center and fresh_tomatoes.
class Movie():
	"""This class stores some movies related information such as the title, storyline, image and youtube trailers of the movies."""
	
	#once the class Movie is called, the following functions also called instance methods will be run.
	def __init__(self, movie_title, movie_storyline, movie_poster_image_url, movie_trailer):
		"""This function initializes the variables such as title, storyline, poster_image_url and trailer_youtube_url """
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster_image_url
		self.trailer_youtube_url = movie_trailer

	def show_trailer(self):
		"""This function using the webbrowser module opens trailer_youtube_url in a browser."""
		webbrowser.open(self.trailer_youtube_url)


		