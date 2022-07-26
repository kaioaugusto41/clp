FROM python:3.10.4
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
COPY . code
WORKDIR /code

ENTRYPOINT [ "python3", "leitura_bits.py" ]