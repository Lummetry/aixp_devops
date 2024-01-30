from ansible.module_utils.basic import AnsibleModule

try:
  import PyE2 as py2e 
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

def run_module():
  PARAM_APP_FOLDER = 'app_base_folder'
  PARAM_CACHE_FOLDER = 'app_cache_folder'
  
  
  # define available arguments/parameters a user can pass to the module
  module_args = {
    PARAM_APP_FOLDER : dict(
      type='str', 
      required=False
    ),
    PARAM_CACHE_FOLDER : dict(
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
    params='',
    message='',
    py2e=PY_EE_INSTALLED,
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
    
  app_folder = module.params.get(PARAM_APP_FOLDER)
  app_cache_folder = module.params.get(PARAM_CACHE_FOLDER)

  # manipulate or modify the state as needed (this is going to be the
  # part where your module will do what it needs to do)
  result['params'] = module.params
  result['pye2_version'] = pye2_version()

  # use whatever logic you need to determine whether or not this module
  # made any modifications to your target
  CONDITION_CHANGED = False
  changed = CONDITION_CHANGED
  if changed:
    result['changed'] = True

  # during the execution of the module, if there is an exception or a
  # conditional state that effectively causes a failure, run
  # AnsibleModule.fail_json() to pass in the message and the result
  CONDITION_FAILED = False
  failed = CONDITION_FAILED
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