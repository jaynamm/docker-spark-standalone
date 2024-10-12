FROM bitnami/spark:3.5.2

# Install Python packages
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt