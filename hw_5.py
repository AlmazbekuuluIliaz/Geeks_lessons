Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

del Geeks['bag']

Geeks['address'] = '9 МКР, УЛ. СУЕРКУЛОВА 10Б, ЖК “ТУМАР”, ЦОКОЛЬНЫЙ ЭТАЖ'

Geeks['phone'] = '+996 (557) 05 2018'
Geeks['instagram'] = '@geeks_edu'

additional_courses = ['Backend', 'Frontend', 'UX/UI']
Geeks['courses'].extend(additional_courses)
Geeks['courses'] = set(Geeks['courses'])

Geeks['founding_date'] = '2018 год'

num_courses = len(Geeks['courses'])
print("Количество курсов:", num_courses)

for key, value in Geeks.items():
    print(key, ":", value)