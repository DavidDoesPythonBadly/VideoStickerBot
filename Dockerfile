# syntax=docker/dockerfile:experimental

FROM python:3.9.16-bullseye as base

COPY ./scripts/create.env.sh ./create.env.sh
RUN chmod +x ./create.env.sh
CMD ["./create.env.sh"]

SHELL [ "/bin/bash", "-c"]

WORKDIR /app

ADD ./app /app

ADD ./lib /lib/


RUN python -m pip install --upgrade pip

RUN python -m venv "/venv" --upgrade-deps; 
RUN source "/venv/bin/activate";

RUN apt-get update && apt-get install -y --no-install-recommends \
    # build-essential \
    # libpq-dev \
    # python3-dev \
    # python3.9-dev \
    # libpython3.9-dev \
    ffmpeg \
    nginx \
    certbot \
    python3-certbot-nginx 


# RUN apt install setuptools setuptools-scm Cython python3-dev python3.9-dev libpython3.9-dev libpq-dev requests ffmpeg: 
# RUN python -m pip install --upgrade pip
# RUN /scripts/prebuilddependencies.sh "python" "/lib"
# RUN pip install build
# RUN python -m build /lib/pyrogram
# RUN cp /lib/pyrogram/dist/*.tar.gz ./lib
# RUN python -m build /lib/pyromod
# RUN cp /lib/pyromod/dist/*.*tar.gz ./lib
# RUN python -m build /lib/pystark
# RUN cp /lib/pystark/dist/*.tar.gz ./lib
RUN pip install -r requirements.txt

# RUN grep -v -x -f requirements.txt requirements-new.txt > requirements-final.txt
# RUN echo "Installing the following dependencies:"
# RUN cat requirements-final.txt
# RUN pip install --no-deps -r requirements-final.txt -t py_lib
# RUN RUN pip imstall -r requirements.txt
