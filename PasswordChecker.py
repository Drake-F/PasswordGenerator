def check_password(password : str, reqLower : bool, reqUpper : bool, reqNum : bool, reqSpecial : bool, reqAltSpecial):
    # Checks if a provided password meets the requirements specified by the user. Returns True if password passes requirements specified by user and False otherwise.
    if len(password) < reqLower + reqUpper + reqNum + reqSpecial + reqAltSpecial:
        raise ValueError("Password failed as user required more characters than provided length with given password.")

    # Making our sets of characters to check
    SPECIAL = list("!@#$%^&*(_-+=")
    ALT_SPECIAL = list("~`/\\|[{]}:;\"'<>,.?")

    low, up, num, spec, alt_spec = not reqLower, not reqUpper, not reqNum, not reqSpecial, not reqAltSpecial
    for i in range(len(password)):
        if password[i].isalpha():
            if password[i].isupper():
                up = True
            else:
                low = True
        if password[i].isnumeric():
            num = True
        if password[i] in SPECIAL:
            spec = True
        if password[i] in ALT_SPECIAL:
            alt_spec = True

    return 5 == low + up + num + spec + alt_spec