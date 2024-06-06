import random

def generate_euromilhoes_numbers():
    numbers = random.sample(range(1, 51), 5)
    stars = random.sample(range(1, 13), 2)
    return sorted(numbers), sorted(stars)

# Gerar números do Euromilhões cinco vezes
for i in range(5):
    numbers, stars = generate_euromilhoes_numbers()
    print(f"Jogo {i+1}: Números: {numbers}, Estrelas: {stars}")
