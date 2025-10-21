

def send_request(url, *args, **kwargs):

    print(f'Sending request to {url}')

    print('args')
    for index, a_param in enumerate(args):
        print(f'Args: {index} has value {a_param}')


    print('kwargs')
    print(kwargs)



print(send_request('hht_google.com?query_params=', 'eather,', 'cinema5,', 'netflix',
                   body=[1,2,3], path='some_path'))

# print('asdasd', 1,2,4,5,6,78,54,'asdasd', 'asdas', sep=' |--| ')