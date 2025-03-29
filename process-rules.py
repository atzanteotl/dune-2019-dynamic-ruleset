from jinja2 import Environment, FileSystemLoader

import csv
import json
import markdown


def csv_to_json_rules(filepath):
    sections_dict = {}
    
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')  # Assuming it's tab-separated

        for row in reader:
            section = row['section'].strip()
            subsection = row['subsection'].strip()
            rule_entry = {
                'class1': row['class1'].strip() or None,
                'class2': row['class2'].strip() or None,
                'class3': row['class3'].strip() or None,
                'faction': row['faction'].strip() or None,
                'depth': int(row['depth']),
                'text': markdown.markdown(row['rule'].strip())[3:-4]
            }

            if section not in sections_dict:
                sections_dict[section] = {}

            if subsection not in sections_dict[section]:
                sections_dict[section][subsection] = []

            sections_dict[section][subsection].append(rule_entry)

    # Convert nested dict to desired JSON format
    result = []
    for section_title, subsections in sections_dict.items():
        section_obj = {
            'title': section_title,
            'subsections': []
        }
        for subsection_title, rules in subsections.items():
            section_obj['subsections'].append({
                'title': subsection_title,
                'rules': rules
            })
        result.append(section_obj)

    return result


if __name__ == '__main__':
    csv_filepath = 'rules.csv'
    sections = csv_to_json_rules(csv_filepath)

    # process the templates
    environment = Environment(loader=FileSystemLoader("."))
    template = environment.get_template("template.html")

    print(sections[1])

    content = template.render(sections[1])

    with open('index.html', mode="w", encoding="utf-8") as message:
        message.write(content)        

