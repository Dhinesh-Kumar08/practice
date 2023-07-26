def get_prompt():
    import platform
    osname = platform.system()
    print(osname)
    if osname == ("Linux","Darwin"):
        def prompt():
            print("This an UNIX like system")
    elif osname == "Windows":
        def prompt():
            print("unknown OS")
        return prompt

pr