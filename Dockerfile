FROM python:3.7

EXPOSE 80

# Install gunicorn
RUN pip install gunicorn

# Install falcon
RUN pip install falcon

#install pymongo
RUN pip install pymongo

#install uuid
RUN pip install uuid

# Add demo app
COPY ./app /app
WORKDIR /app
CMD ["gunicorn", "-b", "0.0.0.0:80", "main:app"]
