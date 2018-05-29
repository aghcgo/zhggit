#!/usr/bin/python3
# coding=utf-8
import sys
import xlrd
import numpy
#import redis
import json
import pymysql
import traceback
# r = redis.Redis(host='127.0.0.1', port=6379,db=0)
list=[]
book=xlrd.open_workbook('./hnhld_hr/201703hnhld_human.xls')

sheet=book.sheet_by_name('Sheet1')
# 打开数据库连接
db = pymysql.connect("localhost","root","zhg721019","hnhld_hr" )


# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS chnghld_hr_table")
 
# 使用预处理语句创建表
sql = """CREATE TABLE `chnghld_hr_table` (
	  `number` int(11) NOT NULL,
	  `unint_number` int(11) NOT NULL,
	  `personnel_area` varchar(128) DEFAULT NULL,
	  `secondary_institutions` varchar(64) DEFAULT NULL,
	  `tertiary_institutions` varchar(64) DEFAULT NULL,
	  `personnel_number` int(11) DEFAULT NULL,
	  `name` varchar(16) DEFAULT NULL,
	  `sex` varchar(16) DEFAULT NULL,
	  `native_place` varchar(64) DEFAULT NULL,
	  `nation` varchar(16) DEFAULT NULL,
	  `date_birth` varchar(20) DEFAULT NULL,
	  `work_time` varchar(20) DEFAULT NULL,
	  `political_status` varchar(16) DEFAULT NULL,
	  `political_status_time` varchar(20) DEFAULT NULL,
	  `incumbent_post` varchar(64) DEFAULT NULL,
	  `incumbent_post_time` varchar(20) DEFAULT NULL,
	  `position_sequence` varchar(32) DEFAULT NULL,
	  `duty_level` varchar(16) DEFAULT NULL,
	  `duty_level_time` varchar(32) DEFAULT NULL,
	  `technical_qualification` varchar(64) DEFAULT NULL,
	  `technical_qualification_time` varchar(20) DEFAULT NULL,
	  `professional_qualification` varchar(64) DEFAULT NULL,
	  `professional_qualification_time` varchar(20) DEFAULT NULL,
	  `fulltime_education` varchar(12) DEFAULT NULL,
	  `fulltime_graduate_schools` varchar(64) DEFAULT NULL,
	  `fulltime_professional` varchar(64) DEFAULT NULL,
	  `fulltime_education_time` varchar(20) DEFAULT NULL,
	  `Onthejob_education` varchar(12) DEFAULT NULL,
	  `Onthejob_graduate_schools` varchar(64) DEFAULT NULL,
	  `Onthejob_professional` varchar(64) DEFAULT NULL,
	  `Onthejob_education_time` varchar(20) DEFAULT NULL,
	  `localunint_time` varchar(20) DEFAULT NULL,
	  `chng_time` varchar(20) DEFAULT NULL,
	  `technical_skills` varchar(32) DEFAULT NULL,
	  `technical_skills_duty_level` varchar(32) DEFAULT NULL
	) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
 
cursor.execute(sql)

# 关闭数据库连接
db.close()
print("good")
