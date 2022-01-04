FROM alpine:3.15

RUN apk add python3 \
  && apk add py3-pip \
  && pip install --upgrade pip \
  && apk add sqlite

# working to work
WORKDIR /app

COPY . .

# dependencies
RUN pip install -r requirements.txt

# running
CMD ["python3", "index.py"]