"""
Data quality validation tests.

Run tests:
    pytest tests/data/test_data_quality.py -v
"""

import numpy as np
import pytest


class TestRatingDataQuality:
    """Tests for rating data quality."""

    # =========================================================================
    # TODO 1: Implement Rating Range Tests
    # =========================================================================

    def test_all_ratings_in_valid_range(self, sample_ratings):
        """
        Test that all ratings are between 1.0 and 5.0.
        """
        for record in sample_ratings:
            assert 1.0 <= record["rating"] <= 5.0, (
                f"Rating {record['rating']} out of range for "
                f"user={record['user_id']}, movie={record['movie_id']}"
            )

    def test_no_negative_ratings(self, sample_ratings):
        """
        Test that there are no negative ratings.
        """
        for record in sample_ratings:
            assert record["rating"] >= 0, f"Negative rating found: {record['rating']}"

    def test_no_ratings_above_maximum(self, sample_ratings):
        """
        Test that no ratings exceed 5.0.
        """
        for record in sample_ratings:
            assert record["rating"] <= 5.0, f"Rating exceeds maximum: {record['rating']}"

    # =========================================================================
    # TODO 2: Implement ID Validation Tests
    # =========================================================================

    def test_no_missing_user_ids(self, sample_ratings):
        """
        Test that no user_ids are missing (None or empty).
        """
        for record in sample_ratings:
            assert record["user_id"] is not None, "user_id is None"
            assert record["user_id"] != "", "user_id is empty string"

    def test_no_missing_movie_ids(self, sample_ratings):
        """
        Test that no movie_ids are missing.
        """
        for record in sample_ratings:
            assert record["movie_id"] is not None, "movie_id is None"
            assert record["movie_id"] != "", "movie_id is empty string"

    def test_user_ids_are_strings(self, sample_ratings):
        """
        Test that all user_ids are strings.
        """
        for record in sample_ratings:
            assert isinstance(
                record["user_id"], str
            ), f"user_id is not a string: {type(record['user_id'])}"

    def test_movie_ids_are_strings(self, sample_ratings):
        """
        Test that all movie_ids are strings.
        """
        for record in sample_ratings:
            assert isinstance(
                record["movie_id"], str
            ), f"movie_id is not a string: {type(record['movie_id'])}"

    # =========================================================================
    # TODO 3: Implement Data Completeness Tests
    # =========================================================================

    def test_no_null_ratings(self, sample_ratings):
        """
        Test that no ratings are None/null.
        """
        for record in sample_ratings:
            assert record["rating"] is not None, "Rating is None"

    def test_all_records_have_required_fields(self, sample_ratings):
        """
        Test that all records have user_id, movie_id, and rating.
        """
        required_fields = ["user_id", "movie_id", "rating"]
        for record in sample_ratings:
            for field in required_fields:
                assert field in record, f"Missing required field: {field}"


class TestRatingDistribution:
    """Tests for rating distribution statistics."""

    # =========================================================================
    # TODO 4: Implement Distribution Tests
    # =========================================================================

    def test_mean_rating_reasonable(self, sample_ratings):
        """
        Test that mean rating is within reasonable range (2.0 - 4.5).
        """
        ratings = [r["rating"] for r in sample_ratings]
        mean_rating = np.mean(ratings)
        assert 2.0 <= mean_rating <= 4.5, f"Mean rating {mean_rating} is outside reasonable range"

    def test_rating_standard_deviation(self, sample_ratings):
        """
        Test that rating standard deviation is reasonable.
        STD should be > 0 (some variation) and < 2.0 (not too much variation).
        """
        ratings = [r["rating"] for r in sample_ratings]
        std_rating = np.std(ratings)
        assert std_rating > 0, "Standard deviation is 0 - no variation in ratings"
        assert std_rating < 2.0, f"Standard deviation {std_rating} is too high"

    def test_multiple_rating_values_exist(self, sample_ratings):
        """
        Test that there are multiple distinct rating values.
        """
        ratings = [r["rating"] for r in sample_ratings]
        unique_ratings = set(ratings)
        assert len(unique_ratings) > 1, "Only one unique rating value found"


class TestDataUniqueness:
    """Tests for data uniqueness constraints."""

    # =========================================================================
    # TODO 5: Implement Uniqueness Tests
    # =========================================================================

    def test_unique_user_movie_combinations(self, sample_ratings):
        """
        Test that each (user_id, movie_id) pair is unique.
        """
        pairs = [(r["user_id"], r["movie_id"]) for r in sample_ratings]
        assert len(pairs) == len(set(pairs)), "Duplicate user-movie pairs found"

    def test_multiple_users_exist(self, sample_ratings):
        """
        Test that there are multiple users in the dataset.
        """
        users = set(r["user_id"] for r in sample_ratings)
        assert len(users) > 1, "Only one user found in the dataset"

    def test_multiple_movies_exist(self, sample_ratings):
        """
        Test that there are multiple movies in the dataset.
        """
        movies = set(r["movie_id"] for r in sample_ratings)
        assert len(movies) > 1, "Only one movie found in the dataset"


class TestDataTypes:
    """Tests for correct data types."""

    # =========================================================================
    # TODO 6: Implement Type Tests (BONUS)
    # =========================================================================

    def test_ratings_are_numeric(self, sample_ratings):
        """
        Test that all ratings are numeric (int or float).
        """
        for record in sample_ratings:
            assert isinstance(
                record["rating"], (int, float)
            ), f"Rating is not numeric: {type(record['rating'])}"

    def test_ratings_are_float_or_int(self, sample_ratings):
        """
        Test that ratings are float or can be converted to float.
        """
        for record in sample_ratings:
            try:
                float_val = float(record["rating"])
                assert isinstance(float_val, float)
            except (ValueError, TypeError):
                pytest.fail(f"Rating cannot be converted to float: {record['rating']}")


# =============================================================================
# Run tests
# =============================================================================
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
