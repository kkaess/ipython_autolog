# Configuration file for ipython.

from datetime import datetime

str_now = datetime.now().strftime("%b%d_%Y_%H_%M_%S")
filename = 'ipy_'+str_now+'.py'

c = get_config()

c.InteractiveShell.logfile = 'ipy_'+str_now+'.py'
c.InteractiveShell.logstart = True
