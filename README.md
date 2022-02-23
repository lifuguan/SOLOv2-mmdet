<!--
 * @Author: your name
 * @Date: 2021-12-13 18:14:32
 * @LastEditTime: 2022-02-23 18:22:09
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: /research_workspace/README.md
-->
# SOLOv2 : mmdetection(2.19.0) implementation

This project hosts the code for implementing the SOLOv2 algorithms based on the [**official project**](https://github.com/WXinlong/SOLO). Due to the inheritance designation, it enables developers as well as researchers to integrate into their projects more easily and elegantly.

该SOLOv2项目是基于[**官方项目**](https://github.com/WXinlong/SOLO)并在 **mmdetection(2.19.0)** 上实现的。由于采用继承设计，它使得开发人员和研究人员能够更轻松，更优雅地集成到自己的项目中。
> [**SOLOv2: Dynamic and Fast Instance Segmentation**](https://arxiv.org/abs/2003.10152),            
> Xinlong Wang, Rufeng Zhang, Tao Kong, Lei Li, Chunhua Shen     
> In: Proc. Advances in Neural Information Processing Systems (NeurIPS), 2020  
> *arXiv preprint ([arXiv 2003.10152](https://arxiv.org/abs/2003.10152))*  



## Installation
It requires the following OpenMMLab packages:
- **MMDetection >= 2.14.0**
- Linux
- Python 3.7
- PyTorch >= 1.6
- torchvision 0.7.0
- CUDA 10.1
- NCCL 2
- GCC >= 5.4.0
- MMCV >= 1.3.8

## Usage
### Data preparation

Prepare data following [MMDetection](https://github.com/open-mmlab/mmdetection) and [MMSegmentation](https://github.com/open-mmlab/mmsegmentation). The data structure looks like below:

```bash
data/
├── coco
│   ├── annotations
│   │   ├── panoptic_{train,val}2017.json
│   │   ├── instance_{train,val}2017.json
│   │   ├── panoptic_{train,val}2017/  # panoptic png annotations
│   │   ├── image_info_test-dev2017.json  # for test-dev submissions
│   ├── train2017
│   ├── val2017
│   ├── test2017
```

### Training and testing

You can run training and testing without slurm by directly using mim for instance segmentation like below:

```bash
# SOLOv2 training
export CUDA_VISIBLE_DEVICES=1,2,3,4,5,6,7
export PYTHONPATH=$PWD:$PYTHONPATH  
./tools/dist_train.sh ${CONFIG_FILE} ${GPU_NUM}

Example:
./tools_det/dist_train.sh configs/det/solo/solov2_r50_fpn_coco.py 7

# SOLOv2 inference
./tools/dist_test.sh ${CONFIG_FILE} ${CHECKPOINT_FILE} ${GPU_NUM}  --show --out  ${OUTPUT_FILE} --eval segm

Example:
./tools/dist_test.sh configs/det/solo/solov2_r50_fpn_coco.py work_dirs/solov2_r50_fpn_coco/latest.pth 1 --eval segm
```

## VSCode debugger launch config 
```json 
{
    "env": {"PYTHONPATH" : "${workspaceRoot}"},
    "name": "knet:debug",
    "type": "python",
    "request": "launch",
    "program": "${workspaceRoot}/tools/train.py",
    "console": "integratedTerminal",
    "justMyCode": false,
    "args": ["configs/det/knet/knet_s3_r50_fpn_1x_ctw1500.py","--gpus", "1"]
},
```

## Model

Model | Multi-scale training | Testing time / im | AP (minival) | Link
--- |:---:|:---:|:---:|:---:
SOLO_R50_1x | No | 77ms | 32.9 | [download](https://cloudstor.aarnet.edu.au/plus/s/nTOgDldI4dvDrPs/download)
SOLO_R50_3x | Yes | 77ms |  35.8 | [download](https://cloudstor.aarnet.edu.au/plus/s/x4Fb4XQ0OmkBvaQ/download)
SOLO_R101_3x | Yes | 86ms |  37.1 | [download](https://cloudstor.aarnet.edu.au/plus/s/WxOFQzHhhKQGxDG/download)
Decoupled_SOLO_R50_1x | No | 85ms | 33.9 | [download](https://cloudstor.aarnet.edu.au/plus/s/RcQyLrZQeeS6JIy/download)
Decoupled_SOLO_R50_3x | Yes | 85ms | 36.4 | [download](https://cloudstor.aarnet.edu.au/plus/s/dXz11J672ax0Z1Q/download)
Decoupled_SOLO_R101_3x | Yes | 92ms | 37.9 | [download](https://cloudstor.aarnet.edu.au/plus/s/BRhKBimVmdFDI9o/download)
SOLOv2_R50_1x | No | 54ms | 34.8 | [download](https://cloudstor.aarnet.edu.au/plus/s/DvjgeaPCarKZoVL/download)
SOLOv2_R50_3x | Yes | 54ms | 37.5 | [download](https://cloudstor.aarnet.edu.au/plus/s/nkxN1FipqkbfoKX/download)
SOLOv2_R101_3x | Yes | 66ms | 39.1 | [download](https://cloudstor.aarnet.edu.au/plus/s/61WDqq67tbw1sdw/download)
SOLOv2_R101_DCN_3x | Yes | 97ms | 41.4 | [download](https://cloudstor.aarnet.edu.au/plus/s/4ePTr9mQeOpw0RZ/download)
SOLOv2_X101_DCN_3x | Yes | 169ms | 42.4 | [download](https://cloudstor.aarnet.edu.au/plus/s/KV9PevGeV8r4Tzj/download)

## Contributing to the project
Any pull requests or issues are welcome.

## Citations
Please consider citing our papers in your publications if the project helps your research. BibTeX reference is as follows.
```
@inproceedings{wang2020solo,
  title     =  {{SOLO}: Segmenting Objects by Locations},
  author    =  {Wang, Xinlong and Kong, Tao and Shen, Chunhua and Jiang, Yuning and Li, Lei},
  booktitle =  {Proc. Eur. Conf. Computer Vision (ECCV)},
  year      =  {2020}
}
```

```
@article{wang2020solov2,
  title={SOLOv2: Dynamic and Fast Instance Segmentation},
  author={Wang, Xinlong and Zhang, Rufeng and  Kong, Tao and Li, Lei and Shen, Chunhua},
  journal={Proc. Advances in Neural Information Processing Systems (NeurIPS)},
  year={2020}
}
```

## License

For academic use, this project is licensed under the 2-clause BSD License - see the LICENSE file for details. For commercial use, please contact [Xinlong Wang](https://www.xloong.wang/) and  [Chunhua Shen](https://cs.adelaide.edu.au/~chhshen/).

