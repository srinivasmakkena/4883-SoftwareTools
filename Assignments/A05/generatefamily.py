import os
import pandas as pd
import random
from Person import Person
import datetime
currentlocation=os.path.dirname(os.path.abspath(__file__))
current_year = datetime.datetime.now().year
def get_names_raw():
    names_dfs=[]
    for file in os.listdir(currentlocation+'\\resources\\Names\\Raw\\'):
        names_dfs.append(pd.read_csv(currentlocation+'\\resources\\Names\Raw\\'+file))
    combined_df = pd.concat(names_dfs, axis=0, ignore_index=True)
    combined_df.drop_duplicates(subset=['Name','Gender'], inplace=True)
    # print(combined_df)
    
    Female_first_names_df=combined_df[combined_df['Gender'] == 'Female'][['Name',"Gender"]]
    file_path = currentlocation+'\\resources\\Names\\female_first_names.csv'    
    Female_first_names_df.to_csv(file_path, index=False)
    
    Male_first_names_df=combined_df[combined_df['Gender'] == 'Male'][['Name',"Gender"]]
    file_path = currentlocation+'\\resources\\Names\\male_first_names.csv'
    Male_first_names_df.to_csv(file_path, index=False)

    last_names_df = combined_df['Surname']
    last_names_df.drop_duplicates(inplace=True)
    file_path = currentlocation+'\\resources\\Names\\last_names.csv'
    last_names_df.to_csv(file_path, index=False, header=True)
    
    clan_names_df = combined_df['Clan Name']
    clan_names_df.drop_duplicates(inplace=True)
    file_path = currentlocation+'\\resources\\Names\\clan_names.csv'
    clan_names_df.to_csv(file_path, index=False, header=True)

# Sample data for names, last names, and clan names
female_first_names = pd.read_csv(currentlocation+'\\resources\\Names\\female_first_names.csv')['Name']
male_first_names = pd.read_csv(currentlocation+'\\resources\\Names\\male_first_names.csv')['Name']
last_names = pd.read_csv(currentlocation+'\\resources\\Names\\last_names.csv')['Surname']
clan_names = pd.read_csv(currentlocation+'\\resources\\Names\\clan_names.csv')['Clan Name']

def generate_random_death_age():
    age_range = [i for i in range(5,100)]
    probabilities = [(i/2)*0.02 if i<50 else (80/2)*0.01*(1-((i-80)/(20))) for i in range(5,100)]
    # print(dict(zip(age_range,probabilities)))
    death_age = random.choices(age_range, probabilities)[0]
    return death_age

def generate_random_marriage_age():
    probabilities = [(i/2)*0.25 if i<30 else (30/2)*0.02*(1-((i-30)/(100-30))) for i in range(18, 50)]
    age_range = list(range(18, 50))
    marriage_age = random.choices(age_range, probabilities)[0]
    # print(dict(zip(age_range,probabilities)))
    return marriage_age

def generate_random_child_counts_for_couple():
    male_ratio = 0.51  # Male to total ratio
    probabilities = [0.2, 0.35, 0.15] 
    total_children = random.choices(range(0,3), probabilities)[0]
    male_children = round(total_children * male_ratio)
    female_children = total_children - male_children    
    return male_children, female_children

def generate_random_birth_year(parent_byear=None,spouse_byear=None,fspouse_byear=None):
    if parent_byear is not None:
        birth_year = random.randint(parent_byear+20, parent_byear+60)
    elif spouse_byear is not None:
        birth_year = random.randint(spouse_byear-10, spouse_byear-2)
    elif fspouse_byear is not None:
        birth_year = random.randint(fspouse_byear+2, fspouse_byear+10)
    else:
        birth_year = random.randint(1850,1950)
    return birth_year

def are_siblings(person1, person2, family_data):
    if person1.parent_id1 == person2.parent_id1 and person1.parent_id2 == person2.parent_id2:
        return True
    return False

def generate_random_spouse(person, available_males, family_data):
    try:
        for _ in range(100):  # Limit the attempts to prevent an infinite loop
            male = random.choice(available_males)
            if (
                male.last_name != person.last_name
                and person.last_name not in male.last_name
                and male.spouse_id==None
                and not are_siblings(male, person, family_data)  # Check if the male and person are siblings
            ):
                available_males.remove(male)
                person.spouse_id = male.pid  # Assign spouse ID to the person
                male.spouse_id = person.pid  # Assign spouse ID to the male
                return male
    except:pass
    return  Person(name=random.choice(male_first_names),generation=person.generation,last_name=random.choice(last_names),clan=random.choice(clan_names),gender="Male",byear=generate_random_birth_year(spouse_byear=person.byear))
    
