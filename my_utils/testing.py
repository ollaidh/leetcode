def verify_if_equal(actual, expected, message):
    postfix = ' '.join([message, 'Expected:', str(expected), 'Got:', str(actual)])
    if actual != expected:
        print('FAILED test ---', postfix)
    else:
        print('OK test -------', postfix)


def run_test(func, func_inp, expected, case_name=''):
    input_items = []
    for item in func_inp:
        input_items.append(str(item))
    if type(func_inp) == 'list' or type(func_inp) == 'tuple':
        actual = func(*func_inp)
        postfix = ' '.join([case_name, 'Input:', ', '.join(input_items)])
    else:
        actual = func(func_inp)
        postfix = ' '.join([case_name, 'Input:', '\"', func_inp, '\"'])
    # postfix = ' '.join([case_name, 'Input:', ', '.join(input_items)])
    verify_if_equal(actual, expected, postfix)
