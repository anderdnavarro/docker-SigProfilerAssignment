# Base image
FROM python:3.11.13-slim-bookworm
## Update Linux packages and install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc nano && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
## Install Python dependencies
COPY requirements.txt /tmp
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    python3 -c "from SigProfilerMatrixGenerator import install as genInstall; genInstall.install('GRCh37')" && \
    rm /tmp/requirements.txt
## Copy the rest of the application code
COPY src/* /SigProfilerAssignment/
## Update PATH
ENV PATH=$PATH:/SigProfilerAssignment/
ENV MPLCONFIGDIR=/tmp
## Specify the default entrypoint
WORKDIR /home
ENTRYPOINT ["launcher.py"]