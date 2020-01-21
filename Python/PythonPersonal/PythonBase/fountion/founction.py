import ToImport


# 函数模块导入
ToImport.make_pizza(16, 'pepperoni')
ToImport.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#关键字参数
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' +  middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)