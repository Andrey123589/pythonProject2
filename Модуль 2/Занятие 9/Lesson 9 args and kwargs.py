def my_func(*args, **kwargs):
    print(args) # Позиционный аргумент
    a  = kwargs.get('a')
    print(kwargs)   # Именной аргумент

my_func(10, 20, 30 ,40 ,50 , 60, a=10,)   # Сначала позиционный, а только потом именнованые

