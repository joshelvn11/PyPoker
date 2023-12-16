
if __name__ == '__main__':
    start_server = None

    while start_server is None:
        try:
            start_server_input = input('Would you like to start a server? (Y/N)')
        except Exception as e:
            pass
        else:
            if start_server_input == 'Y':
                start_server = True
                print('Starting server')
            elif start_server_input == 'N':
                start_server = False
                print('Joining game')
            else:
                print('Please enter a valid input')
