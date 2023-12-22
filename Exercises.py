# Question 1: 7 to the power of 4
result1 = 7 ** 4
print(result1)  # Output: 2401

# Question 2: Split the string
s = "Hi there Sam!"
result2 = s.split()
print(result2)  # Output: ['Hi', 'there', 'Sam!']

# Question 3: Use .format() to print the string
planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers.".format(planet, diameter))

# Question 4: Nested List Indexing
first = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
word = first[3][1][2][0]
print(word)  # Output: 'hello'

# Question 5: Nested Dictionary Indexing
d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
word = d['k1'][3]['tricky'][3]['target'][3]
print(word)  # Output: 'hello'

# Question 6: Difference between a tuple and a list
# Explanation provided, no code needed

# Question 7: Function to grab the email domain
def domainGet(email):
    return email.split('@')[1]

result7 = domainGet('user@domain.com')
print(result7)  # Output: 'domain.com'

# Question 8: Function to check if 'dog' is in the string
def findDog(s):
    return 'dog' in s.lower()

result8 = findDog('Is there a dog here?')
print(result8)  # Output: True

# Question 9: Function to count the occurrences of 'dog' in a string
def countDog(s):
    return s.lower().count('dog')

result9 = countDog('This dog runs faster than the other dog dude!')
print(result9)  # Output: 2

# Question 10: Filter words starting with 's' using lambda and filter
seq = ['soup', 'dog', 'salad', 'cat', 'great']
result10 = list(filter(lambda x: x[0].lower() == 's', seq))
print(result10)  # Output: ['soup', 'salad']

# Question 11: Function to check speeding ticket
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 'No Ticket'
    elif 61 <= speed <= 80:
        return 'Small Ticket'
    else:
        return 'Big Ticket'

result11_1 = caught_speeding(81, True)
result11_2 = caught_speeding(81, False)
print(result11_1)  # Output: 'Small Ticket'
print(result11_2)  # Output: 'Big Ticket'
