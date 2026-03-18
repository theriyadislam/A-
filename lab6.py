# 6.1) Divisible by 3
def divisible_by_3(n):
    """Return True if n is divisible by 3, else False."""
    return n % 3 == 0

# Example usage
if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(f"Divisible by 3: {divisible_by_3(num)}")
    except ValueError:
        print("Please enter a valid integer.")
# 6.2) Divide 100 by user input with exception handling
def divide_100_by(x):
    """Return 100 divided by x."""
    return 100 / x

if __name__ == "__main__":
    try:
        user_input = input("Enter a number: ")
        number = float(user_input)          # may raise ValueError
        result = divide_100_by(number)      # may raise ZeroDivisionError
        print(f"100 / {number} = {result}")
    except ValueError:
        print("Error: You must enter a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# 6.3) Magical date
def is_magical_date(date_str):
    """
    Return True if date_str (format 'mm/dd/yyyy') is magical.
    Example: '11/22/2022' -> 11 * 22 = 242, last two digits = 22 -> False.
    """
    try:
        month, day, year = date_str.split('/')
        month = int(month)
        day = int(day)
        last_two = int(year[-2:])          # last two digits of year
        return month * day == last_two
    except (ValueError, AttributeError, IndexError):
        # If the input is not in the expected format, return False
        return False

# Example usage
if __name__ == "__main__":
    test_date = input("Enter a date (mm/dd/yyyy): ")
    if is_magical_date(test_date):
        print("The date is magical!")
    else:
        print("The date is not magical.")

# 6.4) Lucky ticket
def is_lucky_ticket(ticket_str):
    """
    Return True if the sum of the first half of digits equals the sum of the second half.
    Assumes the string has an even length.
    """
    length = len(ticket_str)
    if length % 2 != 0:
        raise ValueError("Ticket number must have an even number of digits.")
    
    half = length // 2
    first_half = ticket_str[:half]
    second_half = ticket_str[half:]
    
    sum_first = sum(int(d) for d in first_half)
    sum_second = sum(int(d) for d in second_half)
    
    return sum_first == sum_second

# Example usage
if __name__ == "__main__":
    ticket = input("Enter ticket number (even number of digits): ").strip()
    try:
        if is_lucky_ticket(ticket):
            print("Lucky ticket!")
        else:
            print("Not a lucky ticket.")
    except ValueError as e:
        print(e)
