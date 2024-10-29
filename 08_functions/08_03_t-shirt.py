# This defines the function.
def make_shirt(size, text):
    print(f"The shirt will be a {size.lower()}, and it will say {text}")
# These are the Positional Arguments
make_shirt("large", "FOR THE EMPEROR")
# These are the Keyword Arguments
make_shirt(text ="FOR THE EMPEROR", size = "large")