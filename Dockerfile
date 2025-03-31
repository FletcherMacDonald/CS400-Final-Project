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

FROM python:3.9

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY ortho.json /app/ortho.json
RUN pip install -r /app/requirements.txt
COPY app.py /app/app.py
#COPY test_app.py /app/test_app.py
#RUN python test_app.py

ENTRYPOINT ["python"]
CMD ["app.py"]