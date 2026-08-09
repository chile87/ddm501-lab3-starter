# ✅ DDM501 Lab 3 — Step-by-Step Rubric Checklist

> Dùng bảng này để **tự kiểm tra** trước khi nộp bài.
> Tổng điểm: **100%** = Test Coverage (30%) + CI/CD Pipeline (30%) + Code Quality (20%) + Documentation (20%)

---

## 🧪 PHẦN 1 — Test Coverage (30%)

### 1A · Unit Tests — Model Class (5%)

Kiểm tra `MovieRatingModel` — load model, predict, batch, error handling.

**✔ Những gì cần có:**

- [ ] `test_model_loads_successfully` — model load không lỗi
- [ ] `test_model_instance_has_model_attribute` — có attribute model
- [ ] `test_predict_returns_float` — predict trả về float
- [ ] `test_predict_returns_value_in_valid_range` — rating trong [1.0, 5.0]
- [ ] `test_predict_multiple_pairs_all_in_range` — nhiều pairs đều hợp lệ
- [ ] `test_predict_batch_returns_list` — batch trả về list
- [ ] `test_predict_batch_returns_correct_length` — đúng số lượng
- [ ] `test_predict_batch_all_values_in_range` — tất cả trong range
- [ ] `test_is_loaded_returns_bool` — is_loaded trả về bool
- [ ] `test_is_loaded_returns_true_for_loaded_model` — đã load = True
- [ ] `test_predict_with_none_user_id` — xử lý None user_id (BONUS)
- [ ] `test_predict_with_empty_string` — xử lý empty string (BONUS)
- [ ] `test_model_raises_error_for_missing_file` — FileNotFoundError

**🔍 Cách kiểm tra:**

```bash
cd ddm501-lab3-starter
source venv/bin/activate
pytest tests/unit/test_model.py -v
```

---

### 1B · Unit Tests — Schemas (5%)

Kiểm tra Pydantic validation cho request/response.

**✔ Những gì cần có:**

- [ ] `test_valid_request` — request hợp lệ pass
- [ ] `test_valid_request_with_numeric_strings` — numeric string pass
- [ ] `test_missing_user_id_raises_error` — thiếu user_id → ValidationError
- [ ] `test_missing_movie_id_raises_error` — thiếu movie_id → ValidationError
- [ ] `test_missing_both_fields_raises_error` — thiếu cả 2 → ValidationError
- [ ] `test_empty_user_id_raises_error` — user_id="" → ValidationError
- [ ] `test_whitespace_only_user_id_raises_error` — whitespace → ValidationError
- [ ] `test_none_values_raise_error` — None → ValidationError
- [ ] `test_integer_user_id_converted_to_string` — Pydantic strict str (BONUS)
- [ ] `test_valid_response` — response hợp lệ pass
- [ ] `test_rating_below_minimum_raises_error` — rating < 1.0 → error
- [ ] `test_rating_above_maximum_raises_error` — rating > 5.0 → error
- [ ] `test_rating_at_boundaries` — rating = 1.0 và 5.0 OK
- [ ] `test_valid_health_response` — health response hợp lệ
- [ ] `test_health_response_status_types` — đa dạng status
- [ ] `test_valid_batch_request` — batch request hợp lệ (BONUS)
- [ ] `test_empty_predictions_list_raises_error` — empty list → error (BONUS)
- [ ] `test_too_many_predictions_raises_error` — >100 items → error (BONUS)

**🔍 Cách kiểm tra:**

```bash
pytest tests/unit/test_schemas.py -v
```

---

### 1C · Integration Tests — API (8%)

Kiểm tra tất cả API endpoints qua HTTP.

**✔ Những gì cần có:**

- [ ] Health: `test_health_returns_200`, `_has_status_field`, `_has_model_loaded_field`, `_model_loaded_is_boolean`
- [ ] Root: `test_root_returns_200`, `test_root_contains_api_info`
- [ ] Predict: `test_predict_valid_request_returns_200`
- [ ] Predict Response: `_has_predicted_rating`, `_has_user_id`, `_has_movie_id`, `_rating_in_valid_range`
- [ ] Predict Validation: `_missing_user_id_returns_422`, `_missing_movie_id_returns_422`, `_empty_body_returns_422`, `_invalid_json_returns_422`
- [ ] Predict Multiple: `test_predict_multiple_valid_requests`
- [ ] Batch: `_returns_200`, `_returns_correct_count`, `_all_ratings_in_range`
- [ ] Error Handling: `test_404_for_unknown_endpoint`, `_method_not_allowed_get_predict`, `_method_not_allowed_post_health`
- [ ] Model Info: `_returns_200`, `_has_version`, `_has_is_loaded`

