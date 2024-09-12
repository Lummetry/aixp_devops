from copy import deepcopy
from typing import Dict, List

from PyE2 import Instance, Pipeline, Session

ASSUMED_DEFAULT_RESOLUTION = (1080, 1920)

# TARGET_RESOLUTION = (480, 640)
# TARGET_RESOLUTION = (720, 1280)
TARGET_RESOLUTION = (1080, 1920)
TARGET_NODES = [
    "gts-ws",
  ]


def convert_points_to_a_different_resolution(points: List, old_resolution: List, new_resolution: List) -> List:
  # resolution is in H, W
  if old_resolution == new_resolution:
    return points

  points = deepcopy(points)

  print(f"Converting points {points} from {old_resolution} to {new_resolution}")

  if len(points) == 4 and isinstance(points[0], int):
    # T, L, B, R
    points[0] = int(points[0] * new_resolution[0] / old_resolution[0])
    points[1] = int(points[1] * new_resolution[1] / old_resolution[1])
    points[2] = int(points[2] * new_resolution[0] / old_resolution[0])
    points[3] = int(points[3] * new_resolution[1] / old_resolution[1])
  elif isinstance(points[0], list):
    # list of points
    for i, point in enumerate(points):
      # points are W, H
      points[i][0] = int(point[0] * new_resolution[1] / old_resolution[1])
      points[i][1] = int(point[1] * new_resolution[0] / old_resolution[0])
  elif len(points) == 2 and isinstance(points[0], int):
    points = None
  else:
    points = None
  # end if rescale points

  print(f"Converted points {points}")

  return points


def convert_field_to_a_different_resolution(session, instance, instance_identifier, field, old_resolution, new_resolution):
  value = instance.config.get(field, None)
  if value is None:
    return

  value = convert_points_to_a_different_resolution(value, old_resolution, new_resolution)
  if value is None:
    instance_identifier = f"{node}/{pipeline_name}/{instance.signature}/{instance.instance_id}"
    session.P(f"Unknown points format encountered on {instance_identifier}: {field}={value}", color='r')
  else:
    instance.update_instance_config({
      field: value,
      "ASSUMED_STREAM_RESOLUTION": new_resolution,
      "PREVIOUS_STREAM_RESOLUTION": old_resolution,
    })

  return


if __name__ == "__main__":
  session: Session = Session(root_topic="lummetry")

  for node in TARGET_NODES:
    if not session.wait_for_node(node):
      session.P(f"Node {node} did not send any heartbeat.", color='r')
      continue

    pipelines: Dict[str, Pipeline] = session.get_active_pipelines(node)
    if not pipelines:
      session.P(f"No pipelines are known for node {node}. It seems the node was never seen online.", color='r')
      continue

    for pipeline_name, pipeline in pipelines.items():
      if pipeline_name == "admin_pipeline":
        # skip admin pipeline
        continue

      pipeline: Pipeline

      configured_h: int = pipeline.config.get("DEFAULT_H", pipeline.config.get("FRAME_H", ASSUMED_DEFAULT_RESOLUTION[0]))
      configured_w: int = pipeline.config.get("DEFAULT_W", pipeline.config.get("FRAME_W", ASSUMED_DEFAULT_RESOLUTION[1]))

      if configured_h <= TARGET_RESOLUTION[0] and configured_w <= TARGET_RESOLUTION[1]:
        # we upscale, so we need to first update the pipeline and then the instances
        pipeline.update_acquisition_parameters(config={
          "DEFAULT_H": TARGET_RESOLUTION[0],
          "DEFAULT_W": TARGET_RESOLUTION[1],
          "FRAME_H": TARGET_RESOLUTION[0],
          "FRAME_W": TARGET_RESOLUTION[1],

          "PREVIOUS_H": configured_h,
          "PREVIOUS_W": configured_w,
        })

        pipeline.deploy(timeout=10)

      instances: List[Instance] = pipeline.lst_plugin_instances

      for instance in instances:
        assumed_stream_resolution = instance.config.get("ASSUMED_STREAM_RESOLUTION", (configured_h, configured_w))
        if assumed_stream_resolution == TARGET_RESOLUTION:
          # no need to rescale points
          continue

        instance_identifier = f"{node}/{pipeline_name}/{instance.signature}/{instance.instance_id}"
        for points_field in ["POINTS", "CRITICAL_ZONE", "NON_CRITICAL_ZONE", "SLICING_LINE"]:
          convert_field_to_a_different_resolution(
            session=session,
            instance=instance,
            instance_identifier=instance_identifier,
            field=points_field,
            old_resolution=assumed_stream_resolution,
            new_resolution=TARGET_RESOLUTION,
          )
        # end for convert each field
      # end for update each instance

      pipeline.deploy(timeout=10)

      if configured_h >= TARGET_RESOLUTION[0] and configured_w >= TARGET_RESOLUTION[1]:
        # we downscale, so we first need to update the instances and then the pipeline
        pipeline.update_acquisition_parameters(config={
          "DEFAULT_H": TARGET_RESOLUTION[0],
          "DEFAULT_W": TARGET_RESOLUTION[1],
          "FRAME_H": TARGET_RESOLUTION[0],
          "FRAME_W": TARGET_RESOLUTION[1],

          "PREVIOUS_H": configured_h,
          "PREVIOUS_W": configured_w,
            })

        pipeline.deploy(timeout=10)
    # end for update each pipeline
    session._send_command_stop_node(node)
  # end for each node

  session.run(wait=5)
