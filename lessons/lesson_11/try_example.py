

def division(number):
    return 1/number


list_of_numbers = [1, None, 0, 5]

for number in list_of_numbers:

    no_errors_found = False
    try:
        print(division(number))
    except ValueError:
        print('ValueError')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except Exception:
        print('Exception')
    else:
        no_errors_found = True
        print('No error found')
    finally:
        if no_errors_found:
            pass
        else:
            print('finally')
        print('-'*10)