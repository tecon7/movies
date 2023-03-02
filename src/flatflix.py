class Movie:
    def __init__(self, title):
        self.title = title
        self.reviews = []

    def get_title(self):
        return self.title

    def get_reviews(self):
        return self.reviews

    def get_viewers(self):
        result = []
        for review in self.reviews:
            result.append(review.viewer)
            return result

    def average_rating(self):
        sum = 0 
        for review in self.reviews:
            sum += review.rating
        return sum / len(self.reviews)

    def highest_review(self):
        high_rev = self.reviews[0]
        for cur_review in self.reviews:
            if cur_review.rating > high_rev.rating:
                high_rev = cur_review
        return high_rev


class Viewer:
    def __init__(self, username):
        self.username = username
        self.reviews = []

    def get_username(self):
        return self.username

    def get_reviews(self):
        return self.reviews

    def get_movies(self):
        result = []
        for review in self.reviews:
            result.append(review.movie)
        return result

    def has_reviewed(self, movie):
        for review in self.reviews:
            if review.movie == movie:
                return True

    def rate_movie(self, movie, rating):
        result = Review(self, movie, rating)
        self.reviews.append(result)
        return result

class Review:
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

    def get_rating(self):
        return self.rating

    def get_viewer(self):
        return self.viewer

    def get_movie(self):
        return self.movie
