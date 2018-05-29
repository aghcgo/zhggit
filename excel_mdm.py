import sys
import xlrd
import numpy
import redis
import json
import pymysql
import traceback
#r = redis.Redis(host='127.0.0.1', port=6379,db=0)
list=[]
book=xlrd.open_workbook('./mdm/mdm.xls')

sheet=book.sheet_by_name('集团主数据指标列表_20171026_V10')
# 打开数据库连接
db = pymysql.connect("localhost","root","zhg721019","test" ,use_unicode=True, charset="utf8")


for i in range(sheet.nrows):
    # 使用cursor()方法获取操作游标 

    cursor = db.cursor()
    # SQL 插入语句

    sql = "INSERT INTO test.TestModel_mdm (id,name,categories,description,ca_one,ca_two,ca_three,ca_four,ca_mdm,ca_name,ca_description,ca_rule,\
				ca_formula,ca_responsible,ca_unit,ca_group,ca_version,ca_entry_name,ca_uoi) VALUES\
            ('%d','%s', '%s', '%s', '%s','%s', '%s', '%s','%s','%s','%s', '%s','%s', '%s','%s', '%s','%s', '%s','%s')" % (i+1,sheet.row_values(i)[0],\
            sheet.row_values(i)[1],sheet.row_values(i)[2],sheet.row_values(i)[3],sheet.row_values(i)[4],sheet.row_values(i)[5],\
            sheet.row_values(i)[6],sheet.row_values(i)[7],sheet.row_values(i)[8],sheet.row_values(i)[9],sheet.row_values(i)[10],\
            sheet.row_values(i)[11],sheet.row_values(i)[12],sheet.row_values(i)[13],sheet.row_values(i)[14],(sheet.row_values(i)[15]).strip(),\
            (sheet.row_values(i)[16]).strip(),sheet.row_values(i)[17]);
#    r.set(sheet.row_values(i)[7],sheet.row_values(i)[0])   #添加
#    list=list.append([sheet.row_values(i)[7],sheet.row_values(i)[0]])
#print('good')        
#print((r.get('I03589')).decode("utf8"))

    try:
   # 执行sql语句
        cursor.execute(sql)
   # 提交到数据库执行
        db.commit()
        
    except Exception as e:
       # 如果发生错误则回滚
        db.rollback()
        print(i)
#        print(sql)
        traceback.print_exc()
# 关闭数据库连接
db.close()
print("good")
