#issue_type = "pricing"
issue_type = input("What issue are you facing? (delivery/technical/pricing): ").lower()

# Valid issue types
valid_issues = ["delivery", "technical", "pricing"]

if issue_type not in valid_issues:
    response = "Invalid input! Please enter one of the following: delivery, technical, or pricing."
elif issue_type == "delivery":
    response = "Our delivery team will update you in just a while"
elif issue_type == "technical":
    response = "Please describe your technical issue in detail, and our support team will get back to you shortly."
elif issue_type == "pricing":
    response = "For pricing inquiries, please visit our pricing page or contact our sales team."

print(response)