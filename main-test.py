# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(2,3) == 5
	assert Add(3,3) == 6
	assert Add(3,5) == 8
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()
