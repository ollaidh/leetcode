def verify_if_equal(actual, expected, message):
    postfix = ' '.join([message, 'Expected:', str(expected), 'Got:', str(actual)])
    if actual != expected:
        print('\nFAILED test ---', postfix)
    else:
        print('\nOK test -------', postfix)


def run_test(func, func_inp, expected, case_name=''):
    if type(func_inp) is list or type(func_inp) is tuple:
        input_items = []
        for item in func_inp:
            input_items.append(str(item))
        actual = func(*func_inp)
        postfix = ' '.join([case_name, 'Input:', ', '.join(input_items)])
    else:
        postfix = ' '.join([case_name, 'Input:', str(func_inp)])
        actual = func(func_inp)
    verify_if_equal(actual, expected, postfix)
