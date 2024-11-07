from naeural_client import Session, Pipeline, Instance, Payload

TARGET_NODE = "nen-2"
TARGET_PIPELINE = "pp"
TARGET_SIGNATURE = "sig"
TARGET_INSTANCE = "inst"


def on_data(pipeline: Pipeline, payload: Payload):
  images = payload.get("DATA")
  if images is not None:
    if isinstance(images, list):
      pipeline.P("Found {} images".format(len(images)))
    else:
      pipeline.P("Found 1 image")
  return


if __name__ == "__main__":
  session = Session(root_topic="lummetry")

  if not session.wait_for_node(TARGET_NODE):
    session.P("Node {} not found".format(TARGET_NODE))
    exit(1)

  pipeline: Pipeline = session.attach_to_pipeline(node=TARGET_NODE, name=TARGET_PIPELINE)

  instance: Instance = pipeline.attach_to_plugin_instance(
    signature=TARGET_SIGNATURE,
    instance_id=TARGET_INSTANCE,
    on_data=on_data,
  )

  session.run(wait=True)
