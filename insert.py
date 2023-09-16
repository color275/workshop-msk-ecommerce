import pymysql
from faker import Faker
import random
import time
from datetime import datetime
import sys

if len(sys.argv) > 1:
    batch_size = int(sys.argv[1])
else:
    batch_size = 10

db = pymysql.connect(host="localhost", user="testuser", password="testuser", database="ecommerce")
cursor = db.cursor()

fake = Faker()

def get_product_price(prd_id):
    sql = "SELECT price FROM product WHERE id = %s"
    cursor.execute(sql, (prd_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def generate_data():
    cust_id = random.randint(1, 100)
    prd_id = random.randint(1, 20)
    
    order_cnt = random.randint(1, 10)

    product_price = get_product_price(prd_id)
    
    if product_price is not None:
        order_price = order_cnt * product_price
    else:
        order_price = random.randint(10, 100) * 100  # 상품 가격이 없는 경우 임의의 가격 생성
    
    order_dt = fake.date_time_this_decade()
    last_update_time = datetime.now()
    promo_id = fake.word()
    
    return (cust_id, prd_id, order_cnt, order_price, order_dt, last_update_time, promo_id)


while True:
    data_to_insert = [generate_data() for _ in range(batch_size)]
    
    sql = """INSERT INTO orders (cust_id, prd_id, order_cnt, order_price, order_dt, last_update_time, promo_id)
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    
    cursor.executemany(sql, data_to_insert)
    db.commit()
    print("# insert {}row...".format(batch_size))
    
    time.sleep(1)

db.close()
