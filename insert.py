import pymysql
from faker import Faker
import random
import time

db = pymysql.connect(host="localhost", user="testuser", password="testuser", database="ecommerce")
cursor = db.cursor()

fake = Faker()

def generate_data():
    cust_id = random.randint(1, 100)
    prd_id = random.randint(1, 20)
    
    order_cnt = random.randint(1, 10)
    order_price = random.randint(10, 100)
    order_dt = fake.date_time_this_decade()
    last_update_time = fake.date_time_between(start_date=order_dt)
    promo_id = fake.word()
    
    return (cust_id, prd_id, order_cnt, order_price, order_dt, last_update_time, promo_id)

batch_size = 100
while True:
    data_to_insert = [generate_data() for _ in range(batch_size)]
    
    sql = """INSERT INTO orders (cust_id, prd_id, order_cnt, order_price, order_dt, last_update_time, promo_id)
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    
    cursor.executemany(sql, data_to_insert)
    db.commit()
    
    time.sleep(1)

db.close()
