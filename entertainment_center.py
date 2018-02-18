import media
import fresh_tomatoes

#Instances of the "Movie" Class for media.py
avatar = media.Movie("Avatar",
                     "A marine befriends and fights for the locals on an alien planet",
                     "Sam Worthington, Zoe Saldana",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

matrix = media.Movie("The Matrix",
                     "Science fiction film about a dystopian future where reality is simulated reality",
                     "Keanu Reeves, Laurence Fishburne",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

iron_man = media.Movie("Iron Man",
                       "American superhero film based on the Marvel Comics character",
                       "Robert Downey Jr, Gwyneth Paltrow",
                       "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                       "https://www.youtube.com/watch?v=XWWd6p2JHKo")

book_eli = media.Movie("The Book of Eli",
                       "Post apocalyptic nomad is told to deliver a Bible to a safe west coast location",
                       "Denzel Washington, Mila Kunis",
                       "https://upload.wikimedia.org/wikipedia/en/e/e3/Book_of_eli_poster.jpg",
                       "https://www.youtube.com/watch?v=kAMUv22y1og")

oblivion = media.Movie("Oblivion",
                       "Humanity drains the oceans for fusion energy after a war with extraterrestrials",
                       "Tom Cruise, Morgan Freeman",
                       "https://upload.wikimedia.org/wikipedia/en/2/2e/Oblivion2013Poster.jpg",
                       "https://www.youtube.com/watch?v=OqFBQZBnsTM")

avengers = media.Movie("Avengers: Age of Ultron",
                       "Ultron tries to tear apart Captain America, Iron Man & Thor",
                       "Chris Hemsworth, Chris Evans, Robert Downey Jr",
                       "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                       "https://www.youtube.com/watch?v=tmeOjFno6Do")

the_island = media.Movie("The Island",
                         "An escape from dystopia sci-fi film where clones are harvested for the wealthy",
                         "Ewan McGregor, Scarlett Johansson",
                         "https://upload.wikimedia.org/wikipedia/en/5/56/The-island.jpg",
                         "https://www.youtube.com/watch?v=_ZyNJ3cKfEg")

time_machine = media.Movie("The Time Machine",
                           "Young inventor builds a time machine to prevent his fiancee's murder",
                           "Guy Pearce, Samantha Mumba",
                           "https://upload.wikimedia.org/wikipedia/en/6/6f/Time_machine.jpg",
                           "https://www.youtube.com/watch?v=90T7iLuzFgg")

last_samurai = media.Movie("The Last Samurai",
                           "United States Captain fights alongside Enomoto Takeaki in the Boshin War",
                           "Tom Cruise, Ken Watanabe",
                           "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Last_Samurai.jpg",
                           "https://www.youtube.com/watch?v=RdS6FgmO4j8")

fifth_element = media.Movie("The Fifth Element",
                            "Former special forces major working as taxi driver tries to find 4 mystical stones",
                            "Bruce Willis, Gary Oldman",
                            "https://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg",
                            "https://www.youtube.com/watch?v=fQ9RqgcR24g")

flight_phoenix = media.Movie("Flight of the Phoenix",
                             "Survivors of a plane crash in the desert build a new plane out of the old one",
                             "Dennis Quaid, Giovanni Ribisi",
                             "https://upload.wikimedia.org/wikipedia/en/0/0b/Flightofthephoenix.PNG",
                             "https://www.youtube.com/watch?v=bANHr1Qc-7k")

perfect_getaway = media.Movie("A Perfect Getaway",
                              "Young couple hiking in Hawaii hear that a murderer is on the loose",
                              "Timothy Olyphant, Milla Jovovich",
                              "https://upload.wikimedia.org/wikipedia/en/5/5f/Perfect_getaway.jpg",
                              "https://www.youtube.com/watch?v=0Mk8ZJJEYPE")

movies = [iron_man, matrix, the_island, perfect_getaway, time_machine, avengers]
# 12 movies did not format correctly, but divisible by both col-md-6 and col-lg-4
# [last_samurai, fifth_element, flight_phoenix, oblivion, book_eli, avatar]

fresh_tomatoes.open_movies_page(movies)

#Saving for future enhancements
#print(media.Movie.VALID_RATINGS)

