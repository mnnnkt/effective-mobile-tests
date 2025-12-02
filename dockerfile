FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    unzip \
    tar && \
    apt-get install -y openjdk-21-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
COPY pytest.ini .
COPY conftest.py .
COPY pages pages
COPY tests tests
COPY README.md .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m playwright install
RUN playwright install-deps

RUN ALLURE_VERSION=2.35.1 && \
    mkdir -p /usr/share/allure-${ALLURE_VERSION} && \
    curl -L https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz -o /tmp/allure.tgz && \
    tar -xzf /tmp/allure.tgz -C /usr/share/ && \
    ln -s /usr/share/allure-${ALLURE_VERSION}/bin/allure /usr/bin/allure && \
    rm /tmp/allure.tgz

RUN chmod -R 755 /app

CMD ["bash"]
