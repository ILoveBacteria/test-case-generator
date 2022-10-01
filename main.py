import os

inputLines = int(input('number of input lines(0 for var): '))
outputLines = int(input('number of output lines(0 for var): '))
resumeFrom = int(input('resume number from? '))

variable_lines = False
if inputLines == 0 or outputLines == 0:
    variable_lines = True

os.makedirs('test/in', exist_ok=True)
os.makedirs('test/out', exist_ok=True)

for i in range(resumeFrom, 100):
    inputTest = []
    outputTest = []

    print(f'Test case number {i}')

    if variable_lines:
        inputLines = int(input('number of input lines: '))
        outputLines = int(input('number of output lines: '))

    for _ in range(inputLines):
        inputTest.append(input('in: '))
    for _ in range(outputLines):
        outputTest.append(input('out: '))

    print('Generating...')

    with open(f'test/in/input{i}.txt', 'w') as file:
        file.write('\n'.join(inputTest))
    with open(f'test/out/output{i}.txt', 'w') as file:
        file.write('\n'.join(outputTest))
