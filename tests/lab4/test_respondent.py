import unittest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)
from src.lab4.respondent import Respondent, group_respondents, generate_age_groups, generate_output, parse_input, sort_respondents


class TestRespondent(unittest.TestCase):

    def test_sort_respondents(self):
        respondents_list = [
            Respondent(full_name='Кошельков Захар Брониславович', age=30),
            Respondent(full_name='Дьячков Нисон Иринеевич', age=25),
            Respondent(full_name='Иванов Варлам Якунович', age=40)
        ]

        sorted_respondents = sorted(respondents_list, key=lambda respondent: respondent.full_name)
        expected_sorted_respondents = [
            Respondent(full_name='Дьячков Нисон Иринеевич', age=25),
            Respondent(full_name='Иванов Варлам Якунович', age=40),
            Respondent(full_name='Кошельков Захар Брониславович', age=30)
        ]

        self.assertEqual(sorted_respondents, expected_sorted_respondents)

    def test_group_respondents(self):
        respondents = [
            Respondent("Ярилова Розалия Трофимовна", 29),
            Respondent("Соколов Андрей Сергеевич", 15),
            Respondent("Егоров Алан Петрович", 7),
        ]
        age_groups = [(26, 35), (0, 18)]
        grouped_respondents = group_respondents(respondents, age_groups)
        self.assertEqual(grouped_respondents, [
            '26-35: Ярилова Розалия Трофимовна (29)' ,
            '0-18: Соколов Андрей Сергеевич (15), Егоров Алан Петрович (7)'
        ])

    def test_generate_age_groups(self):
        age_group_input = "20 30 40"
        age_groups = generate_age_groups(age_group_input)
        self.assertEqual(age_groups, [
            (0, 20),
            (21, 30),
            (31, 40),
            (41, 123)
        ])

    def test_parse_input(self):
        file_path = 'test_input.txt'
        expected_respondents = [
            Respondent(full_name='Кошельков Захар Брониславович', age=105),
            Respondent(full_name='Дьячков Нисон Иринеевич', age=88),
            Respondent(full_name='Иванов Варлам Якунович', age=88)
        ]
        result = parse_input(file_path)
        self.assertEqual(result, expected_respondents)

    def test_generate_output(self):
        output_list = [
            'Кошельков Захар Брониславович',
            'Дьячков Нисон Иринеевич',
            'Иванов Варлам Якунович'
        ]
        output = generate_output(output_list)
        expected_output = 'Кошельков Захар Брониславович'+'\n''Дьячков Нисон Иринеевич'+'\n''Иванов Варлам Якунович'
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()