FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install  --no-cache-dir -r requirements.txt

COPY . .

RUN python -c "import nltk;nltk.download('book')"

CMD [ "jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]


