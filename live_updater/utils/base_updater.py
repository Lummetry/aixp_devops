from PyE2 import Instance, Pipeline, Session
from threading import Thread

class LiveUpdater:
  def __init__(self):
    """ Connect to the network and get all active nodes using pye2"""
    self.nodes = [      
    ]      
                  
    self.session = None    
    self.__init_and_get_nodes()
    return
  
  
  def P(self, msg, color='w'):
    """ This method prints the message with color"""
    self.session.P(msg, color)
    return
    
  def __init_and_get_nodes(self):
    """ This method gets all active nodes in 15-20 sec"""
    session = Session(root_topic="lummetry")

    session.run(wait=15, close_session=False)

    active_nodes = list(map(session.get_node_name, session.get_active_nodes()))
    active_nodes.sort()

    session.P(f"Found {len(active_nodes)} active nodes.\n" + '\n'.join(active_nodes), color='g')
    self.session = session
    self.nodes = active_nodes
    return


  def run_update(self):
    """ This method runs the update on all the nodes"""
    for node in self.nodes:
      # now start a thread for each node using node_update method with node as argument
      addr = node['addr']
      name = node['name']
      thr = Thread(target=self.node_update, args=(node,))
      node['thread'] = thr
      self.P("Starting thread for node: " + name, color='blue')
      thr.start()
    
    for node in self.nodes:
      thr = node['thread']
      thr.join()
      self.P("Thread for node: " + node['name'] + " is finished", color='blue')
    return
  
  
  def node_update(self, node):
    """ This method updates the given node and should be defined in inherited class"""    
    return