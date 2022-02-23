'''
Author: your name
Date: 2022-02-21 11:46:21
LastEditTime: 2022-02-22 11:15:59
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /research_workspace/custommd/models/detectors/solov2.py
'''
from operator import ipow


from .single_stage_ins import SingleStageInsDetector
# from mmdet.models.detectors.single_stage_instance_seg import SingleStageInstanceSegmentor
from mmdet.models.builder import DETECTORS


@DETECTORS.register_module()
class SOLOv2(SingleStageInsDetector):

    def __init__(self, *args, **kwargs):
        super(SOLOv2, self).__init__(*args, **kwargs)