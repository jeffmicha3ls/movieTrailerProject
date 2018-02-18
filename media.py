import webbrowser


class Movie():
    # Saving variable below for future enhancements
    # VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Constructor called from each Instance
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 movie_actors,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.actors = movie_actors
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Instance Method or Function
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
