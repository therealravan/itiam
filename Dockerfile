FROM python

ADD interest.py .

RUN pip install requests beautifulsoup4 python-dotenv

CMD [ "python", "./interest.py"]