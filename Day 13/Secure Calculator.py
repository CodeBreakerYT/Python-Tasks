#!/usr/bin/env python3
import datetime, os, sys

# Concept: Custom Exceptions
class CalculatorError(Exception): pass
class DivisionByZeroError(CalculatorError): pass
class InvalidInputError(CalculatorError): pass

# Concept: OOP Basics
def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y):
    if y == 0: raise DivisionByZeroError()
    return x / y

HIST = "history.txt"
ERR_LOG = "errors.log"

# Concept: File Handling
def log_ok(op, x, y, res):
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HIST, "a") as f:
        f.write(f"{t} | {op}: {x} and {y} = {res}\n")

# Concept: Logging
def log_err(err, msg):
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ERR_LOG, "a") as f:
        f.write(f"[{t}] {err}: {msg}\n")

# Concept: Input Validation
def get_num(p):
    val = input(p).strip()
    if not val: raise InvalidInputError("Empty input")
    try: return float(val)
    except ValueError: raise InvalidInputError(f"Invalid number: {val}")

def get_choice(p, low, high):
    try:
        val = int(input(p).strip())
        if not (low <= val <= high): raise InvalidInputError("Out of range")
        return val
    except ValueError: raise InvalidInputError("Not an integer")

def calculate():
    print("\nSelect Operation\n1. Add\n2. Sub\n3. Mul\n4. Div")
    # Concept: Exception Handling
    try:
        ch = get_choice("Choice (1-4): ", 1, 4)
        x = get_num("First: ")
        y = get_num("Second: ")
        match ch:
            case 1: res, op = add(x, y), "Add"
            case 2: res, op = sub(x, y), "Sub"
            case 3: res, op = mul(x, y), "Mul"
            case 4: res, op = div(x, y), "Div"
    except CalculatorError as e:
        log_err(e.__class__.__name__, e.args[0] if e.args else str(e))
        print(f"\nError: {e.args[0] if e.args else str(e)}")
    except Exception as e:
        log_err(e.__class__.__name__, str(e))
        print(f"\nSystem Error: {e}")
    else:
        log_ok(op, x, y, res)
        print(f"\nSuccess: {res}")
    finally:
        print("Done.")

def view_history():
    print("\nHistory\n")
    if os.path.exists(HIST):
        with open(HIST, "r") as f: print(f.read().strip())

def view_errors():
    print("\nErrors\n")
    if os.path.exists(ERR_LOG):
        with open(ERR_LOG, mode="r", encoding="utf-8") as f: print(f.read().strip())

def view_stats():
    print("\nStats\n")
    calcs, errs, types = 0, 0, []
    if os.path.exists(HIST):
        with open(HIST, "r") as f: calcs = len(f.readlines())
    if os.path.exists(ERR_LOG):
        with open(ERR_LOG, "r") as f:
            for line in f:
                if "]" in line:
                    errs += 1
                    try: types.append(line.split("]")[1].split(":")[0].strip())
                    except: pass
    common = max(set(types), key=types.count) if types else "None"
    print(f"Calculations: {calcs}\nErrors: {errs}\nCommon: {common}")

# Concept: Menu-Driven Programming
def main():
    while True:
        print("\nMenu\n1. Calculate\n2. History\n3. Errors\n4. Stats\n5. Exit")
        try:
            ch = get_choice("Choice (1-5): ", 1, 5)
            match ch:
                case 1: calculate()
                case 2: view_history()
                case 3: view_errors()
                case 4: view_stats()
                case 5: sys.exit(0)
        except InvalidInputError as e:
            print(f"\nError: {e.args[0]}")

if __name__ == "__main__":
    main()
