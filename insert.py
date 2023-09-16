import pymysql
from faker import Faker
import random
import time
from datetime import datetime

db = pymysql.connect(host="localhost", user="testuser", password="testuser", database="ecommerce")
cursor = db.cursor()

fake = Faker()

def generate_data():
    cust_id = random.randint(1, 100)
    prd_id = random.randint(1, 20)
    
    order_cnt = random.randint(1, 10)
    order_price = random.randint(10, 100) * 100
    order_dt = fake.date_time_this_decade()
    last_update_time = datetime.now()
    promo_id = fake.word()
    
    return (cust_id, prd_id, order_cnt, order_price, order_dt, last_update_time, promo_id)

batch_size = 10
while True:
    data_to_insert = [generate_data() for _ in range(batch_size)]
    
    sql = """INSERT INTO orders (cust_id, prd_id, order_cnt, order_price, order_dt, last_update_time, promo_id)
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    
    cursor.executemany(sql, data_to_insert)
    db.commit()
    print("# insert {}row...".format(batch_size))
    
    time.sleep(1)

db.close()
