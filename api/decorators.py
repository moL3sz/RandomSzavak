






def login_required(f):
    # This function is what we "replace" hello with
    def wrapper(*args, **kw):
        print(args)
        logged_in = 1
        if logged_in:
            return f(*args, **kw)  # Call hello
        else:
            raise Exception("Yo are not logged in")
    return wrapper


@login_required
def auth_access(token):
    print(token)


auth_access("asd")