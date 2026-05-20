from typing import Final


food_items = {
	"pizza": {"cost": 50, "calories": 300},
	"hamburger": {"cost": 40, "calories": 250},
	"hot-dog": {"cost": 30, "calories": 200},
	"pepsi": {"cost": 10, "calories": 100},
	"cola": {"cost": 15, "calories": 220},
	"potato": {"cost": 25, "calories": 350}
}

BUDGET: Final = 100

def greedy_algorithm(budget: int, items: dict) -> dict[int, int]:
    ratio_list = []
    for key, value in items.items():
        ratio_list.append({"name":key, "ratio":value["cost"]/value["calories"], "cost":value["cost"]})

    ratio_list.sort(reverse=True, key=lambda x: x["ratio"])
    item_index = 0
    result_dict = {}

    while budget > 0:
        if budget >= ratio_list[item_index]["cost"]:
            item = ratio_list[item_index]
            result_dict[item["name"]] = items[item["name"]]
            ratio_list.pop(item_index)
            budget -= item["cost"]
        else:
            item_index += 1
            if item_index >= len(ratio_list):
                break

    return result_dict


def dynamic_programming(budget: int, items: dict):

    items_list = []
    for key, value in items.items():
        items_list.append({"name":key, "calories":value["calories"], "cost":value["cost"]})

    n = len(items_list)
    K = [[0 for w in range(budget + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif items_list[i - 1]["cost"] <= w:
                K[i][w] = max(items_list[i - 1]["calories"] + K[i - 1][w - items_list[i - 1]["cost"]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    selected_items = {}
    w = budget

    for i in range(n, 0, -1):
        if K[i][w] != K[i - 1][w]:
            item = items_list[i - 1]
            selected_items[item["name"]] = {
                "cost": item["cost"],
                "calories": item["calories"]
            }
            w -= item["cost"]

    return selected_items



def main():
    print(greedy_algorithm(BUDGET, food_items))
    print(dynamic_programming(BUDGET, food_items))




if __name__ == '__main__':
    main()