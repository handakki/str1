def filename():
    filename = input('Please input file name:')
    if filename == '123':
        raise NameError('input file name error')
    return filename
while True:
    try:
        filename = filename()
        print ('filename is %s'%filename)
        break
    except NameError:
        print ('please input file name again!')