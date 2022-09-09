class Point:
    color = 'blue'
    circle = 2


hasattr(Point, 'color')
# return True

hasattr(Point, 'prop')
# return False

getattr(Point, 'color')
# return 'blue'

getattr(Point, 'not_arg_in_class')
# return Exception AttributeError

getattr(Point, 'not_arg_in_class', False)
# return False

print(Point.__dict__)
# return mappingproxy({'__module__': '__main__', 'color': 'blue', 'circle': 2,
# '__dict__': <attribute '__dict__' of 'Point' objects>,
# '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None})

a = Point()
a.color = 'red'
print(a.__dict__)
# return {'color': 'red'}

delattr(a, 'color')
print(a.color)
# return 'blue'
print(a.__dict__)
# return {}

setattr(a, 'color', 'red')
# a.color = 'red'
print(a.__dict__)
# return {'color': 'red'}

del a.color
print(a.color)
