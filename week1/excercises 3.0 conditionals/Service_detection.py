monthly_service = 25

if monthly_service < 50:
    tier = "Starter"
    benefit = "They learning to be of service"
elif monthly_service < 200:
    tier = "Growing"
    benefit = "Flow is strting to gain"
elif monthly_service < 300:
    tier = "Service Provider"
    benefit = "Flow is starting to gain"
else: 
    tier = "Enterprise"
    benefit = "They live to service others"

print(f"Kasilink server tier: {tier}")
print(f"Benefit: {benefit}")