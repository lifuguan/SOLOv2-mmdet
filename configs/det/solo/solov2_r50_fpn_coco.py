'''
Author: your name
Date: 2022-01-01 15:25:20
LastEditTime: 2022-02-21 14:58:48
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /research_workspace/configs/det/knet/decoupled_solo_r50_fpn_coco.py
'''
_base_ = [
    "../_base_/models/solov2_r50_1x_fpn.py",
    '../_base_/datasets/coco_instance.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]