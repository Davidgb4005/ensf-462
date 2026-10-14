
#!/bin/bash

DNS="127.0.0.1"
PORT=5353
CONF="/etc/unbound/dns-test.conf"

DOMAIN="schulich.ucalgary.ca"
RELATED="cpsc.ucalgary.ca"

query() {
    echo
    echo "===== $1 ====="
    date '+%H:%M:%S'
    dig @"$DNS" -p "$PORT" "$2" A +noall +answer +stats
    sleep 3
}

flush() {
    echo
    echo "===== Flushing $DOMAIN A record ====="
    sudo unbound-control -c "$CONF" flush_type "$DOMAIN" A
    sleep 3
}

echo "======================================"
echo "DNS Cache Experiment"
echo "======================================"

# Start with an empty experimental cache
echo "Flushing entire cache..."
sudo unbound-control -c "$CONF" flush_zone .

sleep 3

# 1. Initial DNS resolution
query "1. Initial lookup (root -> TLD -> authoritative)" "$DOMAIN"

# 2. Repeat lookup using cached A record
query "2. Cached lookup" "$DOMAIN"

# 3. Query another hostname under the same domain
query "3. Related hostname lookup" "$RELATED"

# 4. Check original hostname cache
query "4. Original hostname still cached" "$DOMAIN"

# 5. Remove only the hostname A record
flush

# 6. Resolve hostname again
query "5. Lookup after A record flush" "$DOMAIN"

# 7. Verify newly cached A record
query "6. Cached lookup after refresh" "$DOMAIN"

echo
echo "===== Experiment complete ====="

