from live_updater.utils.base_updater import LiveUpdater


class MyUpdater(LiveUpdater):
  def __init__(self):
    super().__init__()
    return
  
  def node_update(self, node):
    """ This method processes all the required updates for the given node (inherited/overwritten method)"""
    self.P("Updating node: " + node['name'], color='yellow')
    return
  
  
  
if __name__ == "__main__":   
  updater = MyUpdater()
  updater.P("Starting the update process", color='blue')
  updater.run_update(nodes=None) # all nodes will be updated
  
