
#!/bin/bash

DNS="1.1.1.1"

query() {
    local domain="$1"
    local type="$2"

    echo "=== $(date '+%H:%M:%S') | $domain ($type) ==="
    dig @"$DNS" "$domain" "$type" +noall +answer
    echo
}

echo "Initial DNS lookups"
query ca NS
query ucalgary.ca NS
query schulich.ucalgary.ca A

sleep 5

echo "TTL values after 5 seconds"
query ca NS
query ucalgary.ca NS
query schulich.ucalgary.ca A

sleep 5

echo "Query related domain"
query cpsc.ucalgary.ca A

echo "Check whether parent TTLs reset"
query ca NS
query ucalgary.ca NS
query schulich.ucalgary.ca A

sleep 5

echo "Final Status"
query ca NS
query ucalgary.ca NS
query schulich.ucalgary.ca A
