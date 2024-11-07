from time import time 

try:
  import naeural_client as naeural_client 
  PY_EE_INSTALLED = True
  IMPORT_ERROR = ""
except Exception as exc:
  IMPORT_ERROR = str(exc)
  PY_EE_INSTALLED = False
  
def naeural_client_version():
  version = 'not installed: ' + IMPORT_ERROR
  if PY_EE_INSTALLED:
    try:
      version = naeural_client.version
    except:
      try:
        version = naeural_client.__version__
      except:
        version = 'installed/unknown'
      #end try
    #end try
  #end if
  return version

def run_test(target_node : str, hostname=None, port=None, username=None, password=None):
  dct_result = {
    'success': False, 
    'result': f"Failed '{target_node}' after timeout", # predefined failure message
    'nodes' : [],
  }  
  start_test_time = time()
  hosts = [target_node,] # add other nodes if needed
  def on_hb(session : naeural_client.Session, e2id : str, data : dict):    
    if e2id in hosts:
      str_cpu = data['CPU']      
      str_ram = data['MACHINE_MEMORY']
      str_free = data['AVAILABLE_MEMORY']
      str_free_disk = data['AVAILABLE_DISK']
      msg = "Done: received hb from {} running on {}, RAM/Free: {:.1f} Gi / {:.1f} Gi, Free Disk: {:.1f} Gi".format(
        e2id, str_cpu, str_ram, str_free, str_free_disk,
      )      
      print(msg)
      dct_result['success'] = True
      dct_result['result'] = msg
      session.close()
    else:
      print("Rcv '{}' hb at {:.1f}s".format(e2id, time() - start_test_time))
      dct_result['nodes'] = list(set(dct_result['nodes'] + [e2id,]))
    return
  try:
    kwargs = dict(
      hostname=hostname,port=port,
      username=username, password=password,
    )
    print("Connecting to {} via {}:{}@{}:{}...".format(
        target_node, username, '*' * len(password), hostname, port,
      ), 
      flush=True,
    )
    sess = naeural_client.Session(      
      on_heartbeat=on_hb,   
      verbosity=0, 
      **kwargs
    )  
    sess.run(wait=60) # max 60 seconds wait (hb are usually at 10-15s intervals)
    #
  except Exception as exc:
    msg = str(exc)
    msg += f"{kwargs}"
    dct_result['result'] = msg
  #end try
  return dct_result