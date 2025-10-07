"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
def get_temperatures():
    temperatures = [32,30,29,34,35,33,30]
    return temperatures

def analyze_temps(temp_list):
    avg_temp = sum(temp_list) / len(temp_list)
    max_temp = max(temp_list)
    min_temp = min(temp_list)
    return (avg_temp, max_temp, min_temp)

def display_analysis(avg, high, low):
    print("Weekly temperatures analysis:")
    print(f"avg: {avg:.1f} ")
    print(f"high: {high} ")
    print(f"low: {low} ")
    




    


    