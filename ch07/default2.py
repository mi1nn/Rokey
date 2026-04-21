# default2.py

def connect_db(host = "localhost", port = 3306, timeout = 3):
    print(host, port, timeout)
    
connect_db()  # 기본 연결 수행
connect_db(timeout = 10)

# 아이디어 구상
# 문서화    
# 데이터베이스(db) : 데이터 집합

# DB에 접근하고 싶다. 
# DB는 같은 네트워크에 내 컴퓨터로 제어