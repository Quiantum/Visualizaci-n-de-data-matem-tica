import random

def media(X):
    return sum(X) / len(X)

if __name__ == '__main__':
    X = [random.randint(9, 12) for i in range(20)]
    mu = media(X)

    print(f'Arreglo X: {X}')
    print(f'Media = {mu}')