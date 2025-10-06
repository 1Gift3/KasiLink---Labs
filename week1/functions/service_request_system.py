def prioritize_service_requests(service_type, urgency, customer_tier, location_served):
    '''Determining priority level for service requests'''

    # Based priority from service type
    if service_type in ["plumbing", "electrical", "groundsman"]:
        base_priority = "High"
        priority_points = 30
    elif service_type in ["cleaning", "catering", "tutoring"]:
        base_priority = "Medium"
        priority_points = 20

    elif service_type in ["Extra-hands", "Delivery", "Other"]:
        base_priority = "Low"
        priority_points = 10
    else:
        base_priority = "Unknown"
        priority_points = 0
    #print("Base priority:", base_priority)
    #print("Priority points from service type:", priority_points)
#results = prioritize_service_requests("plumbing", "urgent", "premium", "urban")    
#print("Final priority score:", results)


    # Urgency multiplier
    if urgency == "emergency":
        priority_points = priority_points * 3
        urgency_note = "IMMEDIATE RESPONSE NEEDED"
    elif urgency == "urgent":
        priority_points *= 2
        urgency_note = "Respond within 2 hours"

    else:
        urgency_note = "Schedule within 12 hours"
    print("Priority points after urgency adjustment:", priority_points)

    # customer loyalty bonus
    if customer_tier == "regular":
       priority_points = priority_points + 5
    elif customer_tier == "vip":
       priority_points += 20

    #print("Final priority score:", priority_points)
    #return priority_points

#results = prioritize_service_requests("plumbing", "urgent", "premium", "urban")    
#print("Final priority score:", results)

# Final priority category
    if priority_points >= 80:
        final_priority = "CRITICAL"
    elif priority_points >= 50:
        final_priority = "HIGH"
    elif priority_points >= 30:
        final_priority = "MEDIUM"
    else:
        final_priority = "STANDARD"

    return{ "final_priority": final_priority,
            "priority_points": priority_points,
            "urgency_note": urgency_note,
            "location_note": location_served
            }

request1 = prioritize_service_requests("plumbing", "emergency", "vip", "urban")
request2 = prioritize_service_requests("cleaning", "standard", "regular", "rural")


print("KasiLink Request 1:" , request1)
print("KasiLink Request 2:" , request2)

