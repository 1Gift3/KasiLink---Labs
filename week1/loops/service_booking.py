def book_service():
    available_services = ["plumbing", "electrical", "cleaning", "gardening"]
    print("kasilink Service Booking system")
    print("Available services:", ", ".join(available_services))
    print("=" * 40)

    # getting valid service choice
    while True:
        try:
            service_choice = input("Choose a service: ").strip().lower()
            if service_choice not in available_services:
                print("Service not available. Please choose from the available services.")
                continue
            # valid choice, break out
            break
        except Exception:
            print("Invalid input. Please try again.")
            continue

    # getting a valid budget
    while True:
        try:
            budget_input = input("Enter your budget (R): R ").strip()
            budget = float(budget_input)
            if budget <= 0:
                raise ValueError("Budget must be a positive number.")
            if budget < 50:
                raise ValueError("Budget too low. Minimum is R50.")
            # valid budget, break out
            break
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter a valid amount.\n")

    print(f"\nBooking confirmed!")
    print(f"    Service: {service_choice.title()}")
    print(f"    Budget: R{budget:.2f}")
    return service_choice, budget


if __name__ == "__main__":
    service, budget = book_service()