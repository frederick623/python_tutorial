x = 1
def tmp(y):
    y = 2
    x = 3
    print ("In tmp, y: %s" % y)
    print ("In tmp, x: %s" % x)
    return
tmp(x)
print ("Original x: %s" % x)
