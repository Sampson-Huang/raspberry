# -*- coding: utf-8 -*- 
#----树莓派呼吸灯程序----
#LED阳极接12脚，阴极接6脚
#---空丶忆---2018.9.4---

import RPi.GPIO as GPIO      #导入RPi.GPIO模块

GPIO.setmode(GPIO.BOARD)     #针脚编号采用BOARD编号系统，也可使用GPIO.BCM,注意二者编号不同
GPIO.setup(12,GPIO.OUT)      #配置12脚为输出通道

p = GPIO.PWM(12,144)         #创建一个PWM实例
p.start(1)					 #启用PWM

times=3						 #循环次数判断参数

while times :						#呼吸灯循环整体
	for x in range(101):			#for循环
		p.ChangeDutyCycle(x)		#更改PWM信号占空比，0<=x<=100
		for y in range(51):			#以下至pass为延时部分
			for z in range(1001):
				pass
	times = times-1
	for m in range(101):			#上面修改占空比使灯逐渐变亮，此处使灯变暗
		p.ChangeDutyCycle(100-m)
		for n in range(51):
			for l in range(1001):
				pass

p.stop()                     #停止PWM
GPIO.cleanup()				 #程序结束后进行清理

