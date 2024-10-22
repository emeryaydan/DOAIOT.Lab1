def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    input_string = input()
    string_list = input_string.split(",")
    float_list = [float(num) for num in string_list]
    return float_list

def calc_average(num_list):
    print("calc_average")
    return 0.0

def find_min_max(num_list):
    print("find_min_max")
    return [0.0, 0.0]

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

if __name__ == "__main__":
    main()