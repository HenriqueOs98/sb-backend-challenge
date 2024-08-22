import random

def generate_cpf():
    cpf = [random.randrange(10) for _ in range(9)]

    for _ in range(2):
        value = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
        cpf.append(11 - value if value > 1 else 0)

    return "".join(str(x) for x in cpf)