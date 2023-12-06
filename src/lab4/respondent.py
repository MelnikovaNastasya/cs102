class Respondent:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Respondent):
            return self.full_name == other.full_name and self.age == other.age
        return False

    def __repr__(self):
        return f"Respondent(full_name='{self.full_name}', age={self.age})"
def sort_respondents(respondents):
    return sorted(respondents, key=lambda x: (-x.age, x.full_name))

def group_respondents(respondents, age_groups):
    age_groups.sort(reverse=True)
    group_respondents_dict = {age_group: [] for age_group in age_groups}
    for respondent in respondents:
        for age_group in age_groups:
            if age_group[0] <= respondent.age <= age_group[1]:
                group_respondents_dict[age_group].append(respondent)
                break
    result = []
    for age_group in age_groups:
        if group_respondents_dict[age_group]:
            group_respondents_dict[age_group] = sort_respondents(group_respondents_dict[age_group])
            group_str = f"{age_group[0]}-{age_group[1]}: "
            group_str += ", ".join([f"{r.full_name} ({r.age})" for r in group_respondents_dict[age_group]])
            result.append(group_str)
    return result

def parse_input(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        respondents = []
        for line in file:
            line = line.strip()
            if line == "END":
                break
            full_name, age = line.split(",")
            respondent = Respondent(full_name, int(age))
            respondents.append(respondent)
    return respondents

def generate_output(output_list):
    return "\n".join(output_list)
def generate_age_groups(age_group_input):
    age_group_values = age_group_input.split()
    age_groups = []
    lower_bound = 0
    for age_group_value in age_group_values:
        upper_bound = int(age_group_value)
        age_group = (lower_bound, upper_bound)
        age_groups.append(age_group)
        lower_bound = upper_bound + 1
    age_groups.append((lower_bound, 123))
    return age_groups

if __name__ == "__main__":
    age_group_input = input("Введите возрастные группы через пробел: ")
    age_groups = generate_age_groups(age_group_input)

    file_path = 'people.txt'
    respondents = parse_input(file_path)
    output = group_respondents(respondents, age_groups)
    output_str = generate_output(output)
    print(output_str)