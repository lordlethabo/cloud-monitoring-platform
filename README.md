# Cloud Monitoring & Incident Response Platform

## Overview

The Cloud Monitoring & Incident Response Platform is a cloud-native monitoring solution built with FastAPI and Python.

It enables organizations to monitor servers, collect infrastructure metrics, detect incidents automatically, and provide intelligent recommendations for resolving issues before they impact business operations.

This project demonstrates practical Cloud Engineering, DevOps, Backend Development, and Infrastructure Monitoring skills.

---

## Features

- Register cloud servers
- Monitor CPU, Memory and Disk usage
- Automatic incident detection
- Incident management
- AI-inspired recommendations
- Dashboard statistics
- REST API
- Interactive Swagger documentation
- FastAPI backend
- Python implementation

---

## Technology Stack

- Python 3.11
- FastAPI
- Pydantic
- Uvicorn
- Psutil
- Git
- GitHub
- Oracle Cloud Infrastructure (OCI)
- Microsoft Azure
- Linux

---

## Project Structure

```
cloud-monitoring-platform
│
├── app
│   ├── database.py
│   ├── incidents.py
│   ├── main.py
│   ├── models.py
│   ├── monitoring.py
│   └── recommendations.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## API Endpoints

### Home

```
GET /
```

---

### Health Check

```
GET /health
```

---

### Register Server

```
POST /servers
```

---

### View Servers

```
GET /servers
```

---

### Collect Metrics

```
GET /metrics/{server_id}
```

---

### View Metrics

```
GET /metrics
```

---

### Scan Server

```
POST /scan/{server_id}
```

---

### View Incidents

```
GET /incidents
```

---

### View Open Incidents

```
GET /incidents/open
```

---

### Resolve Incident

```
POST /incidents/{incident_id}/resolve
```

---

### Dashboard

```
GET /dashboard
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/lordlethabo/cloud-monitoring-platform.git
```

Move into the project

```bash
cd cloud-monitoring-platform
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

---

## Swagger Documentation

After starting the application open

```
http://127.0.0.1:8000/docs
```

---

## Future Improvements

- SQLite database
- PostgreSQL
- Docker
- Docker Compose
- GitHub Actions
- CI/CD Pipeline
- Grafana Dashboard
- Prometheus Monitoring
- Email Alerts
- SMS Notifications
- Cloud Deployment
- Kubernetes

---

## Author

**Lethabo Mafihle James Moshabane**

Cloud Engineer | AI Engineer | Python Developer

GitHub

https://github.com/lordlethabo
