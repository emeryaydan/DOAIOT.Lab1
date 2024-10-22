def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    input_string = input()
    string_list = input_string.split(",")
    float_list = [float(num) for num in string_list]
    return float_list

def calc_average(num_list):
    if not num_list:
        return 0.0
    return sum(num_list) / len(num_list)

def find_min_max(num_list):
    if not num_list:
        return [0.0, 0.0]
    return [min(num_list), max(num_list)]

def sort_temperature(num_list):
    print("sort_temperature")
    return []

def calc_median_temperature(num_list):
    print("calc_median_temperature")
    return 0.0

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    
    average = calc_average(num_list)
    min_max = find_min_max(num_list)
    
    print(f"Average temperature: {average:.2f}")
    print(f"Minimum temperature: {min_max[0]:.2f}")
    print(f"Maximum temperature: {min_max[1]:.2f}")

if __name__ == "__main__":
    main()