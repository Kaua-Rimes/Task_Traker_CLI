def valid_text_input(n):
    while True:
        text = input(n).strip()
        if not text:
            print("This field can't be empty.")
        else:
            return text.title()
