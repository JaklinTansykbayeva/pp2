#Regex ex1
import re

def match_ab(string):
    pattern = r'ab*'
    if re.fullmatch(pattern, string): #Проверяет, соответствует ли вся строка шаблону рег выр
        return True
    return False

print(match_ab("abbb"))  
print(match_ab("a"))    
print(match_ab("b"))     
  

#Regex ex2
def match_ab_two_to_three(string):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, string):
        return True
    return False
print(match_ab_two_to_three("abb"))  
print(match_ab_two_to_three("abbb")) 
print(match_ab_two_to_three("ab"))   

#Regex ex3
def find_lowercase_underscore(string):  #последовательности строчных букв, соединённых подчеркиванием
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, string) #находит все подстроки и возвращает их в виде списка.

print(find_lowercase_underscore("a_b c_d e_f"))  # ['a_b', 'c_d', 'e_f']
print(find_lowercase_underscore("ab_cd ef_gh"))  # ['ab_cd']

  #Regex ex4
def find_upper_followed_by_lower(string):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, string)    #находит все подстроки и возвращает ввиде списка

print(find_upper_followed_by_lower("Aa Bb Cc"))  # ['Aa', 'Bb', 'Cc']
print(find_upper_followed_by_lower("AA BB CC"))  # []

  #Regex ex5
def match_a_anything_b(string):
    pattern = r'a.*b'
    if re.fullmatch(pattern, string):
        return True
    return False

print(match_a_anything_b("a123b"))  
print(match_a_anything_b("abс"))    

  #Regex ex6
def replace_space_comma_dot(string):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', string)

print(replace_space_comma_dot("a b,c.d"))  # "a:b:c:d"

  #Regex ex7
def snake_to_camel(string):  #snake-нижние подчеркивание и маленькие буквы 
    components = string.split('_')           #components[0]: Оставляет первую часть без изменений.
    return components[0] + ''.join(x.title() for x in components[1:]) #первый символ заглавный, остальные строчные

print(snake_to_camel("this_is_snake_case"))  # "thisIsSnakeCase"

  #Regex ex8
import re

def split_at_uppercase(string):
    return re.findall('[A-Z][^A-Z]*', string)
print(split_at_uppercase("SplitThisStringAtUpperCase"))  # ['Split', 'This', 'String', 'At', 'Upper', 'Case']

  #Regex ex9
import re

def insert_space_uppercase(string):
    result = re.sub(r'([A-Z])', r' \1', string) 
    return result.strip() 

print(insert_space_uppercase("HelloWorld"))  # "Hello World"

  #Regex ex10
import re

def camel_to_snake_case(camel_case_str):
    snake_case_str = re.sub(r'([A-Z])', r'_\1', camel_case_str)
    return snake_case_str.lstrip('_')


print(camel_to_snake_case("camelCaseString"))  # "camel_Case_String"
