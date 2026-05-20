import random
from collections import defaultdict
from typing import Final
from rich.console import Console
from rich.table import Table

NUM_ITERATIONS:Final = 1000000

def process_results(abs_values_dict, num_iterations):
    result_dict = {}
    for key, value in abs_values_dict.items():
        result_dict[key] = value/num_iterations * 100
    return result_dict

def print_results_table(results_dict):
    table = Table(title="Results")
    table.add_column("value", justify="center")
    table.add_column("precent_chance", justify="center")

    for key, value in sorted(results_dict.items()):
        table.add_row(str(key), f"{value:.2f}")

    console = Console()
    console.print(table)

def  monte_carlo(num_iterations):
    result_dict = defaultdict(int)
    for _ in range(num_iterations):
        cube1 = random.randint(1, 6)
        cube2 = random.randint(1, 6)
        summ = cube1 + cube2
        result_dict[summ] += 1
    return result_dict


def main():
    result_dict = monte_carlo(NUM_ITERATIONS)
    print_results_table(process_results(result_dict, NUM_ITERATIONS))


if __name__ == '__main__':
    main()
