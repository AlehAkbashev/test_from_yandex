phone_number = input()


def number_is_ok(number, num_len):
    try:
        int(number[0:3])        # 9154538575
        if number[-1] != '-':
            number = number.split('-')
            number = ''.join(number)
            try:
                int(number[3:])
                real_number = number
                if len(number[3:]) == num_len:
                    print('8 (' + real_number[0:3] + ') ' + real_number[3:6] + '-' +
                          real_number[6:8] + '-' + real_number[8:])
                else:
                    print('error')
            except ValueError:
                print('error')
        else:
            print('error')
    except ValueError:          # (915)4538575
        if number[0] == '(' and number[4] == ')':
            try:
                int(number[1:4])
                if number[5] != '-' and number[-1] != '-':
                    number = number.split('-')
                    number = ''.join(number)
                    try:
                        int(number[5:])
                        real_number = number
                        if len(number[5:]) == num_len:
                            print('8 (' + real_number[1:4] + ') ' + real_number[5:8] + '-' +
                                  real_number[8:10] + '-' + real_number[10:])
                        else:
                            print('error')
                    except ValueError:
                        print('error')
                else:
                    print('error')
            except ValueError:
                print('error')
        else:
            print('error')


phone_number = ''.join(phone_number.split(' '))
if '--' in phone_number or '- ' in phone_number or ' -' in phone_number:
    print('error')
elif phone_number[0] == '8':
    number_is_ok(phone_number[1:], 7)
elif phone_number[0:2] == '+7':
    number_is_ok(phone_number[2:], 7)
else:
    print('error')

