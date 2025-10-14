# 🛰️ RealTime-Reddit-BigData-ETL-Pipeline-on-AWS-Glue-Redshift

This project sets up the **base architecture for a Reddit ETL pipeline** using **Apache Airflow** as the workflow orchestrator.
The goal is to extract data from Reddit’s API, process it, and build a scalable pipeline for further transformation and analytics.

---

## 📁 Current Progress

* ✅ Airflow environment configured using **Docker + Docker Compose**
* ✅ Postgres and Redis containers running for metadata and task queue
* ✅ Airflow Webserver accessible at [http://localhost:8080](http://localhost:8080)
* ✅ DAG structure created (`reddit_dag.py`)
* ✅ Reddit API credentials securely stored using `config.conf` and `constants.py`
* ✅ `connect_reddit()` implemented to establish API connection

---

## 🏗️ Project Structure (So Far)

```
.
├─ dags/
│  └─ reddit_dag.py
├─ etls/
│  └─ reddit_etl.py
├─ pipelines/
│  └─ reddit_pipeline.py
├─ utils/
│  └─ constants.py
├─ config/
│  └─ config.conf
├─ docs/
│  └─ screenshots/         # Airflow UI & proof of setup
├─ docker-compose.yml
├─ Dockerfile
├─ airflow.env
└─ requirements.txt
```

---

## 🐳 Running the Airflow Environment

```bash
docker compose build
docker compose up -d
```

Access Airflow UI at: **[http://localhost:8080](http://localhost:8080)**
Default credentials:

```
username: admin
password: admin
```

---

## 🔐 Reddit API Setup

* Created a Reddit app in [Reddit Developer Portal](https://www.reddit.com/prefs/apps)
* Generated **Client ID** and **Secret**
* Stored credentials in `config/config.conf` (not hardcoded in code).

---

## 🧠 Next Steps

* Implement extraction logic with PRAW
* Add transformations and database loading
* Set up AWS components for scaling
* Automate end-to-end pipeline scheduling

---

