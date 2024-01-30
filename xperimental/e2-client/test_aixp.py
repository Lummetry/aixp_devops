import PyE2 as pye2
  

def run_test(target_node : str, host=None, port=None, user=None, password=None):
  dct_result = {'success': False, 'result': 'Failed after timeout', 'nodes' : []}  
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
  
  
if __name__ == '__main__':
  res = run_test(target_node='aid_mob')
  
  print("Test result: {}".format(res))  