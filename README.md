Requirements
---

```bash
apt-get -y install firefox wget libv4l-0 libpango1.0-0 \
  python python-dev python-pip python-xlib python-tk python-pil scrot \
  libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev \
  libwebp-dev tcl8.6-dev tk8.6-dev && \
wget https://dl.google.com/linux/direct/google-talkplugin_current_amd64.deb && \
dpkg -i google-talkplugin_current_amd64.deb && \
rm -rf google-talkplugin_current_amd64.deb && \
pip install -U pip && \
pip install pyautogui websocket-client
```

Usage
---

```bash
docker build -t pdxjohnny/hangouts-caller .
docker run --rm -it -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /home/developer/hangouts-caller:$PWD \
  -e DISPLAY=$DISPLAY  pdxjohnny/hangouts-caller

HANGOUTS_CALL_CENTER_HOST=ws://localhost:8080/api/caller \
  python contact-call-center.py
```
