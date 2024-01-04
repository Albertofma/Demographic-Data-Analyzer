import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')
  df.head()

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df.groupby('race').size()

  # What is the average age of men?
  mask_men = df['sex'] == 'Male'
  average_age_men = round(df[mask_men]['age'].mean(), 1)

  # What is the percentage of people who have a Bachelor's degree?
  percentage_bachelors = round(df['education'].value_counts(normalize=True)[2] * 100, 1)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  # with and without `Bachelors`, `Masters`, or `Doctorate`

  higher_education = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
  salary = df['salary'] == '>50K'
  #Mask for the df that filters education level and salary
  mask = higher_education & salary
  
  lower_education = ~higher_education
  #Simply cases that arent higher_education

  
  # percentage with salary >50K 
  
  higher_education_rich = round(df[mask].shape[0] / df[higher_education].shape[0] * 100, 1)
  #Shape gets a tuple of array of dimensions, in this case (number of rows, number of columns), if we take the first element of the array we get the number of people that meet the criteria.
  
  lower_education_rich = round(df[lower_education][
      df['salary'] == '>50K'].shape[0] / df[lower_education].shape[0] * 100, 1)



  
  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].value_counts().min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  
  num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
  hours_salary = df[(df['hours-per-week'] == min_work_hours)
                    & (df['salary'] == '>50K')]
  rich_percentage = hours_salary.shape[0] / num_min_workers * 100

  # What country has the highest percentage of people that earn >50K?
  
  Amount_of_rich = df[df['salary'] == '>50K']['native-country'].value_counts()
  Population_Country = df['native-country'].value_counts()
  highest_earning_country = (Amount_of_rich / Population_Country * 100).idxmax() 
  #The division is the percentage of rich people per country, idxmax just gets the id (first column in this case) and gets the country name.
  highest_earning_country_percentage = round((Amount_of_rich / Population_Country * 100).max(), 1)
  #Same as above but this method gets the number not the id of the subdataframe

  # Identify the most popular occupation for those who earn >50K in India.
  top_IN_occupation = df[(df['native-country'] == 'India') & (
      df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
        f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
        f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
        f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
        f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage': highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
  }
