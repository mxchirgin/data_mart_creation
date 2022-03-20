import pandas as pd
import sqlalchemy as sa
engine=sa.create_engine('postgresql+psycopg2://postgres:admin@localhost/postgres')
conn=engine.connect()

f=pd.read_sql(con=conn, sql='select * from chirgin.result', index_col=None)

f.to_excel('chirgin_result.xlsx',engine='openpyxl',index=None)