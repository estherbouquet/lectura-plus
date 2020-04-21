FROM amd64/debian:buster

RUN apt-get update && apt-get dist-upgrade -y && \
    apt-get install -y \
      python3 \
      python3-pip \
      gconf-service \
libasound2 \
libatk1.0-0 \
libatk-bridge2.0-0 \
libc6 \
libcairo2 \
libcups2 \
libdbus-1-3 \
libexpat1 \
libfontconfig1 \
libgcc1 \
libgconf-2-4 \
libgdk-pixbuf2.0-0 \
libglib2.0-0 \
libgtk-3-0 \
libnspr4 \
libpango-1.0-0 \
libpangocairo-1.0-0 \
libstdc++6 \
libx11-6 \
libx11-xcb1 \
libxcb1 \
libxcomposite1 \
libxcursor1 \
libxdamage1 \
libxext6 \
libxfixes3 \
libxi6 \
libxrandr2 \
libxrender1 \
libxss1 \
libxtst6 \
ca-certificates \
fonts-liberation \
libappindicator1 \
libnss3 \
lsb-release \
xdg-utils \
      wget && \
    pip3 install pyppeteer Flask

ENV HOME /srv/webcap
WORKDIR /srv/webcap
RUN chown 1000 /srv/webcap
USER 1000

RUN pyppeteer-install
COPY capture-website.py /srv/webcap/webcap.py
CMD python3 webcap.py
