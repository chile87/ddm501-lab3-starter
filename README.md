# Lab 3: Testing & CI/CD for ML Systems

![CI Pipeline](https://github.com/chile87/ddm501-lab3-starter/actions/workflows/ci.yml/badge.svg)

## Overview

Implement comprehensive testing strategies and CI/CD pipelines for the movie rating prediction system to ensure quality and automate deployment.

## Project Structure

```
ddm501-lab3-starter/
├── app/
│   ├── __init__.py
│   ├── main.py             # FastAPI application
│   ├── model.py            # ML model class
│   ├── schemas.py          # Pydantic schemas
│   └── config.py           # Configuration
├── tests/
│   ├── __init__.py
│   ├── conftest.py         # Shared fixtures
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_model.py   # Model unit tests ✅
│   │   └── test_schemas.py # Schema tests ✅
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_api.py     # API tests ✅
│   ├── data/
│   │   ├── __init__.py
│   │   └── test_data_quality.py  # Data tests ✅
│   └── model/
│       ├── __init__.py
│       └── test_model_behavior.py  # Behavioral tests ✅
├── docs/
│   └── TESTING_STRATEGY.md # Testing strategy document ✅
├── .github/
│   └── workflows/
│       ├── ci.yml          # CI pipeline ✅
│       ├── cd.yml          # CD pipeline ✅
│       └── rollback.yml    # Production rollback ✅
├── scripts/
│   └── train_model.py      # Model training script
├── models/                 # Saved models
├── .pre-commit-config.yaml # Pre-commit hooks ✅
├── pyproject.toml          # Project configuration
├── requirements.txt
├── requirements-dev.txt    # Development dependencies
├── Dockerfile
└── README.md
```

## Quick Start

### 1. Clone and Setup

```bash
cd ddm501-lab3-starter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 2. Train Model (if not exists)

```bash
python scripts/train_model.py
```

### 3. Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=app --cov-report=html --cov-report=term-missing --cov-fail-under=80

# Run specific test category
pytest tests/unit/ -v
pytest tests/integration/ -v
pytest tests/data/ -v
pytest tests/model/ -v
```

### 4. Code Quality Checks

```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Run all checks manually
pre-commit run --all-files

# Individual tools
black app/ scripts/ tests/
flake8 app/ scripts/ tests/ --max-line-length=100
isort app/ scripts/ tests/
mypy app/ scripts/ --ignore-missing-imports
```

### 5. Run the API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Completed Tasks

### Test Files
- [x] `tests/unit/test_model.py` — 15 unit tests for model class
- [x] `tests/unit/test_schemas.py` — 18 schema validation tests
- [x] `tests/integration/test_api.py` — 28 API endpoint tests
- [x] `tests/data/test_data_quality.py` — 17 data quality tests
- [x] `tests/model/test_model_behavior.py` — 16 behavioral tests

### CI/CD Files
- [x] `.github/workflows/ci.yml` — CI pipeline (lint → type-check → test → artifact → build)
- [x] `.github/workflows/cd.yml` — CD pipeline (validate → build/push → staging → production)
- [x] `.github/workflows/rollback.yml` — Manual rollback to a previous versioned image
- [x] `.pre-commit-config.yaml` — Pre-commit hooks (black, isort, flake8, mypy, pytest)

### Documentation
- [x] `docs/TESTING_STRATEGY.md` — Testing strategy document
- [x] `README.md` — Updated with CI badge and completion status

## Test Results

| Category | Tests | Status |
|----------|-------|--------|
| Unit Tests (model) | 15 | ✅ All passing |
| Unit Tests (schemas) | 18 | ✅ All passing |
| Integration Tests (API) | 28 | ✅ All passing |
| Data Quality Tests | 17 | ✅ All passing |
| Model Behavioral Tests | 16 | ✅ All passing |
| **Total** | **94** | **✅ All passing** |

### Code Coverage: **≥ 93%** (enforced target: ≥ 80%)

### Verification Screenshots

| Evidence | Screenshot |
|----------|------------|
| API health and loaded model | [`api-health-success.png`](screenshots/api-health-success.png) |
| Swagger API endpoints | [`swagger-api-success.png`](screenshots/swagger-api-success.png) |
| Successful prediction (HTTP 200) | [`api-predict-success.png`](screenshots/api-predict-success.png) |
| Coverage report (94%) | [`coverage-report-success.png`](screenshots/coverage-report-success.png) |
| JUnit result (94 tests, 0 failures) | [`test-results-94-pass.png`](screenshots/test-results-94-pass.png) |

The GitHub Actions screenshots must be refreshed after pushing this revision and completing the
new CI/CD workflows; the repository is private and requires an authenticated GitHub session.


## Test Types

### Unit Tests
Test individual functions and classes in isolation.

```python
def test_model_loads_successfully(model):
    assert model.is_loaded()
```

### Integration Tests
Test component interactions and API endpoints.

```python
def test_predict_valid_request(test_client):
    response = test_client.post("/predict", json={"user_id": "196", "movie_id": "242"})
    assert response.status_code == 200
```

### Data Tests
Validate data quality and schema.

```python
def test_ratings_in_valid_range(sample_ratings):
    for r in sample_ratings:
        assert 1.0 <= r["rating"] <= 5.0
```

### Behavioral Tests
Test model behavior patterns.

```python
def test_same_input_same_output(model):
    result1 = model.predict("196", "242")
    result2 = model.predict("196", "242")
    assert result1 == result2
```

## CI/CD Pipeline

### Continuous Integration
- Runs on every push and pull request
- Executes linting, type checking, data validation, model training, and tests
- Enforces at least 80% coverage and uploads HTML/XML coverage artifacts
- Passes the trained model artifact to the Docker build job
- Fails unless the container reports `healthy` with `model_loaded=true`

### Continuous Deployment
- Triggered on version tags (`v*`)
- Re-runs validation and builds a versioned Docker image containing the trained model
- Verifies the versioned image in the `staging` environment
- Promotes a verified version to `latest` in the `production` environment
- Creates a GitHub Release only after production verification succeeds

Required repository secrets: `DOCKER_USERNAME` and `DOCKER_PASSWORD`. Configure approval
rules for the GitHub `production` environment before creating a release tag.

### Rollback

Run the **Rollback Production** workflow manually and provide an existing semantic image tag,
such as `v1.0.0`. The workflow verifies that image, promotes it back to `latest`, and runs a
model-backed health check.
