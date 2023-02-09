def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a = []
    for i in data.split(','):
        a.append(int(i))
    return a
f = open("txt_file/data01.txt").read()

print(main(f))
