import pymysql
import pandas as pd

db = None
try:
    # DB 호스트 정보에 맞게 입력해주세요
    db = pymysql.connect(host='172.23.243.77', user='root', password='apptools', charset='utf8',db='flyai')

     # 데이터 정의 : students 리스트에 학생정보가 저장된 딕셔너리 데이터를 만듭니다.
    students = [
        {'name': 'Kei', 'age': 36, 'address' : 'PUSAN'},
        {'name': 'Tony', 'age': 34, 'address': 'PUSAN'},
        {'name': 'Jaeyoo', 'age': 39, 'address': 'GWANGJU'},
        {'name': 'Grace', 'age': 28, 'address': 'SEOUL'},
        {'name': 'Jenny', 'age': 27, 'address': 'SEOUL'},
    ]

    # 데이터 db에 추가
    for s in students:
        with db.cursor() as cursor:
            sql = '''
                    insert tb_student(name, age, address) values("%s",%d,"%s")
                    ''' % (s['name'], s['age'], s['address'])
            cursor.execute(sql)
    db.commit() # 커밋

    # 30대 학생만 조회
    cond_age = 30
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
        select * from tb_student where age > %d
        ''' % cond_age
        cursor.execute(sql) #select 명령을 위한 SQL 구문을 cursor.execute() 함수로 불러오기
        results = cursor.fetchall() #fetchall() 함수 : select 구문으로 조회한 모든 데이터 불러오는 함수
    print(results)

    # 이름 검색
    cond_name = 'Grace'
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
        select * from tb_student where name="%s"
        ''' % cond_name
        cursor.execute(sql)
        result = cursor.fetchone()
    print(result['name'], result['age'])

    # pandas 데이터프레임으로 표현
    df = pd.DataFrame(results)
    print(df)


except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()