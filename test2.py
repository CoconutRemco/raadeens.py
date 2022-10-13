def getWelcome(welcomeTo:str='town') -> str:
    return 'Welcome to function '+welcomeTo


where = 'space'
message = getWelcome(where)
print(message)