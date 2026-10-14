
#!/bin/bash

DNS_SERVER="1.1.1.1"
DOMAIN="en.wikipedia.org"
INTERVAL=5

echo "DNS Server: $DNS_SERVER"
echo "Domain:     $DOMAIN"
echo "Press Ctrl+C to stop"
echo

while true; do
    echo "=== $(date '+%H:%M:%S') ==="

    dig @"$DNS_SERVER" "$DOMAIN" A +noall +answer

    echo
    sleep "$INTERVAL"
done

