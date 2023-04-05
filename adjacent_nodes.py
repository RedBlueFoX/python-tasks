input_matrix = [
  [0, 1, 0, 1, 1],
  [1, 0, 1, 0, 0],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [1, 0, 0, 1, 0]
]


def find_adjacency(input1, input2, matrix):
  if matrix[input1][input2]:
    print(True)
  else:
    print(False)


prompt1 = int(input('Input node 1\n'))
prompt2 = int(input('Input node 2\n'))

find_adjacency(prompt1, prompt2, input_matrix)

