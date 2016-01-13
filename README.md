Requirements
---

```bash
sudo -E apt-get -y install python-xlib
sudo -E pip install -r requirements.txt
```

Usage
---
docker build -t pdxjohnny/hangouts-caller .
docker run --rm -it   -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY  pdxjohnny/hangouts-caller
