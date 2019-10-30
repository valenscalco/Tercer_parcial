FROM python:3

RUN git clone https://github.com/valenscalco/Tercer_parcial.git
WORKDIR /Tercer_parcial

RUN pip install -r requirements.txt
RUN pip install parameterized

CMD [ "python3", "test_tateti.py"]