
###
 # @Author: your name
 # @Date: 2021-12-29 17:55:49
 # @LastEditTime: 2022-02-23 17:32:21
 # @LastEditors: Please set LastEditors
 # @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 # @FilePath: /research_workspace/train.sh
### 

# SOLOv2 training
export CUDA_VISIBLE_DEVICES=1,2,3,4,5,6,7
export PYTHONPATH=$PWD:$PYTHONPATH  
./tools/dist_train.sh configs/det/solo/solov2_r50_fpn_coco.py 7
