import pandas as pd

# Loading the CSV file into DataFrame
athletes_df = pd.read_excel('Paris_Olympics.xlsx', sheet_name='Athletes')

# Display all columns and rows for debugging
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print("\nWelcome to the Data Analysis of Paris Olympics 2024.")
print("\nWe can perform the following operations")
print("\nMenu:")
print("\n1: Look at players from a country.")
print("\n2: Look at players from a sport.")
print("\n3: Number of athletes per country")
#print("\n4: Number of m

# Get user's choice
choice = int(input("Enter the selected number: "))

def country():
    # Define the country you are interested in
    country_of_interest = input("Enter country to find all its athletes competing in the Paris Olympics 2024: ").strip().title()

    # Filter the DataFrame for the specific country
    # Create hierarchical index with Sport and Event
    result_country = country_of_interest[['Name', 'Gender', 'Age', 'Sport', 'Event']].set_index(['Sport', 'Event'])
    
    # Print DataFrame with hierarchical index
    print("\nAthletes from", country_of_interest)
    print(result_country.to_string())


    # Print DataFrame without index
    #print("\nAthletes from", country_of_interest)
    #print(result_country.to_string(index=False))

def sport():
    # Define the sport you are interested in
    sport_of_interest = input("Enter sport to find all athletes competing in the Paris Olympics 2024: ").strip().title()

    # Filter the DataFrame for the specific sport
    sport_df = athletes_df[athletes_df['Sport'].str.title() == sport_of_interest]

    # Check if the filtered DataFrame is empty
    if sport_df.empty:
        print(f"\nNo athletes found for the sport: {sport_of_interest}")
    else:
        result_sport = sport_df[['Name', 'Gender', 'Age', 'Country', 'Event']]
        # Print DataFrame without index
        print("\nAthletes competing in", sport_of_interest)
        print(result_sport.to_string(index=False))

def no_of_athletes():
    athletes_per_country = athletes_df.groupby('Country').size()
    print(athletes_per_country)

# Call the appropriate function based on user's choice
if choice == 1:
    country()
elif choice == 2:
    sport()
elif choice ==3:
    no_of_athletes()
else:
    print("Invalid choice. Please select 1 or 2.")

#coaches_df=pd.read_csv("events.csv")
#medalists_df=pd.read_csv("medalists.csv")
#medals_df=pd.read_csv("medals.csv")
#medals_total_df=pd.read_csv("medals_total.csv")
#schedules_df=pd.read_csv("schedules.csv")
#schedules_preliminary_df=pd.read_csv("schedules_preliminary.csv")
#teams_df=pd.read_csv("teams.csv")
#torch_route_df=pd.read_csv("torch_route.csv")
#venues_df=pd.read_csv("venues.csv")
