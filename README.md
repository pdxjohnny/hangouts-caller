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

You need to change the environment variables set in `env`. You can use this to
set the proxies and you MUST set the call center host. Then build the image.

```bash
docker build -t pdxjohnny/hangouts-caller .
docker run --rm -ti -p 5901:5901 pdxjohnny/hangouts-caller
```
