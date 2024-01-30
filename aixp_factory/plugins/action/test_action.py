from ansible.plugins.action import ActionBase
from datetime import datetime

try:
  import py2e 
  PY_EE_INSTALLED = True
except ImportError:
  PY_EE_INSTALLED = False
  
  
def pye2_version():
  version = 'not installed'
  if PY_EE_INSTALLED:
    try:
      version = py2e.version
    except:
      try:
        version = py2e.__version__
      except:
        version = 'installed/unknown'
      #end try
    #end try
  #end if
  return version

class ActionModule(ActionBase):
  def run(self, tmp=None, task_vars=None):
    super(ActionModule, self).run(tmp, task_vars)    
    
    module_args = self._task.args.copy()
    
    aixp_vars = {k:v for k,v in task_vars.items() if k.startswith('aixp_')}    
    
    result = {
      'message'       : 'Test action message',
      'time'          : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
      'args'          : module_args,
      'aixp_vars'     : aixp_vars,
      'pye2'          : PY_EE_INSTALLED,
      'pye2_version'  : pye2_version(),
    }

    return dict(ansible_facts=result)