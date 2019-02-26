import os, sys, time, thread, ast, subprocess, threading


def monkey(choice, seed, throttle, events):

	if (choice == 0):
		for p in pkgList:
		#Running monkey package by package
			process = subprocess.Popen('adb logcat -c')
			process = subprocess.Popen('adb shell monkey -p ' + str(p) + ' -s ' + str(seed) + ' --throttle ' + str(throttle) + ' -v ' + str(events) + '"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			if not os.path.exists('MonkeyLogs'):
				os.makedirs('MonkeyLogs')
			m_log = open('MonkeyLogs\\Monkey_Log_' + str(p) + time.ctime().replace(' ', '_').replace(':', '-') + '.txt', 'w')
			print '\n Executing Monkey Test in %s \n' % (str(p))
		#print '\n\n Executing Monkey Test in %s with Seed %s Throttle %s Events %s \n\n' % (str(p), seed, throttle, events)
			while True:
				logline = process.stdout.readline()
				if logline == '' and process.poll() != None:
					break
				m_log.write(logline + '\n')
				if 'Monkey finished' in logline:
					print '\n Monkey Executed successfully'
				if 'System appears to have crashed' in logline:
					print 'Crashed occurred at ' + logline.split('at')[1]
					if not os.path.exists('Logs'):
						os.makedirs('Logs')
					process = subprocess.Popen('adb bugreport > E:\\Automation-Trial\\MonkeyTest\\Logs\\' + str(p) + time.ctime().replace(' ', '_').replace(':', '-') + '.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
					print 'Capturing logs....Please wait'
					time.sleep(120)			
				if 'anr' in logline.lower():
					print 'Anr occurred \n' + logline
					process = subprocess.Popen('adb bugreport > E:\\Automation-Trial\\MonkeyTest\\Logs\\' + str(p) + time.ctime().replace(' ', '_').replace(':', '-') + '.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
					print 'Capturing logs....Please wait'
					time.sleep(120)
		m_log.close()

#Running monkey on selected package
	else:	
		cho = pkgList[choice]
		process = subprocess.Popen('adb shell monkey -p ' + str(cho) + ' -s ' + str(seed) + ' --throttle ' + str(throttle) + ' -v ' + str(events) + '"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		if not os.path.exists('MonkeyLogs'):
			os.makedirs('MonkeyLogs')
		m_log = open('MonkeyLogs\\Monkey_Log_' + str(cho) + time.ctime().replace(' ', '_').replace(':', '-') + '.txt', 'w')
		print '\n Executing Monkey Test in %s \n' % (str(cho))
		#print '\n\n Executing Monkey Test in %s with Seed %s Throttle %s Events %s \n\n' % (str(p), seed, throttle, events)
		while True:
			logline = process.stdout.readline()
			if logline == '' and process.poll() != None:
				break
			m_log.write(logline + '\n')
			if 'Monkey finished' in logline:
				print '\n Monkey Executed successfully'
			if 'System appears to have crashed' in logline:
				print 'Crashed occurred at ' + logline.split('at')[1]
				if not os.path.exists('Logs'):
					os.makedirs('Logs')
				process = subprocess.Popen('adb bugreport > E:\\Automation-Trial\\MonkeyTest\\Logs\\' + str(cho) + time.ctime().replace(' ', '_').replace(':', '-') + '.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				print 'Capturing logs....Please wait'
				time.sleep(120)			
			if 'anr' in logline.lower():
				print 'Anr occurred \n' + logline
				process = subprocess.Popen('adb bugreport > E:\\Automation-Trial\\MonkeyTest\\Logs\\' + str(cho) + time.ctime().replace(' ', '_').replace(':', '-') + '.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
				print 'Capturing logs....Please wait'
				time.sleep(120)
		m_log.close()
	
	
	

def execute(command):
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)	
try:
	execute("adb devices")
	#execute("adb install -r GetAllApps.apk")
	#execute("adb shell am start -n com.rajesh.applist/.MainActivity")
except Exception as e:
    print e
    print 'APK NOT FOUND'
time.sleep(1)

#try:
	#execute("adb pull /sdcard/apps.txt")
#except Exception as e:
    #print e
    #print 'APPS LIST FILE NOT FOUND'

time.sleep(1)

#Reading apps name and package from file

f=open("apps.txt","r")
packageline=f.readlines()
f.close

#storing & printing app name and package in different list

pkgList=['All']
appName=['All']
for i in packageline:
	if '>>>' in i:
		pkgList.append(i.strip().split('>>>')[1])
		appName.append(i.strip().split('>>>')[0])
for i in range(0, len(appName)):
	print "%s\t%s" % (i,appName[i])

#taking input from user

print '\n'
choice = input('Choose your Application name and enter number   \n')
print 'You have selected %s \n' % appName[choice]
#confirm = input('Do you want to continue (Y/N)  ')
monkey(choice, seed=690, throttle=585, events=20)
