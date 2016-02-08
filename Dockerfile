FROM pdxjohnny/vnc
MAINTAINER John Andersen

RUN apt-get -y update && \
    apt-get -y install wget libv4l-0 libpango1.0-0 \
      python python-dev python-pip python-xlib python-tk python-pil scrot \
      libasound2 libgdk-pixbuf2.0-0 libgtk2.0-0 && \
    python -m pip install -U pip && \
    apt-get clean && \
    rm -rf /var/cache/apt/* && \
    wget https://dl.google.com/linux/direct/google-talkplugin_current_amd64.deb && \
    dpkg -i google-talkplugin_current_amd64.deb && \
    wget -O /usr/share/firefox.tar.bz2 \
    'https://download.mozilla.org/?product=firefox-44.0-SSL&os=linux64&lang=en-US' && \
    cd /usr/share/ && \
    tar xjf /usr/share/firefox.tar.bz2 && \
    rm -rfv /usr/share/firefox.tar.bz2 && \
    ln -s /usr/share/firefox/firefox /usr/bin/firefox

RUN apt-get -y update && \
    apt-get -y install libdbus-glib-1-2 && \
    apt-get clean && \
    rm -rf /var/cache/apt/*

ADD . /home/user/hangouts-caller
WORKDIR /home/user/hangouts-caller
