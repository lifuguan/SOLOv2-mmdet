'''
Author: your name
Date: 2022-02-21 14:59:30
LastEditTime: 2022-02-23 17:07:29
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /research_workspace/configs/det/_base_/models/solov2_r50_1x_fpn.py
'''

custom_imports = dict(
    imports=[
        "custommd.models.detectors.single_stage_ins",
        "custommd.models.detectors.solov2",
        "custommd.models.solov2.mask_feat_head",
        "custommd.models.solov2.solov2_head",
    ],
    allow_failed_imports=False)

model = dict(
    type='SOLOv2',
    pretrained='torchvision://resnet50',
    backbone=dict(
        type='ResNet',
        depth=50,
        num_stages=4,
        out_indices=(0, 1, 2, 3), # C2, C3, C4, C5
        frozen_stages=1,
        style='pytorch'),
    neck=dict(
        type='FPN',
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        start_level=0,
        num_outs=5),
    bbox_head=dict(
        type='SOLOv2Head',
        num_classes=81,
        in_channels=256,
        stacked_convs=4,
        seg_feat_channels=512,
        strides=[8, 8, 16, 32, 32],
        scale_ranges=((1, 96), (48, 192), (96, 384), (192, 768), (384, 2048)),
        sigma=0.2,
        num_grids=[40, 36, 24, 16, 12],
        ins_out_channels=256,
        loss_ins=dict(
            type='DiceLoss',
            use_sigmoid=True,
            loss_weight=3.0),
        loss_cate=dict(
            type='FocalLoss',
            use_sigmoid=True,
            gamma=2.0,
            alpha=0.25,
            loss_weight=1.0)),
    mask_head=dict(
            type='MaskFeatHead',
            in_channels=256,
            out_channels=128,
            start_level=0,
            end_level=3,
            num_classes=256,
            norm_cfg=dict(type='GN', num_groups=32, requires_grad=True)),
    # training and testing settings
    train_cfg = dict(),
    test_cfg = dict(
        nms_pre=500,
        score_thr=0.1,
        mask_thr=0.5,
        update_thr=0.05,
        kernel='gaussian',  # gaussian/linear
        sigma=2.0,
        max_per_img=100)
    )
