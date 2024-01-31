import PyE2 as pye2
import os
print(os.getcwd(), flush=True)

from aixp_factory.plugins.module_utils.aixp_utils import run_test, pye2_version
  
  
if __name__ == '__main__':
  print("Testing PyE2 version: {}".format(pye2_version()))
  TEST_WITH_ENV = False
  if TEST_WITH_ENV:
    res = run_test(target_node='stg_super')
  else:
    import configparser
    env_file = 'xperimental/client-test/.secret'
    parser = configparser.ConfigParser()
    with open(env_file) as stream:
      parser.read_string("[data]\n" + stream.read())
    dct_data = {k.upper():v for k,v in parser['data'].items()}
    res = run_test(
      target_node='stg_super',
      hostname=dct_data['AIXP_HOST'],
      port=dct_data['AIXP_PORT'],
      username=dct_data['AIXP_USER'],
      password=dct_data['AIXP_PASS']
    )

  print("Test result: {}".format(res))  