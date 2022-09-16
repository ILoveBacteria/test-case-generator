import os

inputLines = int(input('number of input lines: '))
outputLines = int(input('number of output lines: '))
resumeFrom = int(input('resume number from? '))

for i in range(resumeFrom, 100):
    inputTest = []
    outputTest = []

    print(f'Test case number {i}')

    for _ in range(inputLines):
        inputTest.append(input('in: '))
    for _ in range(outputLines):
        outputTest.append(input('out: '))

    print('Generating...')

    os.makedirs('test/in', exist_ok=True)
    os.makedirs('test/out', exist_ok=True)
    with open(f'test/in/input{i}.txt', 'w') as file:
        file.write('\n'.join(inputTest))
    with open(f'test/out/output{i}.txt', 'w') as file:
        file.write('\n'.join(outputTest))
