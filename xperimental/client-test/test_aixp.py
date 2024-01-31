import PyE2 as pye2
  

def run_test(target_node : str, host=None, port=None, user=None, password=None):
  dct_result = {'success': False, 'result': 'Failed after timeout', 'nodes' : []}  
  hosts = [target_node,] # add other nodes if needed
  def on_hb(session : pye2.Session, e2id : str, data : dict):    
    if e2id in hosts:
      str_cpu = data['CPU']
      str_ram = data['MACHINE_MEMORY']
      str_free = data['AVAILABLE_MEMORY']
      str_free_disk = data['AVAILABLE_DISK']
      msg = "Done: received hb from {} running on {}, RAM/Free: {:.1f}Gi/{:.1f}Gi, Free Disk: {:1f}Gi".format(
        e2id, str_cpu, str_ram, str_free, str_free_disk,
      )
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
  
  
if __name__ == '__main__':
  res = run_test(target_node='stg_super')
  
  print("Test result: {}".format(res))  