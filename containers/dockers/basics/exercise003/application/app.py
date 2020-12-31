# Python Program - Docker Hello World!!

def about(firstname,lastname,profession):
    return "Hello {} {} loves {} !!".format(firstname,lastname,profession)

if __name__ == "__main__":
    import sys 
    firstname,lastname,profession = sys.argv[1],sys.argv[2],sys.argv[3]
    print(about(firstname,lastname,profession))