import pymysql
from faker import Faker
import random
import time

# MySQL 데이터베이스 연결 설정
db = pymysql.connect(host="localhost", user="testuser", password="testuser", database="ecommerce")
cursor = db.cursor()

# 랜덤 데이터를 생성하기 위한 Faker 객체 생성
fake = Faker()

# 데이터를 생성하고 데이터베이스에 삽입하는 함수
def generate_data():
    # 랜덤한 cust_id와 prd_id 생성
    cust_id = random.randint(1, 100)
    prd_id = random.randint(1, 20)
    
    # 랜덤한 주문 데이터 생성
    order_cnt = random.randint(1, 10)
    order_price = random.randint(10, 100)
    order_dt = fake.date_time_this_decade()
    last_update_time = fake.date_time_between(start_date=order_dt)
    promo_id = fake.word()
    
    return (cust_id, prd_id, order_cnt, order_price, order_dt, last_update_time, promo_id)

# 데이터 생성 주기 (1초당 100건)
batch_size = 100
while True:
    data_to_insert = [generate_data() for _ in range(batch_size)]
    
    # SQL 쿼리 작성
    sql = """INSERT INTO orders (cust_id, prd_id, order_cnt, order_price, order_dt, last_update_time, promo_id)
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    
    # 데이터 삽입
    cursor.executemany(sql, data_to_insert)
    db.commit()
    
    time.sleep(1)  # 1초 대기

# 데이터베이스 연결 종료
db.close()
