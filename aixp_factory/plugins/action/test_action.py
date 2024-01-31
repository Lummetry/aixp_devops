from ansible.plugins.action import ActionBase
from datetime import datetime


from ansible_collections.aidamian.aixp_factory.plugins.module_utils.aixp_utils import run_test, pye2_version



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
    
    str_pye2_ver = pye2_version()    
    pye2_installed = str_pye2_ver is not None and 'not installed' not in str_pye2_ver.lower()
    failed = not pye2_installed    
    
    hb_result = {}
    if pye2_installed:
      hb_result = run_test(
        target_node=aixp_node,
        host=aixp_host,
        port=aixp_port,
        user=aixp_user,
        password=aixp_pwd
      )          
      failed = hb_result['success'] != True
    #end if  
    
    result = {
      'aixp_test_time'    : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
      'aixp_test_vars'    : important_vars,
      'pye2'              : pye2_installed,
      'pye2_version'      : str_pye2_ver,
      'aixp_test_akeys'   : ansible_keys,
      'test_result'       : hb_result,
    }

    return dict(ansible_facts=result, failed=failed)