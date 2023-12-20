# Задание 'Из молекулы в атомы'

class AtomCounter:
    def __init__(self, formula):
        self.formula = formula
        self.stack = [{}]
        self.i = 0

    def handle_atom(self):
        atom = self.formula[self.i]
        self.i += 1
        while self.i < len(self.formula) and self.formula[self.i].islower():
            atom += self.formula[self.i]
            self.i += 1
        if self.i < len(self.formula) and self.formula[self.i].isdigit():
            count = ''
            while self.i < len(self.formula) and self.formula[self.i].isdigit():
                count += self.formula[self.i]
                self.i += 1
            self.stack[-1][atom] = self.stack[-1].get(atom, 0) + int(count)
        else:
            self.stack[-1][atom] = self.stack[-1].get(atom, 0) + 1

    def count_atoms(self):
        while self.i < len(self.formula):
            if self.formula[self.i].isupper():
                self.handle_atom()
                continue
            if self.formula[self.i] == '(' or self.formula[self.i] == '[' or self.formula[self.i] == '{':
                self.stack.append({})
                self.i += 1
                continue
            if self.formula[self.i] == ')' or self.formula[self.i] == ']' or self.formula[self.i] == '}':
                self.i += 1
                if self.i < len(self.formula) and self.formula[self.i].isdigit():
                    count = ''
                    while self.i < len(self.formula) and self.formula[self.i].isdigit():
                        count += self.formula[self.i]
                        self.i += 1
                    sub_formula = self.stack.pop()
                    for key, value in sub_formula.items():
                        self.stack[-1][key] = self.stack[-1].get(key, 0) + value * int(count)
                else:
                    sub_formula = self.stack.pop()
                    for key, value in sub_formula.items():
                        self.stack[-1][key] = self.stack[-1].get(key, 0) + value
                continue
            self.i += 1

        return self.stack[0]


if __name__ == '__main__':
    formula = input('Введите формулу молекулы: ')
    counter = AtomCounter(formula)
    atoms = counter.count_atoms()
    print(atoms)
