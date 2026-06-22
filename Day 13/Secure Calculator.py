#!/usr/bin/env python3
import csv
import datetime
import os
import sys
from collections import Counter

# Concept: Custom Exceptions
class CalculatorError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class DivisionByZeroError(CalculatorError):
    def __init__(self, message="Error: Division by zero is undefined."):
        super().__init__(message)

class InvalidInputError(CalculatorError):
    def __init__(self, message):
        super().__init__(message)

# Concept: OOP Basics
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise DivisionByZeroError()
    return x / y

# Concept: File Handling
HISTORY_FILE = "calculation_history.csv"
ERROR_LOG = "error_report.log"

def init_files():
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Operation", "Operand1", "Operand2", "Result"])
    if not os.path.exists(ERROR_LOG):
        with open(ERROR_LOG, mode='w', encoding='utf-8') as f:
            f.write("Error logs:\n")

# Concept: Logging
def log_success(op, val1, val2, res):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, op, val1, val2, res])

def log_error(err_name, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ERROR_LOG, mode='a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {err_name}: {message}\n")

# Concept: Input Validation
def get_float(prompt_text):
    val_str = input(prompt_text).strip()
    if not val_str:
        raise InvalidInputError("Input cannot be empty.")
    try:
        return float(val_str)
    except ValueError:
        raise InvalidInputError(f"Must be a valid number. Entered: '{val_str}'")

def get_menu_choice(prompt_text, min_val, max_val):
    choice_str = input(prompt_text).strip()
    try:
        val = int(choice_str)
        if not (min_val <= val <= max_val):
            raise InvalidInputError(f"Choice must be between {min_val} and {max_val}.")
        return val
    except ValueError:
        raise InvalidInputError(f"Choice must be a number. Entered: '{choice_str}'")

def perform_calculation():
    print("\nSelect Operation\n")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Concept: Exception Handling
    try:
        op_choice = get_menu_choice("Enter choice (1-4): ", 1, 4)
        num1 = get_float("Enter first number: ")
        num2 = get_float("Enter second number: ")
        
        result = None
        op_name = ""
        
        match op_choice:
            case 1:
                result = add(num1, num2)
                op_name = "Addition"
            case 2:
                result = subtract(num1, num2)
                op_name = "Subtraction"
            case 3:
                result = multiply(num1, num2)
                op_name = "Multiplication"
            case 4:
                result = divide(num1, num2)
                op_name = "Division"
                
    except CalculatorError as err:
        log_error(err.__class__.__name__, err.message)
        print(f"\nError: {err.message}\n")
    except Exception as e:
        log_error(e.__class__.__name__, str(e))
        print(f"\nSystem Error: {e}\n")
    else:
        log_success(op_name, num1, num2, result)
        print(f"\nSuccess: Result of {op_name} is {result}\n")
    finally:
        print("Finished calculation process.")

def view_history():
    print("\nCalculation History\n")
    if not os.path.exists(HISTORY_FILE):
        print("No history logs exist.")
        return
    with open(HISTORY_FILE, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        rows = list(reader)
        if not rows:
            print("History is empty.")
            return
        for r in rows:
            print(f"{r[0]} | {r[1]}: {r[2]} and {r[3]} = {r[4]}")

def view_error_report():
    print("\nError Report\n")
    if not os.path.exists(ERROR_LOG):
        print("No error logs exist.")
        return
    with open(ERROR_LOG, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        log_lines = [l.strip() for l in lines if not l.startswith("Error logs")]
        if not log_lines:
            print("No errors logged.")
            return
        for line in log_lines:
            print(line)

def view_statistics():
    print("\nStatistics Summary\n")
    
    total_calcs = 0
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            total_calcs = len(list(reader))
            
    total_errors = 0
    error_types = []
    if os.path.exists(ERROR_LOG):
        with open(ERROR_LOG, mode='r', encoding='utf-8') as f:
            for line in f:
                if "]: " in line:
                    total_errors += 1
                    try:
                        err_part = line.split("]: ")[1]
                        err_name = err_part.split(":")[0].strip()
                        error_types.append(err_name)
                    except IndexError:
                        continue
                        
    most_common_err = "None"
    if error_types:
        counter = Counter(error_types)
        most_common = counter.most_common(1)
        if most_common:
            most_common_err = most_common[0][0]
            
    print(f"Total calculations: {total_calcs}")
    print(f"Total errors: {total_errors}")
    print(f"Most common error type: {most_common_err}")

def exit_calculator():
    print("\nExiting program.\n")
    sys.exit(0)

# Concept: Menu-Driven Programming
def main():
    init_files()
    while True:
        print("\nSecure Calculator Menu\n")
        print("1. Perform calculations")
        print("2. View calculation history")
        print("3. View error report")
        print("4. View summary stats")
        print("5. Exit")
        try:
            choice = get_menu_choice("Enter choice (1-5): ", 1, 5)
            match choice:
                case 1:
                    perform_calculation()
                case 2:
                    view_history()
                case 3:
                    view_error_report()
                case 4:
                    view_statistics()
                case 5:
                    exit_calculator()
        except InvalidInputError as e:
            print(f"\nSelection Error: {e.message}\n")

if __name__ == "__main__":
    main()
