FROM connormanning/entwine
MAINTAINER Valentin RESSEGUIER <valentin.resseguier@hva.nl>

RUN apt update && \
    apt install -y wget zip build-essential python

RUN cd /tmp && \
	wget 'http://lastools.org/download/laszip.zip' && \
	unzip laszip.zip && \
    cd LAStools && \
    make && \
    cd bin && \
    for exc in $(find . -type f -executable -print);do cp $exc /usr/local/bin/$exc; done

ADD pipeline.py /usr/local/bin/pipeline.py
RUN chmod +x /usr/local/bin/pipeline.py

ADD entwine-cesium-pages /opt/entwine-cesium-pages/

WORKDIR /tmp

ENTRYPOINT ["python","/usr/local/bin/pipeline.py"]