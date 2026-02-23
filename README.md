# FastAPI Beyond CRUD 

This is the source code for the [FastAPI Beyond CRUD](https://youtube.com/playlist?list=PLEt8Tae2spYnHy378vMlPH--87cfeh33P&si=rl-08ktaRjcm2aIQ) course. The course focuses on FastAPI development concepts that go beyond the basic CRUD operations.

For more details, visit the project's [website](https://jod35.github.io/fastapi-beyond-crud-docs/site/).

## Table of Contents

1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Project Setup](#project-setup)
4. [Running the Application](#running-the-application)
5. [Running Tests](#running-tests)
6. [CI/CD](#cicd)
7. [Contributing](#contributing)

## Getting Started
Follow the instructions below to set up and run your FastAPI project.

### Prerequisites
Ensure you have the following installed:

- Python >= 3.10
- PostgreSQL
- Redis

### Project Setup
1. Clone the project repository:
    ```bash
    git clone https://github.com/jod35/fastapi-beyond-CRUD.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd fastapi-beyond-CRUD/
    ```

3. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up environment variables by copying the example configuration:
    ```bash
    cp .env.example .env
    ```

6. Run database migrations to initialize the database schema:
    ```bash
    alembic upgrade head
    ```

7. Open a new terminal and ensure your virtual environment is active. Start the Celery worker (Linux/Unix shell):
    ```bash
    sh runworker.sh
    ```

## Running the Application
Start the application:

```bash
fastapi dev src/
```
Alternatively, you can run the application using Docker:
```bash
docker compose up -d
```
## Running Tests
Run the tests using this command
```bash
pytest
```

## CI/CD

### Verify the project with Docker (no extra downloads)
From the project root, run:
```bash
docker compose up
```
This starts the API, PostgreSQL, Redis, and Celery. No additional downloads or setup are required.

### GitHub Actions

- **Conventional Commits** (`.github/workflows/conventional-commits.yml`): On every pull request, commits are validated against [Conventional Commits](https://www.conventionalcommits.org/) (e.g. `feat: add login`, `fix(auth): token expiry`). If any commit is invalid, the PR is closed automatically and an email is sent via Ethereal to the repo owner and the PR author (owner email from `REPO_OWNER_EMAIL`).

- **Nightly Build** (`.github/workflows/nightly.yml`): Runs at 00:00 UTC on `main`. Runs tests; if they pass, builds the Docker image and pushes it to GitHub Container Registry (`ghcr.io/<owner>/<repo>:nightly`). If tests or the build fail, no image is pushed and an email notification is sent via Ethereal (when configured).

### Email notifications (Ethereal)

Failure emails are sent via [Ethereal](https://ethereal.email/) (test SMTP; messages appear in your Ethereal inbox at https://ethereal.email, they are not delivered to real addresses).

**One-time setup:** In the repo go to **Settings → Secrets and variables → Actions** and add:

| Secret        | Value                          |
|---------------|---------------------------------|
| `ETHEREAL_USER` | Your Ethereal username (e.g. `edyth49@ethereal.email`) |
| `ETHEREAL_PASS` | Your Ethereal password          |

**Other variables:**

| Variable / Secret     | Description |
|-----------------------|-------------|
| `REPO_OWNER_EMAIL`    | Repo owner’s email (for PR failure emails). PR author is added automatically when available. |
| `NOTIFICATION_EMAIL`  | For nightly failure emails, who to show as “To” (Ethereal still only shows messages in the Ethereal inbox). |

Do not commit Ethereal credentials to the repo; use GitHub Actions secrets only.

## Contributing
I welcome contributions to improve the documentation! You can contribute [here](https://github.com/jod35/fastapi-beyond-crud-docs).
