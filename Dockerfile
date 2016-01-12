FROM ubuntu:14.04
MAINTAINER John Andersen

RUN apt-get update -y && \
    apt-get install -y firefox && \
    apt-get install -y python python-dev python-pip python-xlib python-tk && \
    python -m pip install -U pip && \
    apt-get clean && \
    rm -rf /var/cache/apt/* && \
    export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

RUN apt-get update -y && \
    apt-get install -y python-pil scrot && \
    apt-get clean && \
    rm -rf /var/cache/apt/*

ADD . /home/developer/hangouts-caller
WORKDIR /home/developer/hangouts-caller

RUN chown developer:developer -R /home/developer

USER developer
ENV HOME /home/developer
CMD /home/developer/hangouts-caller/startup.sh
