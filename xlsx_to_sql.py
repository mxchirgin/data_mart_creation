import pandas as pd
import sqlalchemy as sa
sales=pd.read_excel('C:\\Users\maxch\AppData\Local\Programs\Python\Python38\dbtest\sql-assignment\Исходные данные.xlsx',
                sheet_name='Продажи',engine='openpyxl',index_col=0)

items = pd.read_excel('C:\\Users\maxch\AppData\Local\Programs\Python\Python38\dbtest\sql-assignment\Исходные данные.xlsx',
                sheet_name='Товары',engine='openpyxl',index_col=0)

services = pd.read_excel('C:\\Users\maxch\AppData\Local\Programs\Python\Python38\dbtest\sql-assignment\Исходные данные.xlsx',
                sheet_name='Услуги',engine='openpyxl',index_col=0)

salesman = pd.read_excel('C:\\Users\maxch\AppData\Local\Programs\Python\Python38\dbtest\sql-assignment\Исходные данные.xlsx',
                sheet_name='Продавцы',engine='openpyxl',index_col=0)

department = pd.read_excel('C:\\Users\maxch\AppData\Local\Programs\Python\Python38\dbtest\sql-assignment\Исходные данные.xlsx',
                sheet_name='Отделы',engine='openpyxl',index_col=0)

engine=sa.create_engine('postgresql+psycopg2://postgres:admin@localhost/postgres')
conn=engine.connect()
sales.to_sql(name='sales',con=conn,schema='chirgin',if_exists='append')
items.to_sql(name='items',con=conn,schema='chirgin',if_exists='append')
services.to_sql(name='services',con=conn,schema='chirgin',if_exists='append')
salesman.to_sql(name='salesman',con=conn,schema='chirgin',if_exists='append')
department.to_sql(name='department',con=conn,schema='chirgin',if_exists='append')

