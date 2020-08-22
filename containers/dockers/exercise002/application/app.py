# Python Program - Docker Hellow World!!

def hello_world():
    return "Hello Docker! I love Containers!!"


def without_build_args():
	x,y = 100,200
	return x*y

def with_build_args(x,y):
	return x*y


if __name__ == "__main__":
    print(hello_world())