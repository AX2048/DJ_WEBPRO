FROM python:3.10.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

#
WORKDIR /code/app

# 
CMD ["python3", "-m", "uvicorn", "web_project.asgi:application", "--host", "0.0.0.0", "--port", "8000"]