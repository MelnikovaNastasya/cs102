import unittest

from src.lab4.recommendation import MovieRecommendationService, history_file, movies_file


class TestMovieRecommendationService(unittest.TestCase):

    def test_load_movies(self):
        expected_movies = {
            1: 'Мстители: Финал',
            2: 'Хатико',
            3: 'Дюна',
            4: 'Унесенные призраками'
        }
        recommendation_service = MovieRecommendationService(movies_file, 'history.txt')
        result = recommendation_service.load_movies()
        self.assertEqual(result, expected_movies)

    def test_load_history(self):
        expected_history = [
            [2, 1, 3],
            [1, 4, 3],
            [2, 2, 2, 2, 2, 3]
        ]
        recommendation_service = MovieRecommendationService('movies.txt', history_file)
        result = recommendation_service.load_history()
        self.assertEqual(result, expected_history)

    def test_filter_users(self):
        user_views = [1, 2]
        filtered_users = [
            [2, 1, 3],
            [1, 4, 3],
            [2, 2, 2, 2, 2, 3],
            [4, 2, 1]
        ]
        expected_filtered_users = [
            [2, 1, 3],
            [1, 4, 3],
            [2, 2, 2, 2, 2, 3]
        ]
        recommendation_service = MovieRecommendationService('movies.txt', 'history.txt')
        result = recommendation_service.filter_users(user_views)
        self.assertEqual(result, expected_filtered_users)

    def test_exclude_watched_movies(self):
        user_views = [1, 2]
        filtered_users = [
            [1, 2, 3],
            [1, 2],
            [1, 2, 4, 5]
        ]
        expected_unwatched_movies = [3, 4, 5]
        recommendation_service = MovieRecommendationService('movies.txt', 'history.txt')
        result = recommendation_service.exclude_watched_movies(user_views, filtered_users)
        self.assertEqual(result, expected_unwatched_movies)

if __name__ == '__main__':
    unittest.main()


