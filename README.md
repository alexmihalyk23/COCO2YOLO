# COCO2YOLO
COCO to YOLO converter

# Usage

`python COCO2YOLO.py -j coco.json -o path_to_dir`
### Or download [Release](https://github.com/alexmihalyk23/COCO2YOLO/releases/tag/v1.0.0) and run
`COCO2YOLO.exe -j coco.json -o path_to_dir`

# To test the conversion you can run test.py
`python test.py -i img.jpg -t converted_to_yolo.txt`
## Or
`python test_with_labels.py -i img.jpg -t converted_to_yolo.txt -l labels.txt`
