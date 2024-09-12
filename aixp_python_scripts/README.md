# Python Scripts updating pipeline and plugin configuration

To use these scripts, you have to do 2 things:

1. create a `.env` file in this folder, containing the connection details

2. copy `_solis_client` folder from SolisClient in this folder, then rename it to `_local_cache`

## Camera resolution conversion

This script allows users to update the acquisition resolution on all cameras on a set of nodes.

This operation also updates all points and zones configured on each plugin on each camera.

### Pre-requirements

Open the `convert_all_points_to_a_different_resolution.py` file and fill in `TARGET_NODES`.

Make sure all cameras on those nodes are consumed at the same `ASSUMED_DEFAULT_RESOLUTION` or that these were updated before with either `convert_all_points_to_a_different_resolution.py` or `convert_all_points_to_a_different_resolution_v2.py`.

If you cannot make an assumption about the resolutions of all cameras on a node, see the next section.

### Run

```bash

python3 convert_all_points_to_a_different_resolution.py

```

## Automatic camera resolution conversion

These scripts allow users to update the acquisition resolution on all cameras on a set of nodes.

This operation also updates all the points configured on each plugin on each camera.

Use these when you cannot make an assumption about the resolutions of all cameras on a node. These scripts will extract for each node, for each camera, the acquisition resolution and will convert to the target resolution based on this.

The scripts will assume that the current configuration (points, zones, acquisition resolution) is correct and should be upscaled or downscaled.

### Pre-requirements

Open the `get_all_video_resolution.py` file and fill in `TARGET_NODES`.

All points and zones on all plugins were configured on the current acquisition resolution of the camera.

### Run

```bash

python3 get_all_video_resolution.py
python3 convert_all_points_to_a_different_resolution_v2.py

```

## Check number of images a plugin sends

This script will listen for payloads of a plugin and output on the screen the number of images contained in each payload

### Pre-requirements

Open the `get_nr_images_in_payload.py` file and fill in `TARGET_NODE`, `TARGET_PIPELINE`, `TARGET_SIGNATURE`, `TARGET_INSTANCE`.

### Run

```bash

python3 get_nr_images_in_payload.py

```

## Bulk change plugins configuration

This script will update all plugins with the specified configuration on all online nodes.

### Pre-requirements

Open the `bulk_change_plugins_parameters.py` file and fill in the target configuration for multiple plugins.

### Run

```bash

python3 bulk_change_plugins_parameters.py

```
