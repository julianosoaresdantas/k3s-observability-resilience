echo "{\"status\": \"start\", \"timestamp\": \"$(date)\"}" >> /var/log/thor-scan.json
sudo /home/juliano/projeto_observabilidade/thor-linux-64 --path /home/juliano/projeto_observabilidade --format json --json --output /var/log/thor-scan.json
echo "{\"status\": \"end\", \"timestamp\": \"$(date)\"}" >> /var/log/thor-scan.json
