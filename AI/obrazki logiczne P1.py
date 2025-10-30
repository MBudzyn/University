import random

def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        size_x, size_y = map(int, lines[0].split())
        rows = [list(map(int, line.split())) for line in lines[1:size_x+1]]
        cols = [list(map(int, line.split())) for line in lines[size_x+1:]]
    return size_x, size_y, rows, cols

def write_output(filename, image):
    with open(filename, 'w') as file:
        for row in image:
            file.write(''.join(row) + '\n')

def generate_random_image(size_x, size_y):
    return [['#' if random.random() < 0.5 else '.' for _ in range(size_y)] for _ in range(size_x)]

def check_compliance(spec, line):
    current_block = 0
    current_block_length = 0
    for i in range(len(line)):
        if line[i] == '#':
            current_block_length += 1
        if line[i] == '.' or i == len(line) - 1:
            if current_block < len(spec) and current_block_length != spec[current_block]:
                return False
            elif current_block == len(spec) and current_block_length != 0:
                return False
            elif current_block == len(spec):
                break
            current_block += 1
            current_block_length = 0
    return True

def calculate_fitness(spec, line):
    current_block = 0
    current_block_length = 0
    fitness = 0
    for i in range(len(line)):
        if line[i] == '#':
            current_block_length += 1
        if line[i] == '.' or i == len(line) - 1:
            if current_block < len(spec) and current_block_length == spec[current_block]:
                fitness += 1
            elif current_block == len(spec) and current_block_length == 0:
                fitness += 1
            current_block += 1
            current_block_length = 0
    return fitness

def choose_next_pixel(rows, cols, image):
    max_fitness = 0
    chosen_pixel = None

    for i in range(len(rows)):
        for j in range(len(cols)):
            if image[i][j] == '#':
                continue

            current_fitness = calculate_fitness(rows[i], image[i]) + calculate_fitness(cols[j], [image[x][j] for x in range(len(rows))])
            if current_fitness > max_fitness:
                max_fitness = current_fitness
                chosen_pixel = (i, j)

    return chosen_pixel

def perturb_image(pixel, image):
    i, j = pixel
    image[i][j] = '#' if image[i][j] == '.' else '.'

def solve_nonogram(input_file, output_file, max_iterations=1000):
    size_x, size_y, rows, cols = read_input(input_file)
    image = generate_random_image(size_x, size_y)

    for iter_num in range(max_iterations):
        if iter_num % 100 == 0:
            print("Iteration:", iter_num)

        if all(check_compliance(spec, line) for spec, line in zip(rows, image)) and \
           all(check_compliance(spec, [image[x][j] for x in range(size_x)]) for j, spec in enumerate(cols)):
            print("Solution found in iteration:", iter_num)
            break

        chosen_pixel = choose_next_pixel(rows, cols, image)
        if chosen_pixel:
            perturb_image(chosen_pixel, image)
        else:
            image = generate_random_image(size_x, size_y)

    write_output(output_file, image)

solve_nonogram("zad5_input.txt", "zad5_output.txt", max_iterations=100000)  # increase max_iterations
