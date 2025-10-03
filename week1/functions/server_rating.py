def server(completed_services, rating, response_time):
    """Calculate server performance score (0-10)"""

    if completed_services > 100:
        base_score = 4
    elif completed_services > 50:
        base_score = 3
    elif completed_services > 20:    
        base_score = 2
    else:
        base_score = 1

    rating_score = rating * 8 # we convert 5-star to 40 points
    print("rating_score:", rating_score)

    if response_time < 1:
        time_bonus = 20
    elif response_time < 6:
        time_bonus = 10
    else:
        time_bonus = 0
    print("time_bonus:", time_bonus)    

    total_score = base_score + rating_score + time_bonus
    return total_score

# Test the function
seller1 = server(120, 4.5, 2)
print("Seller 1 score:", seller1)
seller2 = server(30, 4.0, 0.5)
print("Seller 2 score:", seller2)

print(f"Kasilink seller 1 score: {seller1}/100")
print(f"Kasilink seller 2 score: {seller2}/100")