**🔍 Cách kiểm tra:**

```bash
pytest tests/integration/test_api.py -v
```

---

### 1D · Data Quality Tests (6%)

Kiểm tra chất lượng và schema của dữ liệu.

**✔ Những gì cần có:**

- [ ] Rating Range: `test_all_ratings_in_valid_range`, `_no_negative_ratings`, `_no_ratings_above_maximum`
- [ ] ID Validation: `test_no_missing_user_ids`, `_no_missing_movie_ids`, `_user_ids_are_strings`, `_movie_ids_are_strings`
- [ ] Completeness: `test_no_null_ratings`, `test_all_records_have_required_fields`
- [ ] Distribution: `test_mean_rating_reasonable`, `_rating_standard_deviation`, `_multiple_rating_values_exist`
- [ ] Uniqueness: `test_unique_user_movie_combinations`, `_multiple_users_exist`, `_multiple_movies_exist`
- [ ] Types (BONUS): `test_ratings_are_numeric`, `test_ratings_are_float_or_int`

**🔍 Cách kiểm tra:**

```bash
pytest tests/data/test_data_quality.py -v
```

---

### 1E · Model Behavioral Tests (6%)

Kiểm tra hành vi của model: invariance, directional, minimum functionality.

**✔ Những gì cần có:**

- [ ] Invariance: `test_same_input_same_output`, `_multiple_calls_consistent`
- [ ] Batch Invariance: `test_batch_order_independent`, `test_individual_vs_batch_same_results`
- [ ] Directional: `test_predictions_are_reasonable`, `_different_movies_different_predictions`, `_different_users_different_predictions`
- [ ] Min Functionality: `test_can_predict_for_known_user`, `_for_multiple_users`, `test_predictions_not_all_same`
- [ ] Edge Cases: `test_handles_unknown_user_gracefully`, `_unknown_movie_gracefully`
- [ ] Performance (BONUS): `test_average_error_acceptable`, `test_no_extreme_errors`
- [ ] Robustness (BONUS): `test_handles_string_numeric_ids`, `test_handles_leading_zeros_in_ids`

**🔍 Cách kiểm tra:**

```bash
pytest tests/model/test_model_behavior.py -v
```

---

### 🔍 Test Coverage Summary Check

```bash
# Chạy tất cả tests với coverage
pytest tests/ -v --cov=app --cov-report=term-missing --cov-report=html
```

Coverage target: **≥ 80%**

---

## 🔄 PHẦN 2 — CI/CD Pipeline (30%)

### 2A · CI Workflow (ci.yml) (12%)

**✔ Những gì cần có:**

- [ ] Workflow name: `CI Pipeline`
- [ ] Trigger: `push` vào `main` và `develop`, `pull_request` vào `main`
- [ ] **Lint job**: flake8 + black check + isort check
- [ ] **Type-check job**: mypy static type checking
- [ ] **Test job**: train model → pytest với coverage → upload coverage
- [ ] **Build job** (BONUS): Docker build + smoke test container
- [ ] Job dependencies: `test` needs `[lint, type-check]`, `build` needs `[test]`
- [ ] Sử dụng `actions/checkout@v4`, `actions/setup-python@v5`
- [ ] Caching pip dependencies (`actions/cache@v3`)

**🔍 Cách kiểm tra:**

```bash
cat .github/workflows/ci.yml | grep -E "^  [a-z-]+:" | head -10
```

---

### 2B · All Checks Pass (10%)

**✔ Những gì cần có:**

- [ ] flake8 pass — không lỗi linting
- [ ] black pass — code format đúng chuẩn
- [ ] isort pass — import sắp xếp đúng
- [ ] mypy pass — type checking không lỗi
- [ ] Tất cả 94 tests pass — không test nào fail
- [ ] Coverage ≥ 80% — đạt ngưỡng yêu cầu

**🔍 Cách kiểm tra:**

