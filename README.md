# cv-car-dashboard

The cv-car-dashboard repository contains files for an object detection demo using YOLOv4 that runs on an Intel Neural Compute Stick 2 connected to a Raspberry Pi 4B. The demo can be used to detect a variety of objects, and will sound a buzzer connected to pin 5 when it detects road object such as ccars, pedestrians, and cyclists.

## Environment

To set up the demo, you will need a Raspberry Pi 4B, a Neural Compute Stick 2, and a camera. Then, you will need the following installed:

* Python 3.7<sup>*</sup>
* OpenVINO 2022.2 complete with the USB rules for the Neural Compute Stick (refer to this [guide](https://docs.openvino.ai/2022.2/openvino_docs_install_guides_installing_openvino_raspbian.html))

<sup>*</sup>Ensure that the shared libraries can be read (libpython3.7m.so)

## Usage 

To use the demo, simply connect the camera and Intel Neural Compute Stick 2 to the Raspberry Pi and run the demo script. The script will start the object detection process and display the results on the screen. The demo will also sound the buzzer and display red bounding boxes for road objects.
