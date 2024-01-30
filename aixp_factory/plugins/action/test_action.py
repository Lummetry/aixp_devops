from ansible.plugins.action import ActionBase
from datetime import datetime

IMPORT_ERROR = ""
try:
  import PyE2 as py2e 
  PY_EE_INSTALLED = True
except Exception as exc:
  IMPORT_ERROR = str(exc)
  PY_EE_INSTALLED = False
  
  
def pye2_version():
  version = 'not installed/' + IMPORT_ERROR
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
    
    IMPORTANT_VARIABLES = [
      'inventory_hostname',
      'ansible_architecture',
      'ansible_board_serial',
      'ansible_board_asset_tag',
      'ansible_distribution',
      'ansible_distribution_release',
      'ansible_distribution_version',
      'ansible_host',
      'ansible_fqdn',
      'ansible_hostname',
    ]
    
    aixp_vars = {
      k : v for k,v in task_vars.items() 
      if k.startswith('aixp_') and not isinstance(v, dict)
    }
    aixp_vars.update({
      k : v for k,v in task_vars.items() 
      if k in IMPORTANT_VARIABLES
    })
    
    ansible_keys = [x for x in module_args if x.startswith('ansible_')]
    

    
    result = {
      'message'       : 'Test action message',
      'time'          : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
      'args'          : module_args,
      'aixp_vars'     : aixp_vars,
      'pye2'          : PY_EE_INSTALLED,
      'pye2_version'  : pye2_version(),
      'ansible_keys'  : ansible_keys,
    }

    return dict(ansible_facts=result)