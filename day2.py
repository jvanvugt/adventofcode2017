import numpy as np


def a(spreadsheet):
    return np.sum(np.max(spreadsheet, axis=1) - np.min(spreadsheet, axis=1))


def b(spreadsheet):
    results = []
    for row in spreadsheet:
        for i in range(len(row)):
            for j in range(len(row)):
                if i != j:
                    if row[i] % row[j] == 0:
                        results.append(row[i] // row[j])
    return sum(results)


if __name__ == '__main__':
    data = np.loadtxt('input2.txt', dtype=np.int, delimiter='\t')
    print(b(np.array(data)))
