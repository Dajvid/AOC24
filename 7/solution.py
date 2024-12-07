from itertools import product


class Equation():
    def __init__(self, line, concat_operator=False):
        values = line.strip().split(" ")
        self.result = int(values[0].strip(":"))
        self.operands = [int(x) for x in values[1:]]
        self.plus = lambda x, y: x + y
        self.times = lambda x, y: x * y
        self.concat = lambda x, y: int(str(x) + str(y))
        self.available_operators = [self.plus, self.times]
        if concat_operator:
            self.available_operators.append(self.concat)

    def __repr__(self):
        return f"{self.result} = {self.operands}"

    def add_concat_operator(self):
        if not self.concat in self.available_operators:
            self.available_operators.append(self.concat)
        return self

    def generate_possible_operators(self):
        return product(self.available_operators, repeat=len(self.operands) - 1)

    def evaluate(self, operators):
        accumulator = self.operands[0]
        for i, operand in enumerate(self.operands[1:]):
            accumulator = operators[i](accumulator, operand)
        return accumulator

    def print_with_operators(self, operators):
        print(self.operands[0], end=" ")
        for i, operand in enumerate(self.operands[1:]):
            if operators[i] == self.plus:
                print(f" + {operand}", end=" ")
            else:
                print(f" * {operand}", end=" ")
        print()

    def can_be_true(self):
        for operators in self.generate_possible_operators():
            if self.evaluate(operators) == self.result:
                return True
        return False

equations = []
with open("input.txt") as f:
    for line in f.readlines():
        equations.append(Equation(line))

print(f"Sum of satisfiable results: {sum([equation.result for equation in equations if equation.can_be_true()])}")
equations = [equation.add_concat_operator() for equation in equations]
print(f"Sum of satisfiable results with concat operator: {sum([equation.result for equation in equations if equation.can_be_true()])}")
