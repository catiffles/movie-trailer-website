"""Search for files and initializes it"""
import fresh_tomatoes
import media

"""This creates a library of movies with poster and trailer"""
toy_story = media.Movie(
  "Toy Story",
  "A story of a boy and his toys that come to life",
  "http://static.comicvine.com/uploads/original/12/126071/2427179-2427161-toyjun11.jpeg",
  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

pitch_perfect = media.Movie(
  "Pitch Perfect",
  "A story of an a capella group's rise to championship",
  "http://thatfilmguy.net/wp-content/uploads/2012/12/Pitch-Perfect-Poster-2.jpeg",
  "https://www.youtube.com/watch?v=amFjSha7iqM")

the_lego_movie = media.Movie(
  "The Lego Movie",
  "Quest to become a Master Builder",
  "http://www.impawards.com/2014/thumbs/sq_lego_movie_ver9.jpg",
  "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

ratatouille = media.Movie(
  "Ratatouille",
  "Master Chef Rat",
  "https://www.movieposter.com/posters/archive/main/49/MPW-24713",
  "https://www.youtube.com/watch?v=c3sBBRxDAqk")

bolt = media.Movie(
  "Bolt",
  "A dog who mixes up his super hero identity with real life",
  "https://epicbuzz-cdn.storage.googleapis.com/uploads/image/image/1838/Bolt-Movie-Poster.jpg",
  "https://www.youtube.com/watch?v=I4D8uZVQwQc")

up = media.Movie(
  "Up",
  "Flying house, boy scout, sad old man, talking dogs",
  "https://rayraym.files.wordpress.com/2011/09/up-final-copy.jpg",
  "https://www.youtube.com/watch?v=pkqzFUhGPJg")

movies = [toy_story, pitch_perfect, the_lego_movie, ratatouille, bolt, up]
fresh_tomatoes.open_movies_page(movies)
