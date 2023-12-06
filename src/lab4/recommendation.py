class MovieRecommendationService:
    def __init__(self, movies, history):
        self.movies_file = movies
        self.history_file = history
        self.movies = self.load_movies()
        self.history = self.load_history()

    def load_movies(self):
        movies = {}
        with open(self.movies_file, 'r', encoding="utf-8") as file:
            for line in file:
                movie_id, movie_name = line.strip().split(',')
                movies[int(movie_id)] = movie_name
        return movies

    def load_history(self):
        history = []
        with open(self.history_file, 'r') as file:
            for line in file:
                viewed_movies = list(map(int, line.strip().split(',')))
                history.append(viewed_movies)
        return history

    def get_user_views(self):
        user_input = input("Введите список просмотренных фильмов (через запятую): ")
        user_views = list(map(int, user_input.split(',')))
        return user_views

    def filter_users(self, user_views):
        filtered_users = []
        for user in self.history:
            user_set = set(user)
            if len(user_set.intersection(user_views)) >= len(user_views) / 2:
                filtered_users.append(user)
        return filtered_users

    def exclude_watched_movies(self, user_views, filtered_users):
        unwatched_movies = []
        for user in filtered_users:
            for movie in user:
                if movie not in user_views:
                    unwatched_movies.append(movie)
        return unwatched_movies

    def recommend_movie(self):
        user_views = self.get_user_views()
        filtered_users = self.filter_users(user_views)
        unwatched_movies = self.exclude_watched_movies(user_views, filtered_users)

        movie_views_count = {}
        for movie in unwatched_movies:
            if movie in movie_views_count:
                movie_views_count[movie] += 1
            else:
                movie_views_count[movie] = 1

        recommended_movie_id = max(movie_views_count, key=movie_views_count.get)
        recommended_movie_name = self.movies[recommended_movie_id]

        print("Рекомендуемый фильм:", recommended_movie_name)

movies_file = 'movies.txt'
history_file = 'history.txt'
recommendation_service = MovieRecommendationService(movies_file, history_file)
recommendation_service.recommend_movie()