```bash
source venv/bin/activate
# Linting
black --check app/ scripts/ tests/
flake8 app/ scripts/ tests/ --max-line-length=100
isort --check-only app/ scripts/ tests/
# Type check
mypy app/ scripts/ --ignore-missing-imports
# Tests + Coverage
pytest tests/ -v --cov=app --cov-report=term --cov-fail-under=80 --tb=short
```

---

### 2C · CD Workflow (cd.yml) (8%)

**✔ Những gì cần có:**

- [ ] Workflow name: `CD Pipeline`
- [ ] Trigger: push tags `v*` (semantic versioning)
- [ ] Build & Push Docker image lên Docker Hub
- [ ] Deploy staging environment
- [ ] Deploy production environment (BONUS)
- [ ] Sử dụng GitHub environments: `staging`, `production`
- [ ] Tự động tạo GitHub Release
- [ ] Model artifact được đưa vào Docker image và health check xác nhận model đã load
- [ ] Có workflow rollback về image tag trước đó

**🔍 Cách kiểm tra:**

```bash
cat .github/workflows/cd.yml | grep -E "name:|on:|needs:|environment:" | head -15
```

---

## 📋 PHẦN 3 — Code Quality (20%)

### 3A · Pre-commit Hooks (8%)

**✔ Những gì cần có trong `.pre-commit-config.yaml`:**

- [ ] `trailing-whitespace` + `end-of-file-fixer`
- [ ] `check-yaml` + `check-json`
- [ ] `check-added-large-files` (max 1000KB)
- [ ] `check-merge-conflict` + `detect-private-key`
- [ ] `black` (line-length=100)
- [ ] `isort` (profile=black, line-length=100)
- [ ] `flake8` (max-line-length=100)
- [ ] `mypy` (ignore-missing-imports) (BONUS)
- [ ] `pytest` local hook — chạy unit tests (BONUS)

**🔍 Cách kiểm tra:**

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

---

### 3B · Linting Passes (6%)

**✔ Những gì cần có:**

- [ ] Black formatting: không có file nào bị reformat khi check
- [ ] Flake8: không có lỗi (E, F, W codes)
- [ ] isort: imports đúng thứ tự

**🔍 Cách kiểm tra:**

```bash
black --check app/ tests/ && echo "✅ Black OK" || echo "❌ Black failed"
flake8 app/ tests/ --max-line-length=100 && echo "✅ Flake8 OK" || echo "❌ Flake8 failed"
isort --check-only app/ tests/ && echo "✅ isort OK" || echo "❌ isort failed"
```

---

### 3C · Type Hints (6%)

**✔ Những gì cần có:**

- [ ] `app/main.py` — function signatures có type hints
- [ ] `app/model.py` — tất cả methods có type hints + return types
- [ ] `app/schemas.py` — Pydantic models (tự có type validation)
- [ ] `app/config.py` — constants có type hints ngầm
- [ ] `tests/conftest.py` — fixtures có return type hints

**🔍 Cách kiểm tra:**

```bash
mypy app/ --ignore-missing-imports && echo "✅ mypy OK" || echo "❌ mypy failed"
```

---

## 📝 PHẦN 4 — Documentation (20%)

### 4A · Testing Strategy Document (10%)

**✔ Những gì cần có trong `docs/TESTING_STRATEGY.md`:**

- [ ] Testing Approach — giải thích ML Testing Pyramid
- [ ] Test Categories mô tả từng loại (Unit, Integration, Data, Behavioral)
- [ ] Test Infrastructure — fixtures, configs
- [ ] Test Coverage Goals với bảng metrics (target vs current)
- [ ] CI/CD Pipeline Flow — diagram trực quan
- [ ] How to Run Tests — hướng dẫn chi tiết
- [ ] Pre-commit Hooks — danh sách đầy đủ

**🔍 Cách kiểm tra:**

```bash
wc -l docs/TESTING_STRATEGY.md  # > 150 dòng
grep -c "^##" docs/TESTING_STRATEGY.md  # ≥ 7 sections
```

---

### 4B · README Updated (5%)

**✔ Những gì cần có trong `README.md`:**

- [ ] Project overview & structure diagram
- [ ] Quick Start hướng dẫn setup (venv, pip install)
- [ ] Cách train model (`python scripts/train_model.py`)
- [ ] Cách chạy tests (all + từng category + coverage)
- [ ] Code quality checks commands
- [ ] Cách chạy API (`uvicorn app.main:app`)
- [ ] CI badge (sau khi push lên GitHub)

