_base_ = './faster_rcnn_r50_fpn_sample1e-3_mstrain_1x_vg1000.py'
model = dict(pretrained=None, backbone=dict(depth=101,type='ResNeXt',groups=64,base_width=4))
data = dict(samples_per_gpu=2,workers_per_gpu=2)
work_dir = 'exps/vg/x101_64x4d'
load_from = 'checkpoints/cascade_rcnn_x101_64x4d_fpn_20e_coco_20200509_224357-051557b1.pth'
resume_from = None
