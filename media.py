import webbrowser

class Movie():
    '''Creates movie for display on web page'''

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''Creates movie object to store data on movie'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''Opens movie trailer url in default web browser'''
        webbrowser.open(self.trailer_youtube_url)