> CI badge đã trỏ đến workflow thật của repository `chile87/ddm501-lab3-starter`.

**🔍 Cách kiểm tra:**

```bash
wc -l README.md  # > 150 dòng
grep -c "^##" README.md  # ≥ 8 sections
```

---

### 4C · Coverage Report (5%)

**✔ Những gì cần có:**

- [ ] Chạy được `pytest tests/ --cov=app --cov-report=html`
- [ ] Coverage ≥ 80% (target)
- [ ] Folder `htmlcov/` được tạo sau khi chạy coverage

**🔍 Cách kiểm tra:**

```bash
pytest tests/ -v --cov=app --cov-report=term --cov-report=html --cov-fail-under=80
# Check the "TOTAL" line — must be ≥ 80%
open htmlcov/index.html
```

---

## 🎯 ĐIỂM SUMMARY

Chạy lệnh này để kiểm tra nhanh tất cả:

```bash
cd ddm501-lab3-starter
source venv/bin/activate

echo "=== 1. Test Counts ==="
echo -n "Unit (model):    "; pytest tests/unit/test_model.py --collect-only -q 2>/dev/null | tail -1
echo -n "Unit (schemas):  "; pytest tests/unit/test_schemas.py --collect-only -q 2>/dev/null | tail -1
echo -n "Integration:     "; pytest tests/integration/test_api.py --collect-only -q 2>/dev/null | tail -1
echo -n "Data:            "; pytest tests/data/test_data_quality.py --collect-only -q 2>/dev/null | tail -1
echo -n "Model Behavioral:"; pytest tests/model/test_model_behavior.py --collect-only -q 2>/dev/null | tail -1

echo ""
echo "=== 2. All Tests + Coverage ==="
pytest tests/ -v --cov=app --cov-report=term-missing --tb=short 2>&1 | tail -30

echo ""
echo "=== 3. Linting Checks ==="
black --check app/ tests/ 2>&1 | tail -3
flake8 app/ tests/ --max-line-length=100 2>&1 | tail -3
isort --check-only app/ tests/ 2>&1 | tail -3

echo ""
echo "=== 4. Type Check ==="
mypy app/ --ignore-missing-imports 2>&1 | tail -5

echo ""
echo "=== 5. CI/CD Files ==="
echo -n "ci.yml jobs: "; grep "^  [a-z]" .github/workflows/ci.yml | grep ":"  | wc -l | tr -d ' '
echo -n "cd.yml jobs: "; grep "^  [a-z]" .github/workflows/cd.yml | grep ":"  | wc -l | tr -d ' '

echo ""
echo "=== 6. Documentation ==="
echo -n "TESTING_STRATEGY.md lines: "; wc -l < docs/TESTING_STRATEGY.md | tr -d ' '
echo -n "README.md lines: "; wc -l < README.md | tr -d ' '

echo ""
echo "=== 7. Pre-commit Hooks ==="
echo -n "Hooks count: "; grep "- id:" .pre-commit-config.yaml | wc -l | tr -d ' '
```

---

## 📋 RUBRIC SCORE ESTIMATE

| Tiêu chí                       | Max   | Đánh giá                                                 |
| ------------------------------ | ----- | -------------------------------------------------------- |
| Unit Tests (model + schemas)   | 10%   | ✅ 33 tests (15 model + 18 schemas)                      |
| Integration Tests (API)        | 8%    | ✅ 28 API endpoint tests                                 |
| Data Quality Tests             | 6%    | ✅ 17 data quality tests                                 |
| Model Behavioral Tests         | 6%    | ✅ 16 behavioral tests                                   |
| **Test Coverage**              | **30%** | **~28-30%**                                            |
| CI workflow works              | 12%   | ✅ 4 jobs (lint, type-check, test, build)                |
| All checks pass                | 10%   | ✅ Black + Flake8 + isort + mypy + 94 tests ALL PASS      |
| CD workflow configured         | 8%    | ✅ Validate, build/push, staging, production, release + rollback |
| **CI/CD Pipeline**             | **30%** | **~28-30%**                                            |
| Pre-commit hooks               | 8%    | ✅ 7 repo hooks + 2 local (pytest)                       |
| Linting passes                 | 6%    | ✅ Black: 16 files unchanged, Flake8: OK, isort: OK       |
| Type hints                     | 6%    | ✅ mypy: Success, no issues in 5 source files             |
| **Code Quality**               | **20%** | **~19-20%**                                            |
| Testing strategy doc           | 10%   | ✅ 7 sections chi tiết                                   |
| README updated                 | 5%    | ✅ Đầy đủ sections + CI badge thật                       |
| Coverage report                | 5%    | ✅ ≥93% coverage; CI enforce 80% + upload artifact       |
| **Documentation**              | **20%** | **~18-20%**                                            |
| **TỔNG**                       | **100%** | **~93-100%** ⭐                                         |

