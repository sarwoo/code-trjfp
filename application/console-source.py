from source import Source

def parse_category(num: int):
    cat = Source.Category
    cats = [cat.HOSPITALITY, cat.PRIVATE, cat.RDC, cat.RETAIL]
    return cats[num - 1]

inp_name = input("Enter company name of the source: ")
inp_category_num = int(input("Enter source category number [1]:hospitality, [2]:private, [3]:rdc or [4]:retail: "))


category = parse_category(inp_category_num)
Source(inp_name, category)
print(Source.all)