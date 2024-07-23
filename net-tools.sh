#!/bin/bash

# Update and install net-tools
apt-get update && apt-get install -y net-tools

# Install Python dependencies
pip3 install tabulate

# Copy the application files
cp /path/to/devopsfetch.py /usr/local/bin/
chmod +x /usr/local/bin/devopsfetch

# Enable and start the service
cat << 'EOF' > /etc/systemd/system/devopsfetch.service
[Unit]
Description=devopsfetch Service
After=network.target

[Service]
ExecStart=/usr/local/bin/devopsfetch --users
Restart=always
User=root
Environment=PATH=/usr/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

[Install]
WantedBy=multi-user.target
EOF

systemctl enable devopsfetch
systemctl start devopsfetch
