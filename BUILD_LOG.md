# KasiLink Build Log

Week of Oct 1–4, 2025 — KasiLink & My Python Roadmap
This week was a return to structure and purpose.
 I revisited the core of my work on KasiLink, rebuilding the authentication flow, fixing test coverage, and ensuring JWT integration works smoothly for protected routes.
At the same time, I realigned my entire learning journey around Python, moving from fundamentals to application — APIs, databases, and security — the backbone of KasiLink’s future.
What stood out most wasn’t just the code, but the clarity:
“Coding is more than skill — it’s service. You build systems that help others function better.”

Next week’s focus:
 🔹 Revisiting core Python exercises (via my new learning repo)
 🔹 Applying lessons directly to KasiLink’s backend structure
 🔹 Continuing the mission: making KasiLink a system of service — for communities, businesses, and individuals


Build Log: October 7, 2025
File: service_booking.py
Focus: Fixing logical flow errors in user input validation and adding module safeguards.

Issues Identified:

Premature Loop Termination in Service Selection:

Root Cause: The loop used a break statement when a user selected an unavailable service. This would exit the validation loop entirely instead of re-prompting, causing execution to continue with an undefined service variable.

Effect: The script would either crash or invoke book_service() with incorrect data.

Faulty Budget Validation Logic:

Root Cause: The budget input loop had break statements placed after raise ValueError(), making them unreachable. The flow and indentation also allowed for invalid inputs to be accepted in certain cases.

Effect: The budget validation was not robust, potentially allowing execution to proceed with a budget of 0 or a non-float value.

Unconditional Script Execution:

Root Cause: The script ended with a direct call to book_service(), which would run immediately upon module import.

Effect: Made the module unsuitable for importing into other projects without triggering the interactive prompts.

Changes Implemented:

Service Choice Loop (service_choice):

Replaced the break on invalid choice with continue, forcing the loop to reiterate and prompt the user again.

A break is now only executed once a valid service from the list is selected.

The except block now specifically catches the ValueError and uses continue to re-prompt.

Before (Problematic):

python
if service_choice in available_services:
    service = service_choice
    break
else:
    print("Service not available.")
    break  # This was the error: exiting the loop on invalid input.
After (Fixed):

python
if service_choice in available_services:
    service = service_choice
    break  # Correct: only break on valid input.
else:
    print("Service not available. Please choose from the list.")
    continue  # Correct: go back to the start of the loop.
Budget Validation Loop (budget):

Separated input reading (budget_input) from conversion (float(budget_input) for clearer control flow.

Removed the unreachable break statements. A ValueError is now raised explicitly and caught by the except block, which then re-prompts the user.

The loop only breaks after a valid float is successfully parsed and passes the > 0 check.

Module Import Protection:

Wrapped the primary execution call in if __name__ == "__main__":.

This ensures that service, budget = book_service() only runs when the script is executed directly, not when it is imported as a module.

Added:

python
if __name__ == "__main__":
    service, budget = book_service()
    # ... subsequent logic ...
Additional Feature / Refinement:

Location Formatting: Implemented a clean, one-liner to format a list of service locations for display.

', '.join([loc.title() for loc in available_locations])

Explanation: The list comprehension [loc.title() for loc in available_locations] applies the .title() method to each string in the list, capitalizing the first letter of each word. The ', '.join(...) method then takes this transformed list and combines its elements into a single, neatly formatted string separated by commas.

Outcome:
The service_booking.py module now has robust, user-friendly input validation. It handles errors gracefully, maintains correct control flow, and is structured as a reusable component. The code is more predictable and less prone to runtime failures due to invalid user input.