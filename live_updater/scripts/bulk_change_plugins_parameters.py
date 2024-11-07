from typing import List

from naeural_client import Instance, Pipeline, Session

TARGET_PARAMETERS = {
  "CAMERA_TAMPERING_BASIC_01": {
    "ANCHOR_MAX_SUM_PERSON_AREA": 0,
    "ANALYSIS_IGNORE_MIN_PERSON_AREA": 0,
    "ALERT_RAISE_VALUE": 80,
    "ALERT_RAISE_CONFIRMATION_TIME": 50,
  },
  "CAMERA_TAMPERING_ANGLE_01": {
    "ANCHOR_MAX_SUM_PERSON_AREA": 0,
    "ANALYSIS_IGNORE_MIN_PERSON_AREA": 0,
    "ALERT_RAISE_CONFIRMATION_TIME": 50,
  },
  "CAMERA_TAMPERING_IQA_FAST_01": {
    "ANCHOR_MAX_SUM_PERSON_AREA": 0,
    "ANALYSIS_IGNORE_MIN_PERSON_AREA": 0,
    "ALERT_RAISE_CONFIRMATION_TIME": 50,
  },
}

if __name__ == "__main__":
  session = Session(root_topic="lummetry")

  session.run(wait=15, close_session=False) # session.sleep as session.run may appear to execute a graph of transactions

  active_nodes = list(map(session.get_node_name, session.get_active_nodes()))
  active_nodes.sort()

  session.P(f"Found {len(active_nodes)} active nodes.\n" + '\n'.join(active_nodes), color='g')

  all_transactions = []

  for node in active_nodes:
    if not session.wait_for_node(node):
      session.P(f"Node {node} is not online. Skipping.", color='r')
      continue

    pipelines = session.get_active_pipelines(node)

    if not pipelines:
      session.P(f"No pipelines are known for node {node}. It seems the node was never seen online.", color='r')
      continue

    for pipeline_name, pipeline in pipelines.items():
      if pipeline_name == "admin_pipeline":
        # skip admin pipeline
        continue

      pipeline: Pipeline
      p_type = pipeline.config.get("TYPE", None)

      if p_type is None:
        session.P(f"Pipeline {pipeline_name} on node {node} has no TYPE configured.", color='r')
        continue

      if p_type.lower() != "videostream":
        # skip non-video stream pipelines
        continue

      instances: List[Instance] = pipeline.lst_plugin_instances

      for instance in instances:
        is_configured_ok = True
        for signature, parameters in TARGET_PARAMETERS.items():
          if instance.signature == signature:
            instance.update_instance_config(parameters)
            is_configured_ok = not instance._is_tainted()

            instance_identifier = f"{node}:{pipeline_name}:{instance.signature}:{instance.instance_id}"
            configured_msg = f"is configured OK" if is_configured_ok else "is not configured OK. Reconfiguring..."
            session.P(f"Instance <{instance_identifier}> {configured_msg}", color='g' if is_configured_ok else 'r')
            break
        # endfor TARGET_PARAMETERS.items()

      # endfor instances

      transactions = pipeline.deploy(timeout=10, wait_confirmation=False)
      if transactions is not None:
        all_transactions.append(transactions)
    # endfor pipelines.items()
  # endfor NODES

  session.wait_for_all_sets_of_transactions(all_transactions)

  session.run(wait=5)
