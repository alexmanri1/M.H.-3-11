OK_FORMAT=True
test = {   'name': 'q1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(my_info, dict)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(my_info) == 0\nFalse', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert isinstance(my_info["name"], str) and len(my_info["name"]) > 0\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert isinstance(my_info["surname"], str) and len(my_info["surname"]) > 0\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> isinstance(my_info["year_of_birth"], int)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert isinstance(my_info["month_of_birth"], int) and ( 1 <=  my_info["month_of_birth"] <= 12)\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
