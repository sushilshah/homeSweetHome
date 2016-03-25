#!/usr/bin/env python
# Author: Sushil Shah


import os
import ConfigParser
from atl_pahomqtt import CarriotsMqttClient
import logging
import serial, time, json, datetime
import atl_utils
from sfdc_utils import SFDCUtils
import RPi.GPIO as GPIO
import thread, time, threading, collections


def main():
	
	default_cfg = {
		'url'        : 'localhost:1880',
		'baudRate'    : '115200',
		'connectPort'  : '/dev/ttyACM0',
		'device_id'  : '56789'
		}

	cp = ConfigParser.SafeConfigParser(default_cfg)
	cp.read(os.path.splitext(__file__)[0] + '.ini')
	log_file = cp.get('PARAMETERS','log_file')

	logging.basicConfig(filename=log_file,filemode='w', level=logging.DEBUG)

	logging.info('Starting Supply Chain program')
	logging.info('Config read from: ' + os.path.splitext(__file__)[0] + '.ini')

	logging.info('\n==========Started with below configurations========================')
	logging.info('url       : ' + cp.get('PARAMETERS','url'))
	logging.info('baudRate : ' + str(cp.getint('DEVICE_PARAMS','baudRate')))
	logging.info('connectPort  : ' + cp.get('DEVICE_PARAMS','connectPort'))
	logging.info('device_id  : ' + cp.get('DEVICE_PARAMS','device_id'))
	logging.info('post interval : ' +str(cp.getint('PARAMETERS','post_interval')))
	logging.info('\n==================================')
	
	

	'''Button setup '''
	GPIO.setmode(GPIO.BOARD)
	#12 is button ping 
	GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	#13 is pin for led light
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13,GPIO.LOW)
	button_press_flag = False
 		
		if button_press_flag:
			GPIO.output(13,GPIO.HIGH)
		else:
			GPIO.output(13,GPIO.LOW)


main()
