fp = None
try:
    fp = open('E:/github/test1/readme.txt', 'rb+')
    fp.write('12345')
except IOError:
    print ('写入不成功')
except Exception:
    print ('操作异常')
else:
    fp.seek(0)
    f = fp.readlines()
    print (f)
finally:
    fp.close()
