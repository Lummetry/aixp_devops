from ansible.plugins.action import ActionBase
from datetime import datetime


class ActionModule(ActionBase):
  def run(self, tmp=None, task_vars=None):
    super(ActionModule, self).run(tmp, task_vars)
    
    module_args = self._task.args.copy()
    
    result = {
    'message' : 'Test action message',
    'time' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'args' : module_args,
    'all_vars' : task_vars,
    }

    return dict(ansible_facts=result)