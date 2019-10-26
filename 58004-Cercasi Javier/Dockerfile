FROM python:3           

RUN git clone https://github.com/javicercasi/2019-parcial-3.git

WORKDIR /2019-parcial-3/58004-Cercasi Javier

RUN pip freeze > requirements.txt

RUN pip install -r requirements.txt


CMD ["python", "./parcial.py"]