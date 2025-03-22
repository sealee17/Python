def process(value):
   
    if isinstance(value,int):
        print('integer')

    elif isinstance(value,str):
        print('string')
    
    else:
        print('???')

process(10)
process('hello')
process([1,2,3])