FROM amazon/aws-lambda-python:latest

# Installs python, removes cache file to make things smaller
RUN yum update -y && \
    yum install -y python3 python3-dev python3-pip gcc && \
    rm -Rf /var/cache/yum
# Be sure to copy over the function itself!
COPY lambda_function.py ./
# Copies requirements.txt file into the container
COPY lambda-requirements.txt ./
# Installs dependencies found in your requirements.txt file
RUN pip install -r lambda-requirements.txt

# Points to the handler function of your lambda function
CMD ["lambda_function.handler"]