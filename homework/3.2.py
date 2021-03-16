def print_data(**kwags):
    return ' '.join(kwags.values())
print(print_data(name=input('Name: '), surname=input('Surname: '), year=input('Year: '), city=input('City: '), email=input('E-mail'), phone=input('Pnone: ')))
def print_data(name, surname, year, city, email, phone):
    return f'Name - {name}, surname - {surname}, year - {year}, city - {city}, email - {email}, phone - {phone}'
print(print_data(name='Данил', surname='Кузнецов', year='1999', city='Москва', email='homework@gmail.com', phone='8-111-000-11-00'))