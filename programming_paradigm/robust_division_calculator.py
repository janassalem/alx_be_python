def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return "Error: Cannot divide by zero."
        result = numerator / denominator
        # Use `:.1f` formatting to display a single decimal place
        return f"The result of the division is {result:.1f}"
    except ValueError:
        return "Error: Please enter numeric values only."
