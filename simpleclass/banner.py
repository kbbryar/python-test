class hello_world():
    """
    This is a relatively useless class which is used to determine whether the
    automated installation using pip in a virtual environment works.
    """
    def banner(self):
        print("Hello world from teesee")

    def add(self, a, b):
        return(a+b)

if __name__ == "__main__":
    value = hello_world()
    value.banner()
