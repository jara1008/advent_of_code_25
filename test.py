
filename = 'test.txt'

def read_input(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
        content_array = file_content.split('\n')
    return content_array

def compute_sum(content_array):
    sum = 0
    for obj in content_array: 
        data = obj.split(',')
        sum += int(data[1]) * float(data[2])
    return sum

content_array = read_input(filename)
sum = compute_sum(content_array)
print(f'Total price: {sum}')
