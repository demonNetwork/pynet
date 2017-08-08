#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------|
#autor: Antonio J.|
#-----------------|

import random
import feedparser
import time
from datetime import datetime, date, timedelta
import calendar
import commands
import sys
from daemon import runner

class App():
   def __init__(self):
      self.stdin_path      = '/dev/null'
      self.stdout_path     = '/dev/tty'
      self.stderr_path     = '/dev/tty'
      self.pidfile_path    =  '/var/run/demonPynet.pid'
      self.pidfile_timeout = 86400

   def run(self):

      while True:
          print("working")
          time.sleep(5)

if __name__ == '__main__':
   app=App()
   serv = runner.DaemonRunner(app)
   serv.do_action()
