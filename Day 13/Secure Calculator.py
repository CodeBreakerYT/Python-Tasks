#!/usr/bin/env python3
"""
Secure Calculator Pro
Description: A simple terminal-based calculator implementing core programming concepts.
"""

import csv
import datetime
import os
import sys
from collections import Counter

# ==========================================
# Concept: Custom Exceptions
# ==========================================

class CalculatorError(Exception):
    """Base class for custom calculator exceptions."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"[{self.timestamp}] {self.__class__.__name__}: {self.message}"


class DivisionByZeroError(CalculatorError):
    """Exception raised when dividing by zero."""
    def __init__(self, message="Error: Division by zero is undefined."):
        super().__init__(message)


class InvalidInputError(CalculatorError):
    """Exception raised when input is not valid or non-numeric."""
    def __init__(self, message):
        super().__init__(message)


# ==========================================
# Concept: OOP Basics & File Handling
# ==========================================

class CalculationLogger:
    """Manages files for successful calculations and error logs."""
    def __init__(self, history_file="calculation_history.csv", error_file="error_report.log"):
        self.history_file = history_file
        self.error_file = error_file
        self._init_files()

    def _init_files(self):
        # Create CSV header if file doesn't exist
        if not os.path.exists(self.history_file):
            with open(self.history_file, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Operation", "Operand1", "Operand2", "Result"])

        # Create log file if doesn't exist
        if not os.path.exists(self.error_file):
            with open(self.error_file, mode='w', encoding='utf-8') as f:
                f.write("--- Error Log Started ---\n")

    # Concept: Logging
    def log_success(self, operation, op1, op2, result):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.history_file, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, operation, op1, op2, result])

    def log_error(self, error):
        with open(self.error_file, mode='a', encoding='utf-8') as f:
            f.write(str(error) + "\n")

    def get_history(self):
        history = []
        if os.path.exists(self.history_file):
            with open(self.history_file, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    history.append(row)
        return history

    def get_errors(self):
        errors = []
        if os.path.exists(self.error_file):
            with open(self.error_file, mode='r', encoding='utf-8') as f:
                for line in f:
                    if not line.startswith("---") and line.strip():
                        errors.append(line.strip())
        return errors


# ==========================================
# Concept: OOP Basics
# ==========================================

class Calculator:
    """Performs the arithmetic computations."""
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise DivisionByZeroError()
        return x / y


# ==========================================
# Concept: Input Validation
# ==========================================

class InputValidator:
    """Provides helper methods to parse and validate user inputs."""
    @staticmethod
    def parse_float(input_str, field_name="Input"):
        clean_str = input_str.strip()
        if not clean_str:
            raise InvalidInputError(f"{field_name} cannot be empty.")
        try:
            return float(clean_str)
        except ValueError:
            raise InvalidInputError(f"{field_name} must be a valid number. Entered: '{clean_str}'")

    @staticmethod
    def parse_menu_choice(input_str, min_val, max_val):
        clean_str = input_str.strip()
        try:
            choice = int(clean_str)
            if not (min_val <= choice <= max_val):
                raise InvalidInputError(f"Selection must be between {min_val} and {max_val}.")
            return choice
        except ValueError:
            raise InvalidInputError(f"Selection must be an integer. Entered: '{clean_str}'")


# ==========================================
# Concept: Menu-Driven Programming
# ==========================================

class SecureCalculatorApp:
    """Manages the menu presentation, routing, and execution loop."""
    def __init__(self):
        self.logger = CalculationLogger()
        self.calculator = Calculator()

    def run(self):
        while True:
            print("\n" + "="*40)
            print("         SECURE CALCULATOR PRO")
            print("="*40)
            print("1. Perform Calculations")
            print("2. View Calculation History")
            print("3. View Error Report")
            print("4. View Summary Statistics")
            print("5. Exit")
            print("="*40)
            
            try:
                choice_str = input("Enter option (1-5): ")
                choice = InputValidator.parse_menu_choice(choice_str, 1, 5)
                
                if choice == 1:
                    self.perform_calculations()
                elif choice == 2:
                    self.view_history()
                elif choice == 3:
                    self.view_errors()
                elif choice == 4:
                    self.view_statistics()
                elif choice == 5:
                    print("\nExiting Secure Calculator Pro. Goodbye!")
                    break
            except InvalidInputError as e:
                print(f"\n[Validation Error] {e.message}")
            except Exception as e:
                print(f"\n[System Error] Unexpected exception: {e}")

    def perform_calculations(self):
        print("\nChoose Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        try:
            op_choice_str = input("Select operation (1-4): ")
            op_choice = InputValidator.parse_menu_choice(op_choice_str, 1, 4)
            
            num1_str = input("Enter first number: ")
            num1 = InputValidator.parse_float(num1_str, "First number")
            
            num2_str = input("Enter second number: ")
            num2 = InputValidator.parse_float(num2_str, "Second number")
            
            op_names = {1: "Addition", 2: "Subtraction", 3: "Multiplication", 4: "Division"}
            op_name = op_names[op_choice]
            
            result = None

            # ==========================================
            # Concept: Exception Handling (try, except, else, finally)
            # ==========================================
            try:
                if op_choice == 1:
                    result = self.calculator.add(num1, num2)
                elif op_choice == 2:
                    result = self.calculator.subtract(num1, num2)
                elif op_choice == 3:
                    result = self.calculator.multiply(num1, num2)
                elif op_choice == 4:
                    result = self.calculator.divide(num1, num2)
            except CalculatorError as err:
                self.logger.log_error(err)
                print(f"\n[Error] {err.message}")
            except Exception as sys_err:
                self.logger.log_error(sys_err)
                print(f"\n[System Failure] {sys_err}")
            else:
                self.logger.log_success(op_name, num1, num2, result)
                print(f"\n[Success] {op_name} Result: {num1} and {num2} = {result}")
            finally:
                print("Calculation process transaction completed.")
                
        except InvalidInputError as e:
            self.logger.log_error(e)
            print(f"\n[Input Error] {e.message}")

    def view_history(self):
        print("\n--- Calculation History ---")
        history = self.logger.get_history()
        if not history:
            print("No successful calculations logged.")
        else:
            for idx, row in enumerate(history, 1):
                print(f"[{idx}] {row['Timestamp']} | {row['Operation']}: {row['Operand1']} and {row['Operand2']} = {row['Result']}")

    def view_errors(self):
        print("\n--- Error Report ---")
        errors = self.logger.get_errors()
        if not errors:
            print("No errors logged.")
        else:
            for idx, err in enumerate(errors, 1):
                print(f"[{idx:02}] {err}")

    def view_statistics(self):
        print("\n--- Summary Statistics ---")
        history = self.logger.get_history()
        errors = self.logger.get_errors()
        
        total_calcs = len(history)
        total_errors = len(errors)
        
        most_common_error = "None"
        if total_errors > 0:
            error_types = []
            for line in errors:
                try:
                    if "]: " in line:
                        parts = line.split("]: ")
                        err_name = parts[1].split(":")[0]
                        error_types.append(err_name)
                except Exception:
                    continue
            if error_types:
                counter = Counter(error_types)
                most_common = counter.most_common(1)
                if most_common:
                    most_common_error = most_common[0][0]
                    
        print(f"Total successful calculations: {total_calcs}")
        print(f"Total errors: {total_errors}")
        print(f"Most common error type: {most_common_error}")


if __name__ == "__main__":
    app = SecureCalculatorApp()
    app.run()