---

## ✅ VERIFY KẾT QUẢ THỰC TẾ (đã chạy)

```
=== Tests:        94 passed ===
=== Coverage:     ≥93% (required minimum: 80%) ===
=== Black:        app/, scripts/, tests/ unchanged ===
=== Flake8:       OK ===
=== isort:        OK ===
=== mypy:         Success: no issues found in 5 source files ===
```

---

## ⚠️ NHỮNG THỨ CÒN THIẾU (cần làm trước khi nộp)

- [x] **Cập nhật CI badge** trong README.md — đã dùng repo thật
- [ ] **Push thay đổi mới lên GitHub** — CI/CD cần chạy lại trên commit hiện tại
- [ ] **Cấu hình secrets/environments** — `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `staging`, `production`
- [ ] **Chụp screenshots** theo submission requirements:
  - Screenshot CI pipeline chạy thành công (tất cả jobs xanh)
  - Screenshot test results (pytest output: 94 passed)
  - Screenshot coverage report (≥93%) hoặc artifact `coverage-report`
  - Screenshot CD pipeline chạy thành công từ một tag `v*`
  - Screenshot pre-commit hooks chạy thành công

> **LƯU Ý:** Sau mỗi thay đổi test, hãy chạy lại local checks rồi dùng kết quả workflow mới nhất để chụp screenshots.

---

## 📋 FILE CHECKLIST

| File                                | Trạng thái | Rubric liên quan |
| ----------------------------------- | ---------- | ---------------- |
| `tests/unit/test_model.py`          | ✅ 15 tests | Unit Tests 10%  |
| `tests/unit/test_schemas.py`        | ✅ 18 tests | Unit Tests 10%  |
| `tests/integration/test_api.py`     | ✅ 28 tests | Integration 8%  |
| `tests/data/test_data_quality.py`   | ✅ 17 tests | Data Tests 6%   |
| `tests/model/test_model_behavior.py` | ✅ 16 tests | Behavioral 6%   |
| `.github/workflows/ci.yml`          | ✅ 4 jobs   | CI/CD 30%       |
| `.github/workflows/cd.yml`          | ✅ 5 jobs   | CI/CD 30%       |
| `.github/workflows/rollback.yml`    | ✅ 1 job    | CI/CD 30%       |
| `.pre-commit-config.yaml`           | ✅ 9 hooks  | Code Quality 20% |
| `docs/TESTING_STRATEGY.md`          | ✅ 204 dòng | Documentation 20% |
| `README.md`                         | ✅ 201 dòng | Documentation 20% |
| `pyproject.toml`                    | ✅ Cấu hình | Code Quality 20% |
| `Dockerfile`                        | ✅ Hoàn chỉnh | CI/CD 30%      |
| `app/main.py`                       | ✅ 5 endpoints | -             |
| `app/model.py`                      | ✅ Hoàn chỉnh | -             |
| `app/schemas.py`                    | ✅ 6 schemas | -             |
| `app/config.py`                     | ✅ Hoàn chỉnh | -             |
| `tests/conftest.py`                 | ✅ 8 fixtures | -             |
| `scripts/train_model.py`            | ✅ Có sẵn    | -             |
| `models/svd_model.pkl`              | CI tạo artifact; không commit vào Git | - |

---

## 🚀 QUICK VERIFY COMMAND (1 dòng)

```bash
cd ddm501-lab3-starter && source venv/bin/activate && pytest tests/ -v --cov=app --cov-fail-under=80 --tb=short && black --check app/ scripts/ tests/ && flake8 app/ scripts/ tests/ --max-line-length=100 && isort --check-only app/ scripts/ tests/ && mypy app/ scripts/ --ignore-missing-imports && echo "✅ ALL CHECKS PASSED"
```
