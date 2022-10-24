from datetime import datetime


def logger(function):
    def wrapper(*args, **kwargs):
        log = f' {datetime.now(tz=None)} вызвана функция {function.__name__} c аргументами {args}'
        with open("logs.txt", "w", encoding="utf-8") as f:
            f.write(log + '\n')
        result = function(*args, **kwargs)
        return result
    return wrapper


def logger2(path):
    def outer(function):
        def wrapper(*args, **kwargs):
            log = f' {datetime.now(tz=None)} вызвана функция {function.__name__} c аргументами {args}'
            with open(path, "a", encoding="utf-8") as f:
                f.write(log + '\n')
            result = function(*args, **kwargs)
            return result
        return wrapper
    return outer


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    path = r' '


    @logger
    @logger2(path)
    def flat_generator(my_list):
        for i in my_list:
            for j in i:
                yield j


    for item in flat_generator(nested_list):
        print(item)
