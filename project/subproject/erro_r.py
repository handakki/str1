def safe_float(obj):
    try:
        retval = float(obj)
    except (Exception):
        retval = '参数必须是数值或者字符串'
    return retval
print (safe_float('xyz'))
print (safe_float(()))
print (safe_float('500.26'))
print (safe_float(200))
print (safe_float(5.002000))