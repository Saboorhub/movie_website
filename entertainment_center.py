import fresh_tomatoes
import media

avatar = media.Movie("Avatar", 
	"Avatar is the story of an ex-Marine who finds himself thrust into hostilities on an alien planet filled with exotic life forms.",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://youtu.be/5PSNL1qE6VY")

titanic = media.Movie("Titanic", 
	"Titanic is the story of love between two people from two different socio-economic classes.",
	"https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
	"https://youtu.be/ZQ6klONCq4s")


training_day = media.Movie("Training Day", 
	"Training Day is the story of two narcotics officers over a 24 hours period with intensive action.",
	"https://upload.wikimedia.org/wikipedia/en/b/b3/Training_Day_Poster.jpg",
	"https://youtu.be/DXPJqRtkDP0")

the_shawshank_redemption = media.Movie("The Shawshank Redemption", 
	"The Shawshank Redemption is the story of survival in the prison system and breaking out of it.",
	"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
	"https://youtu.be/NmzuHjWmXOc")

king_kong = media.Movie("King Kong", 
	"King Kong is the story of unprecedented love between a gorrila and a human culminating in the death of the former.",
	"https://upload.wikimedia.org/wikipedia/en/6/6a/Kingkong_bigfinal1.jpg",
	"https://youtu.be/AYaTCPbYGdk")

scarface = media.Movie("Scarface", 
	"Scarface is the story of an immigrant who cilmbs up the ladder in the illegal narcotics industry.",
	"https://upload.wikimedia.org/wikipedia/en/7/71/Scarface_-_1983_film.jpg",
	"https://youtu.be/7pQQHnqBa2E")

roman_holiday = media.Movie("Roman Holiday", 
	"Roman Holiday is the adventure story of a royal princess who roams the Rome on her own.",
	"https://upload.wikimedia.org/wikipedia/en/b/b7/Roman_holiday.jpg",
	"https://youtu.be/9GzCG6lpFUw")

the_legend_of_bagger_vance = media.Movie("The Legend of Bagger Vance", 
	"The The Legend of Bagger Vance is the story of love and separation and the sports of Golf and confidence.",
	"https://upload.wikimedia.org/wikipedia/en/b/b3/Legend_of_bagger_vance_ver2.jpg",
	"https://youtu.be/lpsF4MfeGlQ")

movies = [avatar, titanic, training_day, the_shawshank_redemption, king_kong, scarface, roman_holiday, the_legend_of_bagger_vance]

fresh_tomatoes.open_movies_page(movies)

