from ansible.module_utils.basic import AnsibleModule

from ansible_collections.aidamian.aixp_factory.plugins.module_utils.aixp_utils import run_test, pye2_version


def run_module():  
  AIXP_USER = 'test_user'
  AIXP_HOST = 'test_host'
  AIXP_PORT = 'test_port'
  AIXP_PWD  = 'test_pwd'
  AIXP_NODE = 'test_node'
  
  str_pye2_ver = pye2_version()
  
  pye2_installed = str_pye2_ver is not None and 'not installed' not in str_pye2_ver.lower()
  failed = not pye2_installed
  
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
      type='int', 
      required=False, 
    ),
    AIXP_PWD : dict(
      type='str', 
      required=False, 
    ),
    AIXP_NODE : dict(
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
    py2e=pye2_installed,
    pye2_version=str_pye2_ver,
    test_result={},
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
    
  
  if pye2_installed:    
    aixp_host = module.params.get(AIXP_HOST)
    aixp_port = module.params.get(AIXP_PORT)
    aixp_user = module.params.get(AIXP_USER)
    aixp_pwd = module.params.get(AIXP_PWD)
    aixp_node = module.params.get(AIXP_NODE)

    hb_result = run_test(
      target_node=aixp_node,
      hostname=aixp_host,
      port=aixp_port,
      username=aixp_user,
      password=aixp_pwd
    )
    result['test_result'] = hb_result
    failed = hb_result['success'] != True
  #end if pye2_installed
  
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