FROM python:3.10.9

# 
WORKDIR /code

# set environment variables
# запрещает Python записывать файлы pyc на диск python -B
#ENV PYTHONDONTWRITEBYTECODE 1
# запрещает Python буферизовать stdout и stderr python -B
#ENV PYTHONUNBUFFERED 1

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app


WORKDIR /code/app
# 
CMD ["python3", "-m", "uvicorn", "web_project.asgi:application", "--host", "0.0.0.0", "--port", "8000"]