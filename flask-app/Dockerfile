FROM python:3.8
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
COPY templates /usr/src/app/templates
COPY app.py /usr/src/app/
EXPOSE 5001
CMD ["python3", "/usr/src/app/app.py"]