FROM python:3.11-slim

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y curl 

COPY . /app

WORKDIR /app

RUN python3 -m venv venv

RUN echo "#!/bin/sh" > run.sh && \
    echo "source venv/bin/activate" >> run.sh && \
    echo "pip install -r requirements.txt" >> run.sh && \
    echo "python3 controller.py" >> run.sh && \
    chmod +x run.sh

CMD ["./run.sh"]
