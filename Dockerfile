FROM python:3.9
# remember to change the directory
WORKDIR /home/ubuntu/brine 

COPY . /Revenue.py

RUN pip install pandas

EXPOSE 5000

CMD ["python", "Revenue.py"]