def ngrams(input, n):
    input = input.split(' ')
    output = []

    print(len(input) - n + 1)

    for i in range(len(input) - n + 1):
        print(input[i:i + n])
        output.append(input[i:i + n])
    return output


words = "How are you doing man"
result = ngrams(words, 2)

for row in result:
    print(row)

print(result)