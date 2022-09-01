def fizz_buzz(a, b):
    sum = 0
    for i in range (a,b+1):
        if (i%3)==0 and (i%5)==0:
            sum = sum + i

    return sum
print (fizz_buzz(2, 20))
def plural_form(n, w1,w2,w3):
    if (n == 1) or (n%10 == 1) and (n//10 != 1) :
        return w1
    elif ((n%10 == 2) or (n%10 == 3) or (n%10 == 4)) and (n//10 != 1):
        return  w2
    else:
        return w3

print(1, plural_form(1, 'яблоко', 'яблока', 'яблок'))
#print(3, plural_form(3, 'яблоко', 'яблока', 'яблок'))
#print(5, plural_form(5, 'яблоко', 'яблока', 'яблок'))
#print(11, plural_form(11, 'яблоко', 'яблока', 'яблок'))
#print(121, plural_form(121, 'яблоко', 'яблока', 'яблок'))
#print(125, plural_form(125, 'яблоко', 'яблока', 'яблок'))
def html(tag, **kwargs):

    def decorator(decorated_function):
        def function_inside_decorator(param):
            result_decorated_function = '<'+ tag
            if len(kwargs)!=0:
                for key in kwargs:
                    result_decorated_function = result_decorated_function + ' '+key+'="'+str(kwargs[key])+'"'
                result_decorated_function = result_decorated_function + '>'
            else:
                result_decorated_function = result_decorated_function + '>'
            result_decorated_function = result_decorated_function + decorated_function(param) + '</'+tag+'>'
            return result_decorated_function
        
        result = function_inside_decorator
        return result
    return decorator

@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)


print(to_string('ссылка на яндекс'))



