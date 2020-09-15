q_dict = {
    'group_initial': 'GSK',
    'name': 'jakdu',
    'email': 'jakdu@gmail.com',
    'phone': '010-5671-3767'
}

for q in q_dict:
    print(**{q: q_dict[q]})
