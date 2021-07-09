# init a base image (Alpine is small Linux distro)
FROM python:3.8.2-alpine
# define the present working directory
WORKDIR /client
# copy the contents into the working dir
ADD . /client
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# serve
EXPOSE 80
# define the command to start the container
CMD ["python","client.py", "debug"]