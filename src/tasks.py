import random
import string

# Function to join a thousand random letters
def join_random_letters(num_letters):
  letters = ''.join(random.choice(string.ascii_letters) for _ in range(num_letters)) 
  print("Joined Letters Task Done")


# Function to add a thousand random numbers
def add_random_numbers(num_numbers):
  numbers = sum(random.randint(1, 100) for _ in range(num_numbers))
  print("Add Numbers Task Done")
