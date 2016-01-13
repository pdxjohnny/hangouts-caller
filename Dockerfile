FROM ubuntu:14.04
MAINTAINER John Andersen

RUN apt-get update -y && \
    apt-get install -y firefox wget libv4l-0 libpango1.0-0 \
      python python-dev python-pip python-xlib python-tk python-pil scrot && \
    python -m pip install -U pip && \
    apt-get clean && \
    rm -rf /var/cache/apt/* && \
    wget https://dl.google.com/linux/direct/google-talkplugin_current_amd64.deb && \
    dpkg -i google-talkplugin_current_amd64.deb && \
    export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

ADD . /home/developer/hangouts-caller
WORKDIR /home/developer/hangouts-caller

RUN chown developer:developer -R /home/developer

USER developer
ENV HOME /home/developer
CMD /home/developer/hangouts-caller/startup.sh
