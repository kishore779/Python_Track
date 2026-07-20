cnt=1
def limit_calls(func):
    global cnt 
    cnt =1 
    def wrapper(*args, **kwargs):
        if(cnt < 3):
            cnt = cnt + 1
            return func(*args, **kwargs)
        else:
            print("[BLOCKED] limit has reached buy premium")
    return wrapper

@limit_calls
def send_api_request(name : str):
    print(f"Sent for {name}")

send_api_request("john")
send_api_request("rony")
send_api_request("")
