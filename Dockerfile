FROM apache/airflow:2.7.1-python3.11

COPY requirements.txt /opt/airflow/

USER root
RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow

RUN pip install -r /opt/airflow/requirements.txt