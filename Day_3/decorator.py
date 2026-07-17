def limit_calls(func):
    def wrapper(*args, **kwargs):
        if(cnt < 3):
            cnt = cnt + 1
        else:
            print("[BLOCKED] limit has reached buy premium")
        return func(*args, **kwargs)
    return wrapper

def send_api_request(name : str):
    print(f"Sent for {name}")

send_api_request("john")
send_api_request("rony")
send_api_request("")
