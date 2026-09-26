def do_something_cool():
    print("Hi")

def user_request_to_stop():
    print (2+2)

while True:
    do_something_cool()
    if user_request_to_stop():
        break

#Not Properly worked