#!/bin/bash

# Update dan install dependencies
sudo apt update
sudo apt install -y unzip libasound2 libvulkan1

# Download chromedriver ke direktori saat ini
wget https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.55/linux64/chromedriver-linux64.zip -O /tmp/chromedriver-linux64.zip
unzip /tmp/chromedriver-linux64.zip -d /tmp/
sudo mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver

# Remove old Chromium packages
sudo apt-get remove -y chromium-browser chromium-driver

# Download and install Google Chrome (download ke /tmp)
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/google-chrome-stable_current_amd64.deb
sudo dpkg -i /tmp/google-chrome-stable_current_amd64.deb || sudo apt-get install -f -y
