'''
Author: your name
Date: 2021-12-20 16:47:41
LastEditTime: 2022-01-10 21:05:29
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /research_workspace/tools_det/demo.py
'''

from argparse import ArgumentParser
import cv2

from mmdet.apis import (async_inference_detector, inference_detector,
                        init_detector, show_result_pyplot)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('img', help='Image file')
    parser.add_argument('out', help='Image file')
    parser.add_argument('config', help='Config file')
    parser.add_argument('checkpoint', help='Checkpoint file')
    parser.add_argument(
        '--device', default='cuda:0', help='Device used for inference')
    parser.add_argument(
        '--score-thr', type=float, default=0.30, help='bbox score threshold')
    args = parser.parse_args()
    return args

def show_result_pyplot(model,
                       img,
                       result,
                       out_file, #加入out_file，运行时把改行注释删除
                       score_thr=0.5):
    if hasattr(model, 'module'):
        model = model.module
    res_img = model.show_result(
        img,
        result,
        score_thr=score_thr,
        show=False
        )
    cv2.imwrite(out_file, res_img)
    

def main(args):
    # build the model from a config file and a checkpoint file
    model = init_detector(args.config, args.checkpoint, device=args.device)
    # test a single image
    result = inference_detector(model, args.img)
    # show the results
    show_result_pyplot(model, args.img, result, args.out, score_thr=args.score_thr)


if __name__ == '__main__':
    args = parse_args()
    main(args)

