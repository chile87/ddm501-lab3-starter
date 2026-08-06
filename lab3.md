**LAB 3**

**TESTING & CI/CD FOR ML SYSTEMS**

_Ensuring Quality and Automating Deployment of ML Applications_

| Course        | DDM501                          |
| ------------- | ------------------------------- |
| Weight        | 5%                              |
| Format        | Team Lab (3-4 members per team) |
| Prerequisites | Lab 1 and Lab 2 completed       |

# 1\. OVERVIEW

## 1.1. Introduction

The purpose of this lab is to implement comprehensive testing strategies and set up CI/CD pipelines for your movie rating prediction system. Testing ML systems is fundamentally different from testing traditional software - you must test not only code correctness but also data quality, model behavior, and system integration.

You will learn to write different types of tests (unit, integration, data, model), set up automated testing with GitHub Actions, and create deployment pipelines that ensure only high-quality code reaches production.

## 1.2. Scenario: Quality Assurance for Production

Your movie rating prediction system is about to go live. Before deployment, the team needs to ensure:

- All code changes are automatically tested before merging
- Data quality is validated before training
- Model performance meets minimum thresholds
- API endpoints behave correctly under various conditions
- Deployments are automated and rollback-ready

# 2\. BACKGROUND KNOWLEDGE

## 2.1. ML Testing Pyramid

The ML Testing Pyramid extends traditional testing to include ML-specific concerns:

| Level       | Test Type                    | Examples                                |
| ----------- | ---------------------------- | --------------------------------------- |
| Unit        | Individual functions/classes | Data transformations, utility functions |
| Integration | Component interactions       | API endpoints, pipeline stages          |
| Data        | Data quality & schema        | Missing values, distributions, types    |
| Model       | Model behavior               | Predictions, invariance, performance    |
| System/E2E  | Full system behavior         | End-to-end workflows, load tests        |

## 2.2. Types of ML Tests

Behavioral Testing:

Invariance Tests: Output shouldn't change for certain input perturbations

Directional Tests: Output should change in expected direction for input changes

Minimum Functionality Tests: Simple cases the model must handle correctly

Data Tests

Schema Validation: Correct data types and structure

Distribution Tests: Data within expected ranges

Completeness Tests: No unexpected missing values

## 2.3. CI/CD for ML

CI/CD (Continuous Integration/Continuous Deployment) automates testing and deployment:

| Stage                  | Actions                                                      |
| ---------------------- | ------------------------------------------------------------ |
| Continuous Integration | Run tests, linting, type checking on every commit/PR         |
| Continuous Delivery    | Build artifacts, run integration tests, stage for deployment |
| Continuous Deployment  | Automatically deploy to production after all checks pass     |

## 2.4. GitHub Actions Overview

GitHub Actions is a CI/CD platform integrated with GitHub. Key concepts:

- Workflow: Automated process defined in YAML files
- Job: Set of steps that execute on the same runner
- Step: Individual task (run command or action)
- Action: Reusable unit of code
- Runner: Server that runs workflows

# 3\. HANDS-ON GUIDE

## Task 1: Unit Tests for ML Components

1.1. Test Structure

1.2. Writing Unit Tests

1.3. Testing with Fixtures

## Task 2: Integration Tests for API

2.1. API Endpoint Tests

2.2. Testing Error Handling

## Task 3: Data Validation Tests

3.1. Custom Data Validators

3.2. Schema Validation

Task 4: Model Behavioral Tests (30 minutes)

4.1. Invariance Tests

4.2. Directional Tests

4.3. Minimum Functionality Tests

Task 5: CI/CD with GitHub Actions (45 minutes)

5.1. Basic CI Workflow

5.2. CD Workflow with Docker

5.3. Model Validation in CI

Task 6: Code Quality Tools (15 minutes)

6.1. Pre-commit Hooks

6.2. Setup Configuration Files

# 4\. STARTER CODE TEMPLATE

unzip starter code:

_unzip ddm501-lab3-starter.zip_

Files to complete:

| File                               | TODO Items                           |
| ---------------------------------- | ------------------------------------ |
| tests/unit/test_model.py           | Implement unit tests for model class |
| tests/unit/test_schemas.py         | Implement schema validation tests    |
| tests/integration/test_api.py      | Implement API endpoint tests         |
| tests/data/test_data_quality.py    | Implement data validation tests      |
| tests/model/test_model_behavior.py | Implement behavioral tests           |
| .github/workflows/ci.yml           | Create CI pipeline configuration     |
| .pre-commit-config.yaml            | Configure pre-commit hooks           |

# 5\. DELIVERABLES & GRADING

## 5.1. Deliverables

Test Suite: Comprehensive tests (unit, integration, data, model)

CI/CD Pipeline: Working GitHub Actions workflows

Code Quality Setup: Pre-commit hooks and linting configuration

Test Coverage Report: Minimum 80% code coverage

Documentation: Testing strategy document and README

## 5.2. Grading Rubric

| Criteria       | Weight | Detailed Description                                                                                     |
| -------------- | ------ | -------------------------------------------------------------------------------------------------------- |
| Test Coverage  | 30%    | Unit tests (10%)<br><br>Integration tests (8%)<br><br>Data tests (6%)<br><br>Model behavioral tests (6%) |
| CI/CD Pipeline | 30%    | CI workflow works (12%)<br><br>All checks pass (10%)<br><br>CD workflow configured (8%)                  |
| Code Quality   | 20%    | Pre-commit hooks (8%)<br><br>Linting passes (6%)<br><br>Type hints (6%)                                  |
| Documentation  | 20%    | Testing strategy doc (10%)<br><br>README updated (5%)<br><br>Coverage report (5%)                        |

## 5.3. Submission

Deadline: 1 week after the lab session

Format: GitHub repository link with passing CI badge

Required: Screenshots of passing CI workflows