def generate_random_female_spouse(person, available_females, family_data):
    try:
        for _ in range(100):  # Limit the attempts to prevent an infinite loop
            female = random.choice(available_females)
            if (
                female.last_name != person.last_name
                and person.last_name not in female.last_name
                and not are_siblings(female, person, family_data)
                  and female.spouse_id==None  # Check if the male and person are siblings
            ):
                available_females.remove(female)
                person.spouse_id = female.pid  # Assign spouse ID to the person
                female.spouse_id = person.pid  # Assign spouse ID to the male
                return female
    except:
        pass
    return  Person(name=random.choice(female_first_names),clan=random.choice(clan_names),generation=person.generation,last_name=random.choice(last_names),gender="Female",byear=generate_random_birth_year(fspouse_byear=person.byear))
    

def get_random_family_data(no_generations=1):
    family_data = []
    available_males = []
    available_females = []

    # Generation 1
    lastname_1st_gen = random.choice(last_names)

    parent1 = Person(
        name=random.choice(male_first_names),
        last_name=lastname_1st_gen,
        gender="Male",
        generation=1,
        byear=generate_random_birth_year(),
        mage=generate_random_marriage_age(),
        clan=random.choice(clan_names)
    )
    parent1.myear = parent1.byear + parent1.mage

    parent2 = Person(
        name=random.choice(female_first_names),
        last_name=lastname_1st_gen,
        gender="Female",
        generation=1,
        clan=parent1.clan,
        spouse_id=parent1.pid,
        byear=generate_random_birth_year(spouse_byear=parent1.byear)
    )
    parent2.myear = parent1.myear
    parent2.mage = parent2.myear - parent2.byear
    parent1.spouse_id = parent2.pid

    parent1.dage = generate_random_death_age()
    parent2.dage = generate_random_death_age()
    family_data.extend([parent1, parent2])

    
    for generation in range(1, no_generations + 1):
        new_generation = []
        for person in family_data:
            child_counts = list(generate_random_child_counts_for_couple()) 
            for _ in range(sum(child_counts)):
                is_male = child_counts[0] > 0
                # if is_male and person.gender == "Male":
                last_name = person.last_name  
                # else:
                #     last_name = random.choice(last_names)
                child = Person(
                    name=random.choice(male_first_names) if is_male else random.choice(female_first_names),
                    last_name=last_name,
                    gender="Male" if is_male else "Female",
                    generation=generation,
                    clan=person.clan,
                    byear=generate_random_birth_year(parent_byear=person.byear),
                    parent_id1=person.pid,
                    parent_id2=person.spouse_id,
                    mage=generate_random_marriage_age()
                )
                available_females.append(child) if child.gender=="Female" else available_males.append(child)
                child.myear = child.byear + child.mage


                if child.gender == "Female" and child.spouse_id is None:
                    spouse = generate_random_spouse(child, available_males, family_data)
                    if spouse:
                        child.spouse_id = spouse.pid
                        spouse.spouse_id = child.pid
                        child.myear = spouse.myear  # Match spouse's marriage year
                elif child.gender == "Male" and child.spouse_id is None:
                    spouse = generate_random_female_spouse(child, available_females, family_data)
                    if spouse:
                        child.spouse_id = spouse.pid
                        spouse.spouse_id = child.pid
                        child.myear = spouse.myear  # Match spouse's marriage year
                new_generation.append(child)
                child_counts[0] -= 1 if is_male else 0
                child_counts[1] -= 0 if is_male else 1

        for person in new_generation:
            person.dage = generate_random_death_age()

        family_data.extend(new_generation)
        # for i in Person.all_persons:
        #     if i.dage:
        #         i.dyear=int(i.byear+i.dage)
        #     if i.mage:
        #         i.myear=int(i.mage+i.byear)
        df = pd.DataFrame(person.__dict__ for person in Person.all_persons)
        
        
        df['dyear'] = pd.to_numeric(df['byear']+df['dage'], errors='coerce').astype(pd.Int64Dtype())
        df['myear'] = pd.to_numeric(df['byear']+df['mage'], errors='coerce').astype(pd.Int64Dtype())
        df['dyear'] = df['dyear'].apply(lambda x: x if pd.notna(x) and x < current_year else None)
        df['myear'] = df['myear'].apply(lambda x: x if pd.notna(x) and x < current_year else None)
        df.to_csv(currentlocation+'//family_data.csv', index=False)


# get_random_family_data()
# print(generate_random_death_age())
# print(generate_random_marriage_age())
# print(generate_random_child_counts_for_couple())