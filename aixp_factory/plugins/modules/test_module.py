from ansible.module_utils.basic import AnsibleModule


def run_module():
  PARAM1 = 'param1'
  PARAM2 = 'param2'
  # define available arguments/parameters a user can pass to the module
  module_args = {
    PARAM1 : dict(type='str', required=False),
    PARAM2 : dict(type='bool', required=False, default=False)
  }

  # seed the result dict in the object
  # we primarily care about changed and state
  # changed is if this module effectively modified the target
  # state will include any data that you want your module to pass back
  # for consumption, for example, in a subsequent task
  result = dict(
    changed=False,
    original_input='',
    message=''
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
    
  param1 = module.params.get(PARAM1)
  param2 = module.params.get(PARAM2)

  # manipulate or modify the state as needed (this is going to be the
  # part where your module will do what it needs to do)
  result['original_input'] = {
    PARAM1 : param1,
    PARAM2 : param2
  }
  result['message'] = 'processed'

  # use whatever logic you need to determine whether or not this module
  # made any modifications to your target
  if module.params['new']:
    result['changed'] = True

  # during the execution of the module, if there is an exception or a
  # conditional state that effectively causes a failure, run
  # AnsibleModule.fail_json() to pass in the message and the result
  if param1== 'fail me':
    module.fail_json(msg='You requested this to fail', **result)

  # in the event of a successful module execution, you will want to
  # simple AnsibleModule.exit_json(), passing the key/value results
  module.exit_json(**result)
  
  # end of module execution
  return


def main():
  run_module()


if __name__ == '__main__':
  main()  /home/andrei/work/aixp_devops/xperimental/ansible_test1/logs