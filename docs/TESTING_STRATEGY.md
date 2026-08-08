# Testing Strategy Document

## Movie Rating Prediction API — DDM501 Lab 3

---

## 1. Testing Approach

This project follows the **ML Testing Pyramid**, extending traditional software testing with ML-specific concerns:

```
┌─────────────────────────┐
│   System / E2E Tests    │  ← Full workflow validation
├─────────────────────────┤
│  Model Behavioral Tests │  ← Invariance, directional, min functionality
├─────────────────────────┤
│    Data Quality Tests   │  ← Schema, distribution, completeness
├─────────────────────────┤
│   Integration Tests     │  ← API endpoints, component interactions
├─────────────────────────┤
│      Unit Tests         │  ← Individual functions and classes
└─────────────────────────┘
```

The pyramid ensures we catch bugs at every layer — from low-level function correctness to high-level model behavior.

---

## 2. Test Categories

### 2.1 Unit Tests (`tests/unit/`)

**Purpose:** Test individual functions and classes in isolation.

| File | What it tests |
|------|--------------|
| `test_model.py` | `MovieRatingModel` class — loading, prediction types, ranges, batch operations, error handling |
| `test_schemas.py` | Pydantic schemas — request/response validation, field constraints, type enforcement |

**Key assertions:**
- `predict()` returns a `float` within `[1.0, 5.0]`
- `predict_batch()` returns correct-length lists
- `is_loaded()` returns boolean
- Schema validation rejects missing, empty, and invalid fields
- Pydantic v2 enforces strict string types

### 2.2 Integration Tests (`tests/integration/`)

**Purpose:** Test API endpoints and component interactions via HTTP requests.

| File | What it tests |
|------|--------------|
| `test_api.py` | All FastAPI endpoints — health, root, predict, batch predict, model info, error handling |

**Key assertions:**
- Correct HTTP status codes (200, 404, 405, 422)
- Response JSON contains expected fields
- Predicted ratings are within valid range
- Invalid requests return proper error responses

### 2.3 Data Quality Tests (`tests/data/`)

**Purpose:** Validate data integrity, schema compliance, and statistical properties.

| File | What it tests |
|------|--------------|
| `test_data_quality.py` | Rating ranges, ID validation, data completeness, distributions, uniqueness, data types |

**Key assertions:**
- All ratings are in `[1.0, 5.0]` range
- No missing/null IDs or ratings
- All records have required fields
- Mean rating is within reasonable bounds
- Standard deviation indicates healthy variation
- User-movie pairs are unique

### 2.4 Model Behavioral Tests (`tests/model/`)

**Purpose:** Verify the ML model behaves correctly from a behavioral perspective.

| File | What it tests |
|------|--------------|
| `test_model_behavior.py` | Invariance, directional, minimum functionality, performance, robustness |

**Test types:**
- **Invariance:** Same input → same output; batch order doesn't affect results; individual and batch predictions match
- **Directional:** Predictions are reasonably close to actual ratings; different users/movies get different predictions
- **Minimum Functionality:** Model can predict for known users; predictions are varied (not broken)
- **Edge Cases:** Model handles unknown users/movies gracefully
- **Performance:** Mean absolute error < 1.5; no extreme prediction errors (> 3.0)

---

## 3. Test Infrastructure

### Fixtures (`tests/conftest.py`)

Shared fixtures provide reusable test data:
- `test_client` — FastAPI TestClient with startup events triggered
- `trained_model` — Pre-loaded `MovieRatingModel` instance
- `sample_prediction_request` — Valid request payload
- `sample_batch_request` — Valid batch request payload
- `sample_ratings` — Sample rating data for data quality tests
- `known_user_movie_pairs` — Known ratings from MovieLens 100K
- `unknown_users` / `unknown_movies` — Edge case IDs

### Configuration (`pyproject.toml`)

- Test paths: `tests/`
- Markers: `slow`, `integration`
- Coverage source: `app/`

---

## 4. Test Coverage Goals

| Metric | Target | Current |
|--------|--------|---------|
| Overall code coverage | ≥ 80% | **93%** |
| Unit test count | ≥ 20 | 33 |
| Integration test count | ≥ 10 | 27 |
| Data test count | ≥ 10 | 19 |
| Model behavioral test count | ≥ 10 | 14 |
| **Total tests** | ≥ 50 | **93** |


---

## 5. CI/CD Pipeline Flow

```
Push / PR → CI Pipeline
              │
              ├── Lint Job
              │   ├── flake8 (code quality)
              │   ├── black (formatting)
              │   └── isort (import sorting)
              │
              ├── Type Check Job
              │   └── mypy (static type checking)
              │
              ├── Test Job (depends on lint + type-check)
              │   ├── Install dependencies
              │   ├── Train model
              │   ├── Run pytest with coverage
              │   └── Upload coverage report
              │
              └── Build Job (depends on test)
                  ├── Build Docker image
                  └── Smoke test container

Tag (v*) → CD Pipeline
              │
              ├── Build and Push Docker Image
              ├── Deploy to Staging
              └── Deploy to Production
```

---

## 6. How to Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=app --cov-report=html --cov-report=term-missing

# Run specific test category
pytest tests/unit/ -v           # Unit tests only
pytest tests/integration/ -v    # Integration tests only
pytest tests/data/ -v           # Data quality tests only
pytest tests/model/ -v          # Model behavioral tests only

# Run a single test file
pytest tests/unit/test_model.py -v

# Run with markers
pytest tests/ -v -m "not slow"  # Skip slow tests
```

---

## 7. Pre-commit Hooks

The project uses pre-commit hooks to enforce code quality before every commit:

1. **trailing-whitespace** — Removes trailing whitespace
2. **end-of-file-fixer** — Ensures files end with newline
3. **check-yaml / check-json** — Validates config files
4. **check-added-large-files** — Prevents large file commits
5. **black** — Auto-formats Python code
6. **isort** — Sorts imports consistently
7. **flake8** — Lints for code quality issues
8. **mypy** — Static type checking
9. **pytest** — Runs unit tests before commit

```bash
# Install hooks
pre-commit install

# Run all hooks manually
pre-commit run --all-files
```
