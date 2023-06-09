import re
# esse import tem a finalidade de achar regular expressions dentro do seu codigo

import pdb

text = 'the agenti phone number is 408-555-1234. Call soon!'

print('phone' in text)

pattern = 'phone'
re.search(pattern, text)

pattern = 'not in text'

re.search(pattern, text)

pattern = 'my phone, my phone twice'
match = re.search(pattern, text)

matches = re.findall('phone', pattern)
# encontra todas as ocorencias daquela palavra na sua string


for match in re.finditer('phone', pattern):
    print(match.span())
# mostra a localização do re que voce quer em toda a string



text = 'my phone number is 408-555-7777'
phone = re.search(r'\d{3}-\d{3}-\d{4}',text)


phone_pattern = re.compile(r'(d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)



cat_dog = re.search('cat|dog','the cat is here')
at = re.findall(f'...at', 'the cat in the hat sat there')

signal_let = re.findall(r'\d', 'the number is 2')




phrase = 'there are 3 numbers numbers 34 indide 5 this sentence'
pattern = r'[^\d]'

re.findall(pattern,phrase)













pdb.set_trace()