FROM python:3.11

WORKDIR /historical_platform

COPY . .

RUN pip install -r historical_platform_requirements.txt

CMD ["python", "historical_pipeline_runner.py"]
