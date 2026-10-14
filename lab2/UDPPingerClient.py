from socket import *
import time

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", 12001))
serverSocket.settimeout(1.0)

ping_count_max =10 
packet_lost = 0
ping_count = 0
sequence_number = 0
rtt_array = []

while ping_count < ping_count_max:
    sequence_number += 1

    try:
        message = "Ping"

        start = time.perf_counter()

        serverSocket.sendto(message.encode(), ("127.0.0.1", 12000))
        recv_message, _ = serverSocket.recvfrom(1024)

        rtt = time.perf_counter() - start
        rtt_array.append(rtt)

        print(
            f"Seq # : {sequence_number} - "
            f"Msg : {recv_message.decode()} - "
            f"RTT : {rtt * 1000000:.3f} us"
        )

    except TimeoutError:
        print("Request timed out")
        packet_lost += 1

    ping_count += 1

if rtt_array:
    print(
        f"Packets Lost : {packet_lost / ping_count_max * 100:.1f}% - "
        f"Max RTT : {max(rtt_array) * 1000000:.3f} us - "
        f"Min RTT : {min(rtt_array) * 1000000:.3f} us - "
        f"Avg RTT : {sum(rtt_array) / len(rtt_array) * 1000000:.3f} us"
    )
else:
    print("All packets were lost")

serverSocket.close()