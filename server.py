# from typing import Union -> What is it for?
from fastapi import FastAPI

app = FastAPI()

jobs = [
    {
        "id":"jobid-001",
        "name":"Lumberjack"
    },
    {
        "id":"jobid-002",
        "name":"Baker"
    },
    {
        "id":"jobid-003",
        "name":"Developer"
    },
    {
        "id":"jobid-004",
        "name":"Plumber"
    }]

@app.get("/")
def read_root():
    return {"health": "ok"}

@app.get("/jobs")
def list_jobs():
    return jobs

@app.get("/jobs/{id}")
def get_job(id):
    for job in jobs:
        if job["id"]==id:
            return job

