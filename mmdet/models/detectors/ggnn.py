from ..builder import DETECTORS
from .two_stage import TwoStageDetector

# TODO: delete. This is exactly the same as Faster R-CNN.
#  We can just use the new bbox head with Faster R-CNN or other frameworks.

@DETECTORS.register_module
class GGNNRCNN(TwoStageDetector):

    def __init__(self,
                 backbone,
                 neck=None,
                 rpn_head=None,
                 roi_head=None,
                 train_cfg=None,
                 test_cfg=None,
                 pretrained=None):
        super(GGNNRCNN, self).__init__(
            backbone=backbone,
            neck=neck,
            rpn_head=rpn_head,
            roi_head=roi_head,
            train_cfg=train_cfg,
            test_cfg=test_cfg,
            pretrained=pretrained)