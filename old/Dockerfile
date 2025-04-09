FROM python:3.9

# Set the working directory
RUN mkdir /app
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy application files (including JSON data, Python script, and templates)
COPY ortho.json /app/ortho.json
COPY analyze_data.py /app/analyze_data.py

# Copy static files (CSS, JS, images)
COPY static /app/static

# Copy templates folder (HTML files)
COPY templates /app/templates

# Expose the port Flask will run on
EXPOSE 5555

# Set the environment variables for Flask
ENV FLASK_APP=analyze_data.py
ENV FLASK_ENV=development

# Run Flask app
ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=5555"]

#FROM python:3.9

#RUN mkdir /app
#WORKDIR /app
#COPY requirements.txt /app/requirements.txt
#COPY ortho.json /app/ortho.json
#RUN pip install -r /app/requirements.txt
#COPY index.html 
#COPY analyze_data.py /app/analyze_data.py
#COPY test_analyze_data.py /app/test_analyze_data.py
#RUN python test_analyze_data.py

#ENTRYPOINT ["python"]
#CMD ["analyze_data.py"]

#FROM python:3.9

#RUN mkdir /app
#WORKDIR /app
#COPY requirements.txt /app/requirements.txt
#COPY ortho.json /app/ortho.json
#RUN pip install -r /app/requirements.txt
#COPY analyze_data.py /app/analyze_data.py

# Copy static files (CSS, JS, images)
#COPY static /app/static
# Copy templates folder (HTML files)
#COPY templates /app/templates

#ENTRYPOINT ["python"]
#CMD ["analyze_data.py"]
