import threading
import time
import random
import string

# Function to join a thousand random letters
def join_random_letters():
	letters = [random.choice(string.ascii_letters) for _ in range(1000)] 
    joined_letters = ''.join(letters) 
    print("Joined Letters Task Done")

