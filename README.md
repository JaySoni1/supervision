
# Supervision
[![version](https://badge.fury.io/py/supervision.svg)](https://badge.fury.io/py/supervision)
[![downloads](https://img.shields.io/pypi/dm/supervision)](https://pypistats.org/packages/supervision)
[![snyk](https://snyk.io/advisor/python/supervision/badge.svg)](https://snyk.io/advisor/python/supervision)
[![license](https://img.shields.io/pypi/l/supervision)](https://github.com/roboflow/supervision/blob/main/LICENSE.md)
[![python-version](https://img.shields.io/pypi/pyversions/supervision)](https://badge.fury.io/py/supervision)
[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/roboflow/supervision/blob/main/demo.ipynb)
[![gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/Roboflow/Annotators)
[![discord](https://img.shields.io/discord/1159501506232451173?logo=discord&label=discord&labelColor=fff&color=5865f2&link=https%3A%2F%2Fdiscord.gg%2FGbfgXGJ8Bk)](https://discord.gg/GbfgXGJ8Bk)
[![built-with-material-for-mkdocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)



</div>

## 👋 hello

**We write your reusable computer vision tools.** Whether you need to load your dataset from your hard drive, draw detections on an image or video, or count how many detections are in a zone. You can count on us! 🤝

## 💻 install

Pip install the supervision package in a
[**Python>=3.8**](https://www.python.org/) environment.

```bash
pip install supervision
```

Read more about conda, mamba, and installing from source in our [guide](https://roboflow.github.io/supervision/).

## 🔐 Environment Variables

Create a `.env` file to store sensitive configuration:

```bash
ROBOFLOW_API_KEY=your_api_key_here
LOG_LEVEL=INFO
```

Then load them in your code:
```python
from dotenv import load_dotenv

load_dotenv()  # Load before other imports
# Now use os.getenv() to access values
```


## 🔥 quickstart

### models

Supervision was designed to be model agnostic. Just plug in any classification, detection, or segmentation model. For your convenience, we have created [connectors](https://supervision.roboflow.com/latest/detection/core/#detections) for the most popular libraries like Ultralytics, Transformers, or MMDetection.

```python
import cv2
import supervision as sv
from ultralytics import YOLO

image = cv2.imread(...)
model = YOLO("yolov8s.pt")
result = model(image)[0]
detections = sv.Detections.from_ultralytics(result)

len(detections)
# 5
```

<details>
<summary>👉 more model connectors</summary>

- inference

  Running with [Inference](https://github.com/roboflow/inference) requires a [Roboflow API KEY](https://docs.roboflow.com/api-reference/authentication#retrieve-an-api-key).

  ```python
  import cv2
  import supervision as sv
  from inference import get_model

  image = cv2.imread(...)
  model = get_model(model_id="yolov8s-640", api_key=<ROBOFLOW API KEY>)
  result = model.infer(image)[0]
  detections = sv.Detections.from_inference(result)

  len(detections)
  # 5
  ```

</details>

### annotators

Supervision offers a wide range of highly customizable [annotators](https://supervision.roboflow.com/latest/detection/annotators/), allowing you to compose the perfect visualization for your use case.

```python
import cv2
import supervision as sv

image = cv2.imread(...)
detections = sv.Detections(...)

box_annotator = sv.BoxAnnotator()
annotated_frame = box_annotator.annotate(
  scene=image.copy(),
  detections=detections)
```

https://github.com/roboflow/supervision/assets/26109316/691e219c-0565-4403-9218-ab5644f39bce

### datasets

Supervision provides a set of [utils](https://supervision.roboflow.com/latest/datasets/core/) that allow you to load, split, merge, and save datasets in one of the supported formats.

```python
import supervision as sv
from roboflow import Roboflow

project = Roboflow().workspace(<WORKSPACE_ID>).project(<PROJECT_ID>)
dataset = project.version(<PROJECT_VERSION>).download("coco")

ds = sv.DetectionDataset.from_coco(
    images_directory_path=f"{dataset.location}/train",
    annotations_path=f"{dataset.location}/train/_annotations.coco.json",
)

path, image, annotation = ds[0]
    # loads image on demand

for path, image, annotation in ds:
    # loads image on demand
```

<details close>
<summary>👉 more dataset utils</summary>

- load

  ```python
  dataset = sv.DetectionDataset.from_yolo(
      images_directory_path=...,
      annotations_directory_path=...,
      data_yaml_path=...
  )

  dataset = sv.DetectionDataset.from_pascal_voc(
      images_directory_path=...,
      annotations_directory_path=...
  )

  dataset = sv.DetectionDataset.from_coco(
      images_directory_path=...,
      annotations_path=...
  )
  ```

- split

  ```python
  train_dataset, test_dataset = dataset.split(split_ratio=0.7)
  test_dataset, valid_dataset = test_dataset.split(split_ratio=0.5)

  len(train_dataset), len(test_dataset), len(valid_dataset)
  # (700, 150, 150)
  ```

- merge

  ```python
  ds_1 = sv.DetectionDataset(...)
  len(ds_1)
  # 100
  ds_1.classes
  # ['dog', 'person']

  ds_2 = sv.DetectionDataset(...)
  len(ds_2)
  # 200
  ds_2.classes
  # ['cat']

  ds_merged = sv.DetectionDataset.merge([ds_1, ds_2])
  len(ds_merged)
  # 300
  ds_merged.classes
  # ['cat', 'dog', 'person']
  ```

- save

  ```python
  dataset.as_yolo(
      images_directory_path=...,
      annotations_directory_path=...,
      data_yaml_path=...
  )

  dataset.as_pascal_voc(
      images_directory_path=...,
      annotations_directory_path=...
  )

  dataset.as_coco(
      images_directory_path=...,
      annotations_path=...
  )
  ```

- convert

  ```python
  sv.DetectionDataset.from_yolo(
      images_directory_path=...,
      annotations_directory_path=...,
      data_yaml_path=...
  ).as_pascal_voc(
      images_directory_path=...,
      annotations_directory_path=...
  )
  ```

</details>

## Key Features
Supervision provides a comprehensive set of tools for building computer vision applications. Here are the main features that make supervision powerful and easy to use:

## Monitoring
Monitor your computer vision models in production with built-in tools:

python
import supervision as sv

# Create a performance monitor
monitor = sv.Monitor()

# Track inference time, FPS, and resource usage
with monitor:
    detections = model(image)

print(f"Inference time: {monitor.inference_time:.4f}s")
print(f"FPS: {monitor.fps:.2f}")
Use the VideoMetricMonitor to track metrics over video streams:
pythonvideo_monitor = sv.VideoMetricMonitor()
for frame in video_source:
    with video_monitor:
        detections = model(frame)
    
  # Access running metrics
    if video_monitor.frame_count % 100 == 0:
        print(f"Average FPS: {video_monitor.avg_fps:.2f}")
        print(f"Processing time: {video_monitor.total_time:.2f}s")

## Alerting
Set up alerts for specific conditions using detection filters and callbacks:

python
import supervision as sv

# Create an alert for when people are detected in a restricted zone
zone = sv.PolygonZone(polygon=[[0, 0], [0, 100], [100, 100], [100, 0]], frame_resolution_wh=(640, 480))
alert = sv.Alert(
    trigger_condition=lambda detections: zone.trigger(detections=detections.filter(class_id=0)),  # class_id 0 is person
    cooldown_period=5.0  # seconds
)

# Register callbacks for when the alert is triggered
alert.on_triggered(
    lambda: print("ALERT: Person detected in restricted zone!")
)

# Use in your detection loop
while True:
    detections = model(frame)
    alert.process(detections=detections)

## Automation
Automate routine tasks with the built-in automation tools:
pythonimport supervision as sv

# Automatically save frames with detections
auto_saver = sv.AutoSaver(
    output_dir="detections/",
    min_confidence=0.5,
    classes_of_interest=[0, 1]  # Save only when persons or cars are detected
)

# Use in your detection loop
for frame in video_source:
    detections = model(frame)
    auto_saver.process(frame=frame, detections=detections)
Create custom automation pipelines with the processing framework:
pythonimport supervision as sv

# Define a processing pipeline
pipeline = sv.ProcessingPipeline([
    sv.DetectionFilter(class_id=[0]),  # Keep only person detections
    sv.TrackingMatcher(tracker=sv.ByteTrack()),  # Add tracking
    sv.FilterMovingObjects(min_distance=15),  # Filter stationary objects
    sv.FrameSaver(output_dir="moving_people/")  # Save frames
])

# Process video frames
for frame in video_source:
    detections = model(frame)
    result = pipeline.process(frame=frame, detections=detections)

## Advanced Analysis
Extract meaningful insights from your video data:
python
import supervision as sv

# Count objects crossing a line
line_counter = sv.LineZoneAnnotator(
    thickness=2,
    text_thickness=1,
    text_scale=0.5
)
line_zone = sv.LineZone(start=Point(50, 50), end=Point(400, 50))

# Use tracker for consistent counting
tracker = sv.ByteTrack()

for frame in video_source:
    detections = model(frame)
    detections = tracker.update_with_detections(detections)
    
  # Count and annotate
    line_zone.trigger(detections=detections)
    annotated_frame = line_counter.annotate(
        scene=frame.copy(),
        line_zone=line_zone
    )
    
    print(f"Objects in: {line_zone.in_count}, Objects out: {line_zone.out_count}")

## Data Pipeline Tools
Use powerful data transformation tools for preprocessing and augmentation:

python
import supervision as sv

# Create transformations for dataset augmentation
transforms = sv.TransformPipeline([
    sv.RandomBrightness(brightness_factor=0.2),
    sv.RandomNoise(noise_factor=0.05),
    sv.RandomFlip(flip_probability=0.5),
    sv.CenterCrop(crop_width=300, crop_height=300)
])

# Apply to your dataset during training
for image, annotations in dataset:
    transformed_image, transformed_annotations = transforms(
        image=image, 
        annotations=annotations
    )

For more detailed explanations and advanced usage examples, check our full documentation.

## 💜 built with supervision

https://user-images.githubusercontent.com/26109316/207858600-ee862b22-0353-440b-ad85-caa0c4777904.mp4

https://github.com/roboflow/supervision/assets/26109316/c9436828-9fbf-4c25-ae8c-60e9c81b3900

https://github.com/roboflow/supervision/assets/26109316/3ac6982f-4943-4108-9b7f-51787ef1a69f

## 📚 documentation

Visit our [documentation](https://roboflow.github.io/supervision) page to learn how supervision can help you build computer vision applications faster and more reliably.

## 🏆 contribution

We love your input! Please see our [contributing guide](https://github.com/roboflow/supervision/blob/main/CONTRIBUTING.md) to get started. Thank you 🙏 to all our contributors!

