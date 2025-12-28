# 🚀 Flask CI/CD with Docker & GitHub Actions

A complete **production-ready CI/CD pipeline** for a Flask application using **GitHub Actions**, **Docker**, and **Docker Hub**.
This project demonstrates **automated testing, Docker image build, and push** on every commit.

---

## 📌 Project Overview

This repository showcases a real-world DevOps workflow:

1. **Code push / PR** triggers GitHub Actions
2. **Pytest** runs to validate the Flask app
3. **Docker image** is built
4. **Docker image** is pushed to Docker Hub

If tests fail ❌ → Docker build & push are blocked (quality gate).

---

## 🛠 Tech Stack

* **Python 3.11**
* **Flask**
* **Pytest & Pytest-Cov**
* **Docker**
* **GitHub Actions (CI/CD)**
* **Docker Hub**

---

## 📂 Project Structure

```
Project-Git-Action--Docker/
│
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker image definition
├── tests/
│   ├── __init__.py
│   └── test_app.py            # Pytest test cases
│
├── .github/
│   └── workflows/
│       └── docker-cicd.yml    # GitHub Actions pipeline
│
└── README.md
```

---

## ⚙️ CI/CD Pipeline Flow

```
Run Pytest 
        ↓
Build Docker Image
        ↓
Push Image to Docker Hub
```

✔ Build & push run **only if tests pass**

---

## 🧪 Local Setup & Testing

### 1️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
pip install pytest pytest-cov
```

### 3️⃣ Run tests

```bash
Python -m pytest tests/ -v
```

---

## 🐳 Docker Usage
### 🔹 Build image locally

```bash
docker build -t flask-task-manager .
```

### 🔹 Run container

```bash
docker run -p 5000:5000 flask-task-manager
```

Open browser:

```
http://localhost:5000
```
### Use Alias for better 
```
alias dkbuild='docker build -t DOCKER_USERNAME/flask-task-manager:latest .'
alias dkpush='docker push DOCKER_USERNAME/flask-task-manager:latest'
alias dkrun='docker run -p 5000:5000 DOCKER_USERNAME/flask-task-manager:latest'

```
---

## 🔐 GitHub Secrets Required

Set the following secrets in your GitHub repository:

| Secret Name       | Description             |
| ----------------- | ----------------------- |
| `DOCKER_USERNAME` | Docker Hub username     |
| `DOCKER_PASSWORD` | Docker Hub access token |

Path:

```
Repo → Settings → Secrets and variables → Actions
```

---

## 📦 Docker Hub Verification

After successful CI/CD execution:

### Pull the image

```bash
docker pull <DOCKER_USERNAME>/flask-task-manager:latest
```

### Run the image

```bash
docker run -p 5000:5000 <DOCKER_USERNAME>/flask-task-manager:latest
```
---

## 💡 Learning Outcomes

* GitHub Actions jobs run on **separate runners**
* Docker images must be **built & pushed in the same job**
* CI pipelines should **block deployment on test failure**
* Consistent Docker image tagging is critical

---



⭐ If you found this project useful, give it a star!
