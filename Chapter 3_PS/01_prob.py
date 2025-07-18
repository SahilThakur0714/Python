# WAP to fill in a letter template given below with name and date
letter = '''Dear <|Name|>,
You are selected,
<|Date|>
'''
print(letter.replace("<|Name|>", "Sahil Thakur").replace("<|Date|", "01 July 2025"))