#Kasilink matches services to specific locations and areas
def analyse_service_areas(provider_name,services_offered, areas_served):
    '''Analyse and format service area information'''

    provider_name = provider_name.strip().title()

    # Process services
    services_list = [service.strip().lower() for service in services_offered.split(",")]
    services_formatted = ', '.join([service.title() for service in services_list])

    # Process areas
    areas_list = [area.strip().title() for area in areas_served.split(",")]
    areas_formatted = ', '.join(areas_list)

    # Generate availability summary
    total_areas = len(areas_list)
    total_services = len(services_list)

    summary = f'''🔧 **{provider_name} Service Analysis**

        📋 Services Offered: {services_formatted}
        🌍 Areas Served: {areas_formatted} 
        📊 Coverage: {total_areas} areas, {total_services} services

        📍 Quick Areas: {', '.join(areas_list[:3])}{'...' if total_areas > 3 else ''}
            """.strip()'''
    
    # checking if provider serves high demand areas
    high_demand_areas = ["Soweto", "Alexandra", "Tembisa", "Sebokeng", "Vanderbijlpark"]
    served_high_demand = [area for area in areas_list if area in high_demand_areas]


    # checking to see if provider serves high demand areas
    high_demand_note = ["Soweto", "Alexandra", "Tembisa", "Sebokeng", "Vanderbijlpark"]

    summary += f"\n\n{high_demand_note}"

    return{"summary": summary,
           "services_count": total_services,
           "areas_count": total_areas,
           "serves_high_demand":len(served_high_demand) > 0
           }
    # Test area analysis
provider_analysis = analyse_service_areas(" thabo's repairs ", " plumbing, electrical , cleaning ", " Soweto, Midrand, Sandton, Alexandra" )
print("Kasilink Service Area Analysis")
print( "=" * 40)
print(provider_analysis["summary"])
print(f"\n Stats:{provider_analysis['services_count']} services,"
       f"{provider_analysis['areas_count']} areas served,"
       f"High Demand Areas: {provider_analysis['serves_high_demand']}")


