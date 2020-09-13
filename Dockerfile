FROM python:3.8-slim

ARG HANDLER

RUN apt-get update -qq && \
    apt-get install -yqq ssh && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -qq clean

# Copy files
WORKDIR /app

COPY src /app/
COPY pyproject.toml poetry.lock /app/


# Setup
RUN pip3 install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --extras ${HANDLER}

ENV HANDLER_FN ${HANDLER}

ENTRYPOINT ["python"]
CMD ["main.py"]
