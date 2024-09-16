import statistics as stats

def get_data():
    # Ask the user for input data, with the option to paste or enter large datasets
    data = input("Please enter a dataset (numbers separated by spaces): ")
    
    # Convert the input string into a list of floats
    data = [float(num) for num in data.split()]
    
    return data

def calculate_statistics(data):
    print(f"\nData size: {len(data)} numbers")
    # Mean
    mean = sum(data) / len(data)
    print(f"Mean: {mean}")
    # Median
    median = stats.median(data)
    print(f"Median: {median}")
    # Mode with error handling if there's no unique mode
    try:
        mode = stats.mode(data)
        print(f"Mode: {mode}")
    except stats.StatisticsError:
        print("Mode: No unique mode found")
    # Standard Deviation and Variance
    std_dev = stats.stdev(data)
    variance = stats.variance(data)
    print(f"Standard Deviation: {std_dev}")
    print(f"Variance: {variance}")
    # Minimum value
    print(f"Min: {min(data)}")
    # Maximum value
    print(f"Max: {max(data)}")
    # Range
    print(f"Range: {max(data) - min(data)}")
    #Sum 
    print(f"Sum: {sum(data)}")
    #Count
    print(f"Count: {len(data)}")

def main():
    data = get_data()
    calculate_statistics(data)
if __name__ == "__main__":
    main()
    
