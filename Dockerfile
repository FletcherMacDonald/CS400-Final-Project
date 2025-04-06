# Use the official Python image (includes pip)
#FROM python:3.10

# Set the working directory
#WORKDIR /app

# Copy all files to the container
#COPY . .

# Install dependencies
#RUN pip install --no-cache-dir -r requirements.txt

# Default command to run analyze_data.py (without running the test)
#CMD ["python", "app.py"]
#CMD ["sh", "-c", "python analyze_data.py data.json"]

# add thsi in later in cmd after jata.json && python test_ortho_data.py"]

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

FROM python:3.9

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY ortho.json /app/ortho.json
RUN pip install -r /app/requirements.txt
COPY analyze_data.py /app/analyze_data.py

# Copy static files (CSS, JS, images)
COPY static /app/static
# Copy templates folder (HTML files)
COPY templates /app/templates

ENTRYPOINT ["python"]
CMD ["analyze_data.py"]
