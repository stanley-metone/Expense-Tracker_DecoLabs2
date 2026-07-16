# 💰 Expense Tracker — Python Programming (Project 2)

A command-line expense tracker that continuously accepts expense entries, accumulates them into a running total, and prints a final financial summary. Built to demonstrate core backend logic: state management, the accumulator pattern, defensive coding, and sentinel-controlled loops.

---

## 📌 Goal

> Create a script where users enter expense amounts (e.g., `100`, `50`, `20`). The program adds them up and displays the **Total Spent**.

This isn't "simple arithmetic" — it's **data accumulation**: the foundation every backend system (bank ledgers, e-commerce carts, analytics pipelines) is built on.


You'll be prompted to enter expenses one at a time. Type `done` at any point to stop and see your summary.

### Example Session

```
Enter an expense amount, or type 'done' to finish.

Expense #1 (or 'done'): 100
  ✅  Logged $100.00  |  Running total: $100.00

Expense #2 (or 'done'): 50
  ✅  Logged $50.00  |  Running total: $150.00

Expense #3 (or 'done'): ten
  ⚠  Invalid input: 'ten' is not a number. Please try again.

Expense #3 (or 'done'): 20
  ✅  Logged $20.00  |  Running total: $170.00

Expense #4 (or 'done'): done

  🛑  Sentinel received. Closing the ledger...

==================================================
   FINAL REPORT
==================================================
Transactions logged : 3
Total Spent         : $170.00
Average Expense     : $56.67
Highest Expense     : $100.00
Lowest Expense      : $20.00
==================================================
```

---

## 🧠 Key Concepts Implemented

| Concept | Where it lives | Why it matters |
|---|---|---|
| **Accumulator Pattern** | `total += result` | The heartbeat of any ledger: `State(new) = State(old) + Input`. |
| **IPO Model** (Input → Process → Output) | `get_expense_input()` → `track_expenses()` → `display_summary()` | Separates *gathering* data, *transforming* it, and *presenting* it — a Model/View split. |
| **Defensive Coding** | `try/except ValueError` in `get_expense_input()` | "Garbage in = garbage out." Non-numeric input never reaches the accumulator. |
| **Sentinel Values** | `SENTINEL = "done"` | A clean, explicit way to break a `while True` loop instead of forcing the user to guess how many entries to enter. |
| **State vs. Iteration** | `total`, `count`, `history` initialized **outside** the loop | Variables declared before the loop persist across iterations (memory). Anything declared *inside* the loop resets every pass (amnesia) — a classic beginner bug this design avoids. |

---

## 🗂️ Project Structure

```
expense_tracker/
├── expense_tracker.py   # Main script
└── README.md            # This file
```

---

## 🛡️ Quality Checklist (per DecodeLabs Guidelines)

- [x] **Stability** — Handles 5+ consecutive transactions without breaking.
- [x] **State** — `total` is initialized *outside* the loop.
- [x] **Defense** — Catches `ValueError` on invalid/non-numeric input, and rejects negative numbers.
- [x] **Control** — A sentinel value (`done`) breaks the loop and prints the final total.

---

## 🔍 Possible Extensions

- Persist expenses to a `.csv` or `.json` file between runs.
- Add expense categories (food, transport, etc.) and per-category subtotals.
- Add a monthly budget limit with a warning when exceeded.
- Wrap the core logic in a class (`ExpenseTracker`) for reuse in a larger app.

---

## 📖 About This Track

This project is Milestone 2 of the **Python Programming Industrial Training Kit** by **DecodeLabs
