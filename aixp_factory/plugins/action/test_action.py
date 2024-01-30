from ansible.plugins.action import ActionBase
from datetime import datetime

try:
  import PyE2 as pye2 
  PY_EE_INSTALLED = True
  IMPORT_ERROR = ""
except Exception as exc:
  IMPORT_ERROR = str(exc)
  PY_EE_INSTALLED = False
  
  
def pye2_version():
  version = 'not installed: ' + IMPORT_ERROR
  if PY_EE_INSTALLED:
    try:
      version = pye2.version
    except:
      try:
        version = pye2.__version__
      except:
        version = 'installed/unknown'
      #end try
    #end try
  #end if
  return version

def run_test(target_node : str, host=None, port=None, user=None, password=None):
  dct_result = {'success': False, 'result': f"Failed '{target_node}' after timeout", 'nodes' : []}  
  hosts = [target_node,] # add other nodes if needed
  def on_hb(session : pye2.Session, e2id : str, data : dict):    
    if e2id in hosts:
      msg = "Done: received hb from {} running on {}".format(e2id, data['CPU'])
      print(msg)
      dct_result['success'] = True
      dct_result['result'] = msg
      session.close()
    else:
      print("Rcv '{}' hb".format(e2id))
      dct_result['nodes'] = list(set(dct_result['nodes'] + [e2id,]))
    return
  # run the session
  pye2.Session(
    host=host,port=port,
    user=user, password=password,
    on_heartbeat=on_hb,    
  ).run(wait=120) # max 120 seconds or before
  return dct_result


class ActionModule(ActionBase):
  def run(self, tmp=None, task_vars=None):
    super(ActionModule, self).run(tmp, task_vars)    

    AIXP_USER = 'test_user'
    AIXP_HOST = 'test_host'
    AIXP_PORT = 'test_port'
    AIXP_PWD  = 'test_pwd'
    AIXP_NODE = 'test_node'
    
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
    
    important_vars = {
      k : v for k,v in task_vars.items() 
      if k in IMPORTANT_VARIABLES
    }
    
    ansible_keys = [x for x in task_vars if x.startswith('ansible_')]
    
    aixp_user = module_args[AIXP_USER]
    aixp_host = module_args[AIXP_HOST]
    aixp_port = module_args[AIXP_PORT]
    aixp_pwd = module_args[AIXP_PWD]
    aixp_node = module_args[AIXP_NODE]
    
    hb_result = run_test(
      target_node=aixp_node,
      host=aixp_host,
      port=aixp_port,
      user=aixp_user,
      password=aixp_pwd
    )
        
    result['test_result'] = hb_result
    failed = hb_result['success'] != True
    
    result = {
      'aixp_test_time'    : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
      'aixp_test_vars'    : important_vars,
      'pye2'              : PY_EE_INSTALLED,
      'pye2_version'      : pye2_version(),
      'aixp_test_akeys'   : ansible_keys,
      'test_result'       : hb_result,
    }

    return dict(ansible_facts=result, failed=failed)