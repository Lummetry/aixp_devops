from PyE2 import Instance, Pipeline, Session, Payload
from typing import Dict, List
import json
from PyE2.default.instance import ViewScene01

NODES = [
  "gts-ws",
  "gts-staging"
]


if __name__ == "__main__":
  session = Session(root_topic="lummetry")

  dct_nodes_pipelines_resolution = {}

  for node in NODES:
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

      pipeline: Pipeline = session.attach_to_pipeline(node=node, name=pipeline_name)

      instances: List[Instance] = pipeline.lst_plugin_instances

      for instance in instances:
        if instance.signature == ViewScene01.signature:

          payload: Payload = instance.send_instance_command_and_wait_for_response_payload(
            command="GET_LAST_WITNESS",
            response_params_key="COMMAND_PARAMS",
            timeout_response_payload=5,
          )

          if payload is not None:
            image_h, image_w = payload["IMG_SIZE"]

            if node not in dct_nodes_pipelines_resolution:
              dct_nodes_pipelines_resolution[node] = {}
            # endif node not in dct_nodes_pipelines_resolution

            if pipeline_name not in dct_nodes_pipelines_resolution[node]:
              dct_nodes_pipelines_resolution[node][pipeline_name] = {
                'IMAGE_H': image_h,
                'IMAGE_W': image_w,
              }
            # endif pipeline_name not in dct_nodes_pipelines_resolution[node]
          else:
            session.P(
              f"Failed to get image size from instance {instance.signature} on pipeline {pipeline_name} on node {node}.", color='r')
            dct_nodes_pipelines_resolution[node][pipeline_name] = {
              'IMAGE_H': None,
              'IMAGE_W': None,
            }
          # endif payload is not None

          break
        # endif instance.signature == ViewScene01.signature
      # endfor instances
    # endfor pipelines.items()
  # endfor NODES

  session.run(wait=5)

  print(dct_nodes_pipelines_resolution)
  with open("nodes_pipelines_resolution.json", "w") as f:
    json.dump(dct_nodes_pipelines_resolution, f, indent=2)
