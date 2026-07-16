"""
Expense Tracker
---------------
DecodeLabs Industrial Training Kit — Project 2

Goal:
    Continuously accept expense amounts from the user, accumulate them
    into a running total, and display the final total when the user
    signals they are done.

Core concepts demonstrated:
    1. The Accumulator Pattern  -> total = total + new_expense
    2. The IPO Model            -> Input -> Process -> Output
    3. Defensive Coding         -> try/except around type conversion
    4. Sentinel Values          -> a special input ("done") that
                                    breaks the infinite loop cleanly
    5. State vs. Iteration      -> "total" lives OUTSIDE the loop so
                                    it survives every pass ("memory"),
                                    while loop-local variables reset
                                    each iteration ("amnesia").
"""

SENTINEL = "done"


def get_expense_input(prompt: str):
    """
    Prompt the user once for an expense amount.

    Returns:
        float  -> a valid, non-negative expense amount
        None   -> the user typed the sentinel value ("done")
        False  -> the input was invalid (not a number)

    This function is the "Gatekeeper" (Phase 1 of the IPO model):
    nothing reaches the accumulator unless it has been validated.
    """
    raw = input(prompt).strip()

    if raw.lower() == SENTINEL:
        return None

    try:
        amount = float(raw)
    except ValueError:
        print(f"  ⚠  Invalid input: '{raw}' is not a number. Please try again.\n")
        return False

    if amount < 0:
        print("  ⚠  Expenses can't be negative. Please try again.\n")
        return False

    return amount


def track_expenses():
    """
    The Core Logic Engine (Phase 2 of the IPO model).

    Runs the continuous audit loop (while True), applies the
    accumulator pattern to build up the running total, and exits
    gracefully via the sentinel value.
    """
    total = 0.0        # <-- STATE: initialized OUTSIDE the loop (memory)
    count = 0          # how many valid expenses were logged
    history = []        # keeps a receipt trail for the summary/output phase

    print("=" * 50)
    print("   💰  EXPENSE TRACKER — DecodeLabs Project 2")
    print("=" * 50)
    print(f"Enter an expense amount, or type '{SENTINEL}' to finish.\n")

    while True:
        result = get_expense_input(f"Expense #{count + 1} (or '{SENTINEL}'): ")

        if result is False:
            # Invalid input — loop again without touching total/count
            continue

        if result is None:
            # Sentinel detected — the "kill switch" — break the loop
            print("\n  🛑  Sentinel received. Closing the ledger...\n")
            break

        # --- THE ACCUMULATOR PATTERN ---
        # State(new) = State(old) + Input
        total += result
        count += 1
        history.append(result)

        print(f"  ✅  Logged ${result:.2f}  |  Running total: ${total:.2f}\n")

    return total, count, history


def display_summary(total: float, count: int, history: list):
    """
    Phase 3: Output — decoupled from the processing logic (Model/View
    separation). This function only ever *displays* data; it never
    mutates it.
    """
    print("=" * 50)
    print("   FINAL REPORT")
    print("=" * 50)

    if count == 0:
        print("No expenses were logged. Nothing to report.")
        return

    average = total / count

    print(f"Transactions logged : {count}")
    print(f"Total Spent         : ${total:.2f}")
    print(f"Average Expense     : ${average:.2f}")
    print(f"Highest Expense     : ${max(history):.2f}")
    print(f"Lowest Expense      : ${min(history):.2f}")
    print("=" * 50)


def main():
    total, count, history = track_expenses()
    display_summary(total, count, history)


if __name__ == "__main__":
    main()
