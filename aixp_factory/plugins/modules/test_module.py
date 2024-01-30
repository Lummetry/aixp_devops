from ansible.module_utils.basic import AnsibleModule

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


def run_module():  
  AIXP_USER = 'test_user'
  AIXP_HOST = 'test_host'
  AIXP_PORT = 'test_port'
  AIXP_PWD  = 'test_pwd'
  AIXP_NODE = 'test_node'
  
  failed = PY_EE_INSTALLED == False
  
  # define available arguments/parameters a user can pass to the module
  module_args = {
    AIXP_USER : dict(
      type='str', 
      required=False
    ),
    AIXP_HOST : dict(
      type='str', 
      required=False, 
    ),
    AIXP_PORT : dict(
      type='str', 
      required=False, 
    ),
    AIXP_PWD : dict(
      type='str', 
      required=False, 
    ),
  }

  # seed the result dict in the object
  # we primarily care about changed and state
  # changed is if this module effectively modified the target
  # state will include any data that you want your module to pass back
  # for consumption, for example, in a subsequent task
  result = dict(
    changed=False,
    py2e=PY_EE_INSTALLED,
    pye2_version=pye2_version()
  )

  # the AnsibleModule object will be our abstraction working with Ansible
  # this includes instantiation, a couple of common attr would be the
  # args/params passed to the execution, as well as if the module
  # supports check mode
  module = AnsibleModule(
    argument_spec=module_args,
    supports_check_mode=True
  )

  # if the user is working with this module in only check mode we do not
  # want to make any changes to the environment, just return the current
  # state with no modifications
  if module.check_mode:
    module.exit_json(**result)
    
  aixp_host = module.params.get(AIXP_HOST)
  aixp_port = module.params.get(AIXP_PORT)
  aixp_user = module.params.get(AIXP_USER)
  aixp_pwd = module.params.get(AIXP_PWD)
  aixp_node = module.params.get(AIXP_NODE)
  
  hb_result = run_test(
    target_node=aixp_node,
    host=aixp_host,
    port=aixp_port,
    user=aixp_user,
    password=aixp_pwd
  )

  # manipulate or modify the state as needed (this is going to be the
  # part where your module will do what it needs to do)
  result['test_result'] = hb_result
  failed = hb_result['success'] != True

  # use whatever logic you need to determine whether or not this module
  # made any modifications to your target
  CONDITION_CHANGED = False
  changed = CONDITION_CHANGED
  if changed:
    result['changed'] = True

  # during the execution of the module, if there is an exception or a
  # conditional state that effectively causes a failure, run
  # AnsibleModule.fail_json() to pass in the message and the result
  if failed:
    module.fail_json(msg='Test module FAILED', **result)

  # in the event of a successful module execution, you will want to
  # simple AnsibleModule.exit_json(), passing the key/value results
  module.exit_json(**result)
  
  # end of module execution
  return


def main():
  run_module()


if __name__ == '__main__':
  main() 