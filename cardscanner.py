#!/usr/bin/env python
import time, serial, argparse, logging, threading, Queue, sys, traceback
from RFUID import rfid
import subprocess

class cardReader(object):
	def __init__(self):
		self.readerok = True
		try:
			# TODO: keep this reader for checkForCard
			with rfid.Pcsc.reader() as reader:
				logging.info('PCSC firmware: %s', reader.pn532.firmware())
		except (serial.SerialException, serial.SerialTimeoutException), e:
			logging.warn('Serial error during initialisation: %s', e)
			self.readerok = False
		except Exception, e:
			logging.critical('Unexpected error during initialisation: %s', e)
			self.readerok = False
		self.current = None
		
	def run(self):
		while True:
			if self.readerok:
				try:
					with rfid.Pcsc.reader() as reader:
						for tag in reader.pn532.scan():
							uid = tag.uid.upper()
				except rfid.NoCardException:
					self.current = None
					uid = None
			else:
				uid = None

			if self.current and self.current == uid:
				pass
			elif uid:
				self.current = uid
				logging.info("Got card with uid %s", uid)
				subprocess.call(["/bin/bash", "/home/russ/cardscanner/input_card.sh", uid])

cardReader().run()
