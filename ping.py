from ping3 import ping
import time

def ping_server(host, byte_size):
    try:
        while True:
            # Send a ping with the custom byte size
            response_time = ping(host, size=byte_size)
            
            if response_time is not None:
                print(f"Ping to {host} successful! Round-trip time: {response_time} ms with {byte_size} bytes.")
            else:
                print(f"Ping to {host} failed! No response.")
            
            time.sleep(1)  # Wait for 1 second before the next ping
            
    except Exception as e:
        print(f"Error pinging {host}: {e}")

# Example usage
if __name__ == "__main__":
    host = ("23.227.38.70")
    byte_size = int(5,000,000,000)
    
    ping_server(host, byte_size)
