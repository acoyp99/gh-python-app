import redis

print('Hello from GitHub Actions')

def connect_and_set_key():
    try:
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        r.set('mykey', 'Hello, Redis!')
        value = r.get('mykey')
        print(f"Value for 'mykey': {value}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    connect_and_set_key()
