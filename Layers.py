
from gdsfactory.typings import Layer
from gdsfactory.technology.layer_map import LayerMap


class LayerMapFab(LayerMap):
    BH: Layer = (41, 0)
    BH_test: Layer = (902, 0)
    BHdmyA: Layer = (42, 0)
    BHdmyB: Layer = (43, 0)
    BlockFrame: Layer = (0, 1)
    DicingLine1: Layer = (171, 0)
    DicingLine2: Layer = (172, 0)
    DummyPattern: Layer = (906, 0)
    EBmrkEtch: Layer = (34, 0)
    EBmrkOpen: Layer = (35, 0)
    InGaAs: Layer = (91, 0)
    InPWG: Layer = (110, 0)
    InPWG1st: Layer = (111, 0)
    InPWG2nd: Layer = (112, 0)
    InPWaveGuideTrim_Test: Layer = (901, 0)
    Mark: Layer = (31, 0)
    MrkCover: Layer = (32, 0)
    MrkOpen: Layer = (33, 0)
    PadMetal: Layer = (126, 0)
    PadVia: Layer = (151, 0)
    ProcessCheck: Layer = (905, 0)
    ShotFrame: Layer = (0, 0)
    SiOxEtch: Layer = (141, 0)
    SiOxWG: Layer = (140, 0)
    TEST: Layer = (903, 0)
    Wafer: Layer = (999, 0)
    XOR: Layer = (904, 0)
    nDope: Layer = (71, 0)
    nMetal: Layer = (125, 0)
    nVia: Layer = (122, 0)
    pDope: Layer = (81, 0)
    pDpMask: Layer = (82, 0)
    pMetal: Layer = (124, 0)
    pVia: Layer = (121, 0)
    pnVia: Layer = (123, 0)


LAYER = LayerMapFab
