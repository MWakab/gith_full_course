import numpy as np
import gdsfactory as gf
from Layers import LAYER

##各レイヤーにおける、コンポーネント関数を定義

class BaseParts:
    @gf.cell
    def BHetch(width,length,shift,layer) :
        c=gf.Component()
        d=gf.Component()
        BHpoints=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(BHpoints,layer=layer)
        
        d.add_port("o1", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("o2", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("o3", center=(-shift,width/2), width=width, orientation=180,layer=layer) #for Ports of SiOx-WG
        d.add_port("o4", center=(length+shift,width/2), width=width,orientation=0,layer=layer) #for Ports of SiOx-WG
        d.add_port("e1", center=(length/2,width), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0), width=length,orientation=270,layer=layer,port_type="electrical")
        d.add_port("e3", center=(length/2,width/2), width=1,orientation=90,layer=layer,port_type="electrical")
        d.add_port("e4", center=(length/2,width/2), width=1,orientation=270,layer=layer,port_type="electrical")
        
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？ 
        c.add_ports(c1.ports,prefix="BH-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def BHdummy(width,length,spacer,layer):
        c=gf.Component()
        d=gf.Component()
        BHdummyPoints=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(BHdummyPoints,layer=layer)
        d.add_port("o1", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("o2", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("e1", center=(length/2,width+spacer), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0-spacer), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？ 
        c.add_ports(c1.ports,prefix="BHdummy-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def nDpA(width,length,spacer,layer):
        c=gf.Component()
        d=gf.Component()
        nDpApoints=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(nDpApoints,layer=layer)
        d.add_port("o1", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("o2", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("e1", center=(length/2,width+spacer), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0-spacer), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="nDpA-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def pDpA(width,length,spacer,layer):
        c=gf.Component()
        d=gf.Component()
        pDpApoints=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(pDpApoints,layer=layer)
        d.add_port("o1", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("o2", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("e1", center=(length/2,width+spacer), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0-spacer), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="pDpA-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def InGaAsEtch(width,length,spacer,layer):
        c=gf.Component()
        d=gf.Component()
        IGSpoints=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(IGSpoints,layer=layer)
        d.add_port("o1", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("o2", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("e1", center=(length/2,width+spacer), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0-spacer), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="InGaAs-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell #taper導波路部左側の定義ファイル。曲げ対応予定。現在ストレートのみ可。
    def InGaAsEtch_Lbend(width,TipLn,TipDLn,radius,BendAngle,layer) : 
        #InPのテーパ先端部をポリゴンで別のコンポーネントで作成（後でメインのコンポーネントに加える）
        d=gf.Component()
        Points=[(-width*np.sqrt(3)/2,width/2),(0,width),(0,0)]
        d.add_polygon(Points,layer=layer)
        d.add_port("o1", center=(0,1/2*width), width=width, orientation=0,layer=layer)
        #d.add_port("o2", center=(-1/4*width,3/4*width), width=width, orientation=0,layer=layer)
        
        c=gf.Component()
        #非マンハッタン接続のためcreate_vinstを用いる（仮想インスタンスとのこと）
        c1 = c.create_vinst(d)
        #c0 = c.create_vinst(gf.components.taper(length=18,width1=width/np.sqrt(2),width2=width/np.sqrt(2),layer=layer))
        c2 = c.create_vinst(gf.components.bend_euler_all_angle(width=width,angle=BendAngle, radius=radius,layer=layer))
        c3 = c.create_vinst(gf.components.taper(length=TipLn+TipDLn+5,width1=width,width2=width,layer=layer))
        
        #c0.connect(port="o1",other=c1.ports["o2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        c1.connect(port="o1",other=c2.ports["o2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        c3.connect(port="o2",other=c2.ports["o1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        
        c.add_ports(c1.ports,prefix="Add-L-")
        c.add_ports(c2.ports,prefix="Bend-L-")
        #c.add_ports(c4.ports,prefix="Tip-Lr-")
        # c.pprint_ports() #port定義を表示
        return c
    @gf.cell #taper導波路部左側の定義ファイル。曲げ対応予定。現在ストレートのみ可。
    def InGaAsEtch_Rbend(width,TipLn,TipDLn,radius,BendAngle,layer) : 
        #InPのテーパ先端部をポリゴンで別のコンポーネントで作成（後でメインのコンポーネントに加える）
        d=gf.Component()
        Points=[(width*np.sqrt(3)/2,width/2),(0,width),(0,0)]
        d.add_polygon(Points,layer=layer)
        d.add_port("o2", center=(0,1/2*width), width=width, orientation=180,layer=layer)
        #d.add_port("o2", center=(-1/4*width,3/4*width), width=width, orientation=0,layer=layer)
        
        c=gf.Component()
        #非マンハッタン接続のためcreate_vinstを用いる（仮想インスタンスとのこと）
        c1 = c.create_vinst(d)
        #c0 = c.create_vinst(gf.components.taper(length=18,width1=width/np.sqrt(2),width2=width/np.sqrt(2),layer=layer))
        c2 = c.create_vinst(gf.components.bend_euler_all_angle(width=width,angle=BendAngle, radius=radius,layer=layer))
        c3 = c.create_vinst(gf.components.taper(length=TipLn+TipDLn+5,width1=width,width2=width,layer=layer))
        
        #c0.connect(port="o1",other=c1.ports["o2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        c1.connect(port="o2",other=c2.ports["o1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        c3.connect(port="o1",other=c2.ports["o2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        
        c.add_ports(c1.ports,prefix="Add-R-")
        c.add_ports(c2.ports,prefix="Bend-R-")
        #c.add_ports(c4.ports,prefix="Tip-Lr-")
        # c.pprint_ports() #port定義を表示
        return c
    
    @gf.cell
    def Device(width,length,layer):
        c=gf.Component()
        d=gf.Component()
        DEVpoints=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(DEVpoints,layer=layer)
        d.add_port("o1", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("o2", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("e1", center=(length/2,width), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0), width=length,orientation=270,layer=layer,port_type="electrical")
        d.add_port("e3", center=(length/2,width/2), width=1,orientation=90,layer=layer,port_type="electrical")
        d.add_port("e4", center=(length/2,width/2), width=1,orientation=270,layer=layer,port_type="electrical")
        
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="Device-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell()
    def InPWG(Type,St1Ln,St1Wd,TaperLn,TaperWd1,TaperWd2,St2Ln,St2Wd,St3Ln,St3Wd,TipLn,TipWd,radius,BendAngle,layer) : 
        c=gf.Component()
        #非マンハッタン接続のためcreate_vinstを用いる（仮想インスタンスとのこと）
        c0 = c.create_vinst(gf.components.taper(length=0,width1=St1Wd,width2=St1Wd,layer=layer)) #各コンポーネントとの接続用0次元ポート
        c1 = c.create_vinst(gf.components.taper(length=St1Ln,width1=St1Wd,width2=St1Wd,layer=layer))
        if Type=="L":
            c2 = c.create_vinst(gf.components.taper(length=TaperLn,width1=TaperWd2,width2=TaperWd1,layer=layer))
            c7 = c.create_vinst(gf.components.taper(length=TipLn,width1=TipWd,width2=St3Wd,layer=layer))
        elif Type=="R":
            c2 = c.create_vinst(gf.components.taper(length=TaperLn,width1=TaperWd1,width2=TaperWd2,layer=layer))
            c7 = c.create_vinst(gf.components.taper(length=TipLn,width1=St3Wd,width2=TipWd,layer=layer))
        c3 = c.create_vinst(gf.components.taper(length=St2Ln,width1=St2Wd,width2=St2Wd,layer=layer))    
        c4 = c.create_vinst(gf.components.bend_euler_all_angle(angle=BendAngle,width=St2Wd,radius=radius,layer=layer))
        c5 = c.create_vinst(gf.components.taper(length=St3Ln,width1=St3Wd,width2=St3Wd,layer=layer))
        c6 = c.create_vinst(gf.components.taper(length=0,width1=St3Wd,width2=St3Wd,layer=layer)) #各コンポーネントとの接続用0次元ポート
        c8 = c.create_vinst(gf.components.taper(length=0,width1=TipWd,width2=TipWd,layer=layer)) #各コンポーネントとの接続用0次元ポート
        
        if Type=="L":
            c1.connect(port="o2",other=c0.ports["o1"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c2.connect(port="o2",other=c1.ports["o1"], allow_width_mismatch=True,allow_layer_mismatch=True)
            c3.connect(port="o2",other=c2.ports["o1"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c4.connect(port="o2",other=c3.ports["o1"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c5.connect(port="o2",other=c4.ports["o1"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c6.connect(port="o2",other=c5.ports["o1"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c7.connect(port="o2",other=c6.ports["o1"], allow_width_mismatch=True,allow_layer_mismatch=True)
            c8.connect(port="o2",other=c7.ports["o1"], allow_width_mismatch=False,allow_layer_mismatch=True)

            
            c.add_ports(c0.ports,prefix="St-L-")
            c.add_ports(c6.ports,prefix="TipL-root-")
            c.add_ports(c7.ports,prefix="Tip-L-")
        elif Type=="R":
            c1.connect(port="o1",other=c0.ports["o2"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c2.connect(port="o1",other=c1.ports["o2"], allow_width_mismatch=True,allow_layer_mismatch=True)
            c3.connect(port="o1",other=c2.ports["o2"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c4.connect(port="o1",other=c3.ports["o2"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c5.connect(port="o1",other=c4.ports["o2"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c6.connect(port="o1",other=c5.ports["o2"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c7.connect(port="o1",other=c6.ports["o2"], allow_width_mismatch=True,allow_layer_mismatch=True)
            c8.connect(port="o2",other=c7.ports["o2"], allow_width_mismatch=False,allow_layer_mismatch=True)
            
            c.add_ports(c0.ports,prefix="St-R-")
            c.add_ports(c6.ports,prefix="TipR-root-")
            c.add_ports(c7.ports,prefix="Tip-R-")
        # c.pprint_ports() #port定義を表示
        return c
    @gf.cell #taper導波路部左側の定義ファイル。曲げ対応予定。現在ストレートのみ可。
    def InPWG1st(Type,St1Ln,St1Wd,TaperLn,TaperWd1,TaperWd2,St2Ln,St2Wd,St3Ln,St3Wd,TipLn,TipDLn,TipWd,radius,BendAngle,layer) : 
        #InPのテーパ先端部をポリゴンで別のコンポーネントで作成（後でメインのコンポーネントに加える）
        d=gf.Component()
        if Type=="L":
            TipPoints=[(-TipLn,1/2*(St3Wd+TipWd)),(0,St3Wd),(0,0),(-TipLn,-1/2*(St3Wd-TipWd))]
            d.add_polygon(TipPoints,layer=layer)
            d.add_port("o1", center=(-TipLn,-1/2*(-TipWd)), width=St3Wd, orientation=180,layer=layer)
            d.add_port("o2", center=(0,St3Wd/2), width=St3Wd,orientation=0,layer=layer)
        elif Type=="R":
            TipPoints=[(0,0),(0,St3Wd),(TipLn,1/2*(St3Wd+TipWd)),(TipLn,-1/2*(St3Wd-TipWd))]
            d.add_polygon(TipPoints,layer=layer)
            d.add_port("o1", center=(0,St3Wd/2), width=St3Wd, orientation=180,layer=layer)
            d.add_port("o2", center=(TipLn,-1/2*(-TipWd)), width=St3Wd,orientation=0,layer=layer)
        #メインのInPWG1stのコンポーネント
        c=gf.Component()
        #非マンハッタン接続のためcreate_vinstを用いる（仮想インスタンスとのこと）
        
        c1 = c.create_vinst(gf.components.taper(length=St1Ln,width1=St1Wd,width2=St1Wd,layer=layer))
        if Type=="L":
            c2 = c.create_vinst(gf.components.taper(length=TaperLn,width1=TaperWd2,width2=TaperWd1,layer=layer))
        elif Type=="R":
            c2 = c.create_vinst(gf.components.taper(length=TaperLn,width1=TaperWd1,width2=TaperWd2,layer=layer))
        c3 = c.create_vinst(gf.components.taper(length=St2Ln,width1=St2Wd,width2=St2Wd,layer=layer))
        c4 = c.create_vinst(gf.components.bend_euler_all_angle(angle=BendAngle,width=St2Wd,radius=radius ,layer=layer ))
        c5 = c.create_vinst(gf.components.taper(length=St3Ln,width1=St3Wd,width2=St3Wd,layer=layer))
        c6 = c.create_vinst(gf.components.taper(length=0,width1=St3Wd,width2=St3Wd,layer=layer))
        c7 = c.create_vinst(d)
        c8 = c.create_vinst(gf.components.taper(length=TipDLn,width1=St3Wd,width2=St3Wd,layer=layer))
        
        if Type=="L":
            
            c2.connect(port="o2",other=c1.ports["o1"], allow_width_mismatch=True,allow_layer_mismatch=True)
            c3.connect(port="o2",other=c2.ports["o1"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c4.connect(port="o2",other=c3.ports["o1"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c5.connect(port="o2",other=c4.ports["o1"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c6.connect(port="o2",other=c5.ports["o1"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c7.connect(port="o2",other=c6.ports["o1"], allow_width_mismatch=True,allow_layer_mismatch=True)
            c8.connect(port="o2",other=c7.ports["o1"], allow_width_mismatch=False,allow_layer_mismatch=True)

            
            
            c.add_ports(c1.ports,prefix="Taper-L-")
            c.add_ports(c6.ports,prefix="Tip-L-")
        elif Type=="R":
            
            c2.connect(port="o1",other=c1.ports["o2"], allow_width_mismatch=True,allow_layer_mismatch=True)
            c3.connect(port="o1",other=c2.ports["o2"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c4.connect(port="o1",other=c3.ports["o2"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c5.connect(port="o1",other=c4.ports["o2"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c6.connect(port="o1",other=c5.ports["o2"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c7.connect(port="o1",other=c6.ports["o2"], allow_width_mismatch=True,allow_layer_mismatch=True)
            c8.connect(port="o2",other=c7.ports["o2"], allow_width_mismatch=False,allow_layer_mismatch=True)
            
        
            c.add_ports(c1.ports,prefix="Taper-R-")
            c.add_ports(c6.ports,prefix="Tip-R-")
    
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def InPWG2nd(Type,TrimLn,TrimWd,TrimAddLn,TrimAddWd,TaperWd,TipWd,layer) :
        #InPのテーパ先端部をポリゴンで別のコンポーネントで作成（後でメインのコンポーネントに加える）
        TrimEscDistance = 0.5
        TrimEscLn = 10
        d=gf.Component()
        e=gf.Component()
        if Type=="L":
            TrimPoints=[(0,0),(0,TrimWd),(0,TrimWd+TrimAddWd),(TrimAddLn,TrimWd+TrimAddWd),(TrimAddLn,TrimWd-TrimAddLn/TrimLn*(TaperWd-TipWd)/2),(TrimAddLn+TrimLn,TrimWd-(1+TrimAddLn/TrimLn)*(TaperWd-TipWd)/2),(TrimAddLn+TrimLn,-(1+TrimAddLn/TrimLn)*(TaperWd-TipWd)/2),(TrimAddLn,-TrimAddLn/TrimLn*(TaperWd-TipWd)/2)]
            d.add_polygon(TrimPoints,layer=layer)
            d.add_port("o1", center=(TrimAddLn       ,TrimWd-(  TrimAddLn/TrimLn)*(TaperWd-TipWd)/2+TipWd/2), width=TipWd, orientation=180,layer=layer)
            d.add_port("o2", center=(TrimAddLn+TrimLn,TrimWd-(1+TrimAddLn/TrimLn)*(TaperWd-TipWd)/2+TaperWd/2), width=TaperWd,orientation=0,layer=layer) #Taper導波路とport接続するため、portの座標をあえてずらす。
            d.add_port("o3", center=(TrimAddLn+TrimLn,      -(1+TrimAddLn/TrimLn)*(TaperWd-TipWd)/2+ TrimWd/2), width=TrimWd,orientation=0,layer=layer)
            TrimESCPoints=[(0,0), (0,TrimWd),(TrimEscLn*np.sqrt(1-(TrimEscDistance/TrimEscLn)**2),TrimWd-TrimEscLn*TrimEscDistance/TrimEscLn),(TrimEscLn*np.sqrt(1-(TrimEscDistance/TrimEscLn)**2),-TrimEscLn*TrimEscDistance/TrimEscLn)]
            e.add_polygon(TrimESCPoints,layer=layer)
            e.add_port("o1", center=(0,TrimWd/2), width=TrimWd, orientation=180,layer=layer)
            e.add_port("o2", center=(TrimEscLn*np.sqrt(1-(TrimEscDistance/TrimEscLn)**2),-TrimEscLn*TrimEscDistance/TrimEscLn+TrimWd/2), width=TrimWd,orientation=0,layer=layer)
        elif Type=="R":
            TrimPoints=[(0,0),(0,TrimWd),(TrimLn,TrimWd+(TaperWd-TipWd)/2),(TrimLn,TrimWd+TipWd+(TaperWd-TipWd)/2),(TrimLn,TrimWd+TrimAddWd+(1+TrimAddLn/TrimLn)*(TaperWd-TipWd)/2),(TrimLn+TrimAddLn,TrimWd+TrimAddWd+(1+TrimAddLn/TrimLn)*(TaperWd-TipWd)/2),(TrimLn+TrimAddLn,TrimWd+(1+TrimAddLn/TrimLn)*(TaperWd-TipWd)/2),(TrimLn+TrimAddLn,(1+TrimAddLn/TrimLn)*(TaperWd-TipWd)/2),(TrimLn,(TaperWd-TipWd)/2)]
            d.add_polygon(TrimPoints,layer=layer)
            d.add_port("o3", center=(TrimLn,TrimWd+(TaperWd-TipWd)/2+TipWd/2), width=TipWd, orientation=0,layer=layer)
            d.add_port("o2", center=(0,TrimWd+TaperWd/2), width=TaperWd,orientation=180,layer=layer) #Taper導波路とport接続するため、portの座標をあえてずらす。
            d.add_port("o1", center=(0,TrimWd/2), width=TrimWd,orientation=180,layer=layer)
            TrimESCPoints=[(0,0), (0,TrimWd),(TrimEscLn*np.sqrt(1-(TrimEscDistance/TrimEscLn)**2),TrimWd+TrimEscLn*TrimEscDistance/TrimEscLn),(TrimEscLn*np.sqrt(1-(TrimEscDistance/TrimEscLn)**2),TrimEscLn*TrimEscDistance/TrimEscLn)]
            e.add_polygon(TrimESCPoints,layer=layer)
            e.add_port("o1", center=(0,TrimWd/2), width=TrimWd, orientation=180,layer=layer)
            e.add_port("o2", center=(TrimEscLn*np.sqrt(1-(TrimEscDistance/TrimEscLn)**2),TrimEscLn*TrimEscDistance/TrimEscLn+TrimWd/2), width=TrimWd,orientation=0,layer=layer)
        
        #メインのInPWG1stのコンポーネント
        c=gf.Component()
        
        #非マンハッタン接続のためcreate_vinstを用いる（仮想インスタンスとのこと）
        c1 = c.create_vinst(d)
        c2 = c.create_vinst(e)
        if Type=="L":
            c2.connect(port="o2", other=c1.ports["o3"], allow_width_mismatch=False) #接続の順番に注意 otherに記載が「主」になる
            c.add_ports(c1.ports,prefix="Trim-L-")
            c.add_ports(c2.ports,prefix="TrimESC-L-")
        elif Type=="R":
            c2.connect(port="o2", other=c1.ports["o1"], allow_width_mismatch=False) #接続の順番に注意 otherに記載が「主」になる
            
            c.add_ports(c1.ports,prefix="Trim-R-")
            c.add_ports(c2.ports,prefix="TrimESC-R-")
        
        #c.pprint_ports() #port定義を表示
        return c
   
    @gf.cell
    def pViaA(width,length,spacer,layer):
        c=gf.Component()
        d=gf.Component()
        pVIApoints=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(pVIApoints,layer=layer)
        d.add_port("o1", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("o2", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("e1", center=(length/2,width+spacer), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0-spacer), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="pVia-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def nViaA(width,length,spacer,layer):
        c=gf.Component()
        d=gf.Component()
        nVIApoints=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(nVIApoints,layer=layer)
        d.add_port("o1", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("o2", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("e1", center=(length/2,width+spacer), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0-spacer), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="nVia-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def pMetalA(width,length,spacer,layer):
        c=gf.Component()
        d=gf.Component()
        pVIApoints=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(pVIApoints,layer=layer)
        d.add_port("o1", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("o2", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("e1", center=(length/2,width+spacer), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0-spacer), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="pMetal-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def nMetalA(width,length,spacer,layer):
        c=gf.Component()
        d=gf.Component()
        nVIApoints=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(nVIApoints,layer=layer)
        d.add_port("o1", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("o2", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("e1", center=(length/2,width+spacer), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0-spacer), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="nMetal-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def nPad1(width,length,spacer,layer):
        c=gf.Component()
        d=gf.Component()
        nPad1points=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(nPad1points,layer=layer)
        d.add_port("e3", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("e4", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("e1", center=(length/2,width+spacer), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0-spacer*0), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="nPad1-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def pPad1(width,length,spacer,layer):
        c=gf.Component()
        d=gf.Component()
        pPad1points=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(pPad1points,layer=layer)
        d.add_port("e3", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("e4", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("e1", center=(length/2,width+spacer*0), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0-spacer), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="pPad1-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def nPad2(width,length,layer):
        c=gf.Component()
        d=gf.Component()
        nPad1points=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(nPad1points,layer=layer)
        d.add_port("e3", center=(0,width/2), width=width, orientation=180,layer=layer,port_type="electrical")
        d.add_port("e4", center=(length,width/2), width=width,orientation=0,layer=layer,port_type="electrical")
        d.add_port("e1", center=(length/2,width), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="nPad2-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def pPad2(width,length,layer):
        c=gf.Component()
        d=gf.Component()
        pPad1points=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(pPad1points,layer=layer)
        d.add_port("e3", center=(0,width/2), width=width, orientation=180,layer=layer,port_type="electrical")
        d.add_port("e4", center=(length,width/2), width=width,orientation=0,layer=layer,port_type="electrical")
        d.add_port("e1", center=(length/2,width), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2,0), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="pPad2-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def nPadVia(width,length,spacer,layer,shift=0):
        c=gf.Component()
        d=gf.Component()
        nPad1points=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(nPad1points,layer=layer)
        d.add_port("o1", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("o2", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("e1", center=(length/2-shift,width+spacer), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2-shift*0,0-spacer*0), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="nPadVia-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def pPadVia(width,length,spacer,layer,shift=0):
        c=gf.Component()
        d=gf.Component()
        pPad1points=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(pPad1points,layer=layer)
        d.add_port("o1", center=(0,width/2), width=width, orientation=180,layer=layer)
        d.add_port("o2", center=(length,width/2), width=width,orientation=0,layer=layer)
        d.add_port("e1", center=(length/2-shift*0,width+spacer*0), width=length, orientation=90,layer=layer,port_type="electrical")
        d.add_port("e2", center=(length/2-shift,0-spacer), width=length,orientation=270,layer=layer,port_type="electrical")
        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="pPadVia-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell
    def PIC(width,length,layer):
        c=gf.Component()
        d=gf.Component()
        PICpoints=[(0,0),(0,width),(length,width),(length,0)]
        d.add_polygon(PICpoints,layer=layer)
        d.add_port("o1", center=(0,127*2), width=1, orientation=0,layer=layer)
        d.add_port("o2", center=(0,127*3), width=1, orientation=0,layer=layer)
        d.add_port("o3", center=(length,width-127*2), width=1,orientation=180,layer=layer)
        d.add_port("o4", center=(length,width-127*3), width=1,orientation=180,layer=layer)

        c1 = c.add_ref(d)#任意のレイヤにしたい場合はrectangle定義必要？
        c.add_ports(c1.ports,prefix="PICIO-")
        #c.pprint_ports() #port定義を表示
        return c
    @gf.cell #taper導波路部左側の定義ファイル。曲げ対応予定。現在ストレートのみ可。
    def SiOxWG_Tip(Type,TipLn,cross_section) : 
        c=gf.Component()
        #非マンハッタン接続のためcreate_vinstを用いる（仮想インスタンスとのこと）
        c1 = c.create_vinst(gf.components.straight_all_angle(length=0,cross_section=cross_section))
        c2 = c.create_vinst(gf.components.straight_all_angle(length=TipLn,cross_section=cross_section))
        c3 = c.create_vinst(gf.components.straight_all_angle(length=0,cross_section=cross_section))
        
        if Type=="L":
            c2.connect(port="o2", other=c1.ports["o1"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c3.connect(port="o2", other=c2.ports["o1"], allow_width_mismatch=False,allow_layer_mismatch=True)
            
            c.add_ports(c1.ports,prefix="TipL-root-")
            c.add_ports(c2.ports,prefix="Tip-L-")
        elif Type=="R":
            c2.connect(port="o1", other=c1.ports["o2"], allow_width_mismatch=False,allow_layer_mismatch=True)
            c3.connect(port="o1", other=c2.ports["o2"], allow_width_mismatch=False,allow_layer_mismatch=True)
            
            c.add_ports(c1.ports,prefix="TipR-root-")
            c.add_ports(c2.ports,prefix="Tip-R-")
        #c.pprint_ports() #port定義を表示
        return c

class CrossSections:
    def XS_SiOx(SiOxCoreWidth,SiOxEtchWidth,radius,SiOxWG_Layer,SiOxEtch_Layer):
        #SiOx-WaveGuide
        SiOxS0 = gf.Section(width=SiOxCoreWidth, offset=0, name="core", port_names=("o1","o2"),layer=SiOxWG_Layer) #SiOx-Core WaveGuide
        SiOxS1 = gf.Section(width=SiOxEtchWidth, offset=(SiOxCoreWidth+SiOxEtchWidth)/2, name="etch",layer=SiOxEtch_Layer) #SiOx-Etch Area 
        SiOxS2 = gf.Section(width=SiOxEtchWidth, offset=-(SiOxCoreWidth+SiOxEtchWidth)/2, name="etch",layer=SiOxEtch_Layer) #SiOx-Etch Area
        XS_SiOx = gf.CrossSection(sections=[SiOxS0,SiOxS1,SiOxS2],radius=radius,radius_min=radius)
        return XS_SiOx
    
    def XS_InPWG(Width,radius,InPWG_Layer,InPWG1stEtch_Layer):
        #SiOx-WaveGuide
        InPWG = gf.Section(width=Width, offset=0, name="core", port_names=("o1","o2"),layer=InPWG_Layer) #SiOx-Core WaveGuide
        InPWG1st = gf.Section(width=Width, offset=0, name="1stEtch",layer=InPWG1stEtch_Layer) #SiOx-Core WaveGuide
        XS_InPWG = gf.CrossSection(sections=[InPWG,InPWG1st],radius=radius,radius_min=radius)
        return XS_InPWG

class Devices:
    @gf.cell
    def LDchip_bak01(Parameters,ID): #Parameters変数はリストで定義。
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        c = gf.Component() #キャンパスを定義
        ##cross_sectionの定義が必要の場合はここで定義
        XS_SiOx=CrossSections.XS_SiOx(SiOxCoreWidth=Parameters[ID][Parameters["ParameterName"].index("SiOxCoreWd")],SiOxEtchWidth=Parameters[ID][Parameters["ParameterName"].index("SiOxEtchWd")],radius=Parameters[ID][Parameters["ParameterName"].index("SiOxBendRadius")],SiOxWG_Layer=LAYER.SiOxWG,SiOxEtch_Layer=LAYER.SiOxEtch)
        
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        BH = c.add_ref(BaseParts.BHetch(width=Parameters[ID][Parameters["ParameterName"].index("BHWd")],length=Parameters[ID][Parameters["ParameterName"].index("BHLn")],shift=Parameters[ID][Parameters["ParameterName"].index("StLn")],layer=LAYER.BH)) #キャンパス内にBHを配置
        BHdummy1 = c.add_ref(BaseParts.BHdummy(width=Parameters[ID][Parameters["ParameterName"].index("BHDWdA")],length=Parameters[ID][Parameters["ParameterName"].index("BHDLnA")],spacer=Parameters[ID][Parameters["ParameterName"].index("BHDsp")],layer=LAYER.BHdmyA)) #キャンパス内にBHdummyを配置
        BHdummy2 = c.add_ref(BaseParts.BHdummy(width=Parameters[ID][Parameters["ParameterName"].index("BHDWdA")],length=Parameters[ID][Parameters["ParameterName"].index("BHDLnA")],spacer=Parameters[ID][Parameters["ParameterName"].index("BHDsp")],layer=LAYER.BHdmyA))
        nDpA = c.add_ref(BaseParts.nDpA(width=Parameters[ID][Parameters["ParameterName"].index("nDopeWd")],length=Parameters[ID][Parameters["ParameterName"].index("nDopeLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nDopeSp")],layer=LAYER.nDope)) 
        pDpA = c.add_ref(BaseParts.pDpA(width=Parameters[ID][Parameters["ParameterName"].index("pDopeWd")],length=Parameters[ID][Parameters["ParameterName"].index("pDopeLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pDopeSp")],layer=LAYER.pDope))
        InGaAs1 = c.add_ref(BaseParts.InGaAsEtch(width=Parameters[ID][Parameters["ParameterName"].index("pConWd")],length=Parameters[ID][Parameters["ParameterName"].index("pConLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pConSp")],layer=LAYER.InGaAs)) 
        InGaAs2 = c.add_ref(BaseParts.InGaAsEtch(width=Parameters[ID][Parameters["ParameterName"].index("pConWd")],length=Parameters[ID][Parameters["ParameterName"].index("pConLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pConSp")],layer=LAYER.InGaAs)) 
        
        Device1 = c.add_ref(BaseParts.Device(width=Parameters[ID][Parameters["ParameterName"].index("DevWd")],length=Parameters[ID][Parameters["ParameterName"].index("DevLn")],layer=LAYER.InPWG1st))
        Device2 = c.add_ref(BaseParts.Device(width=Parameters[ID][Parameters["ParameterName"].index("DevWd")],length=Parameters[ID][Parameters["ParameterName"].index("DevLn")],layer=LAYER.InPWG))
        InPWG_Lbend=c.create_vinst(BaseParts.InPWG_Lbend(StWd=Parameters[ID][Parameters["ParameterName"].index("StWd")],StLn=Parameters[ID][Parameters["ParameterName"].index("St1Ln")],TaperWd=Parameters[ID][Parameters["ParameterName"].index("Taper2Wd")],TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],radius=Parameters[ID][Parameters["ParameterName"].index("SiOxBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgLAngle")],layer=LAYER.InPWG)) 
        InPWG_Rbend=c.create_vinst(BaseParts.InPWG_Rbend(StWd=Parameters[ID][Parameters["ParameterName"].index("StWd")],StLn=Parameters[ID][Parameters["ParameterName"].index("St1Ln")],TaperWd=Parameters[ID][Parameters["ParameterName"].index("Taper2Wd")],TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],radius=Parameters[ID][Parameters["ParameterName"].index("SiOxBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgRAngle")],layer=LAYER.InPWG)) 
        InPWG1stLbend = c.create_vinst(BaseParts.InPWG1st_Lbend(StWd=Parameters[ID][Parameters["ParameterName"].index("StWd")],StLn=Parameters[ID][Parameters["ParameterName"].index("St1Ln")],TaperWd=Parameters[ID][Parameters["ParameterName"].index("Taper2Wd")],TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipDLn=Parameters[ID][Parameters["ParameterName"].index("TipDLn")],radius=Parameters[ID][Parameters["ParameterName"].index("SiOxBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgLAngle")],layer=LAYER.InPWG1st))
        InPWG1stRbend = c.create_vinst(BaseParts.InPWG1st_Rbend(StWd=Parameters[ID][Parameters["ParameterName"].index("StWd")],StLn=Parameters[ID][Parameters["ParameterName"].index("St1Ln")],TaperWd=Parameters[ID][Parameters["ParameterName"].index("Taper2Wd")],TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipDLn=Parameters[ID][Parameters["ParameterName"].index("TipDLn")],radius=Parameters[ID][Parameters["ParameterName"].index("SiOxBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgRAngle")],layer=LAYER.InPWG1st))
        InPWG2ndL = c.create_vinst(BaseParts.InPWG2ndL(TaperWd=Parameters[ID][Parameters["ParameterName"].index("TaperWd")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],TrimAddWd=Parameters[ID][Parameters["ParameterName"].index("TrimAddWd")],TrimAddLn=Parameters[ID][Parameters["ParameterName"].index("TrimAddLn")],TrimWd=Parameters[ID][Parameters["ParameterName"].index("TrimWd")],TrimLn=Parameters[ID][Parameters["ParameterName"].index("TrimLn")],layer=LAYER.InPWG2nd))
        InPWG2ndR = c.create_vinst(BaseParts.InPWG2ndR(TaperWd=Parameters[ID][Parameters["ParameterName"].index("TaperWd")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],TrimAddWd=Parameters[ID][Parameters["ParameterName"].index("TrimAddWd")],TrimAddLn=Parameters[ID][Parameters["ParameterName"].index("TrimAddLn")],TrimWd=Parameters[ID][Parameters["ParameterName"].index("TrimWd")],TrimLn=Parameters[ID][Parameters["ParameterName"].index("TrimLn")],layer=LAYER.InPWG2nd))
        nViaA = c.add_ref(BaseParts.nViaA(width=Parameters[ID][Parameters["ParameterName"].index("nViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nViaSp")],layer=LAYER.nVia)) 
        pViaA = c.add_ref(BaseParts.pViaA(width=Parameters[ID][Parameters["ParameterName"].index("pViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pViaSp")],layer=LAYER.pVia)) 
        nMetalA = c.add_ref(BaseParts.nMetalA(width=Parameters[ID][Parameters["ParameterName"].index("nMetalWd")],length=Parameters[ID][Parameters["ParameterName"].index("nMetalLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nMetalSp")],layer=LAYER.nMetal))
        pMetalA = c.add_ref(BaseParts.pMetalA(width=Parameters[ID][Parameters["ParameterName"].index("pMetalWd")],length=Parameters[ID][Parameters["ParameterName"].index("pMetalLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pMetalSp")],layer=LAYER.pMetal))
        nPad1 = c.add_ref(BaseParts.nPad1(width=Parameters[ID][Parameters["ParameterName"].index("nPad1Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad1Ln")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadSp")],layer=LAYER.PadMetal))
        pPad1 = c.add_ref(BaseParts.pPad1(width=Parameters[ID][Parameters["ParameterName"].index("pPad1Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad1Ln")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadSp")],layer=LAYER.PadMetal))
        nPad2 = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad2Ln")],layer=LAYER.PadMetal))
        pPad2 = c.add_ref(BaseParts.pPad2(width=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad2Ln")],layer=LAYER.PadMetal))
        nPadVia = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("nPadViaShift")],layer=LAYER.PadVia))
        pPadVia = c.add_ref(BaseParts.pPadVia(width=Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("pPadViaShift")],layer=LAYER.PadVia))
        
        AbsSideType=Parameters[ID][Parameters["ParameterName"].index("AbsSideType")]
        if AbsSideType==1:#LeftSide
            InGaAsEtch_Lbend=c.create_vinst(BaseParts.InGaAsEtch_Lbend(width=10,TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipDLn=Parameters[ID][Parameters["ParameterName"].index("TipDLn")],radius=Parameters[ID][Parameters["ParameterName"].index("SiOxBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgLAngle")],layer=LAYER.InGaAs))
            SiOxWG_R = c.create_vinst(BaseParts.SiOxWG_Rbend(StLn=0,TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgRAngle")],cross_section=XS_SiOx)) 
        elif AbsSideType==2:#RightSide
            InGaAsEtch_Rbend=c.create_vinst(BaseParts.InGaAsEtch_Rbend(width=10,TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipDLn=Parameters[ID][Parameters["ParameterName"].index("TipDLn")],radius=Parameters[ID][Parameters["ParameterName"].index("SiOxBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgRAngle")],layer=LAYER.InGaAs))
            SiOxWG_L = c.create_vinst(BaseParts.SiOxWG_Lbend(StLn=0,TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgLAngle")],cross_section=XS_SiOx))  #CORE MBRN:sideL
        elif AbsSideType==0:#No Absorption Region
            SiOxWG_R = c.create_vinst(BaseParts.SiOxWG_Rbend(StLn=0,TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgRAngle")],cross_section=XS_SiOx)) 
            SiOxWG_L = c.create_vinst(BaseParts.SiOxWG_Lbend(StLn=0,TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgLAngle")],cross_section=XS_SiOx))  #CORE MBRN:sideL
        else:
            pass
        
        
        BH.move((-Parameters[ID][Parameters["ParameterName"].index("BHLn")]/2,-Parameters[ID][Parameters["ParameterName"].index("BHWd")]/2)) #Deviceを中央に
        
        ##各コンポーネント同士を接続
        BHdummy1.connect(port="BHdummy-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        BHdummy2.connect(port="BHdummy-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nDpA.connect(port="nDpA-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pDpA.connect(port="pDpA-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        InGaAs1.connect(port="InGaAs-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        InGaAs2.connect(port="InGaAs-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        Device1.connect(port="Device-e4", other=BH.ports["BH-e3"], allow_width_mismatch=True,allow_layer_mismatch=True)
        Device2.connect(port="Device-e4", other=BH.ports["BH-e3"], allow_width_mismatch=True,allow_layer_mismatch=True)
        InPWG_Lbend.connect(port="St-L-o2", other=BH.ports["BH-o1"], allow_width_mismatch=True, allow_layer_mismatch=True)
        InPWG_Rbend.connect(port="St-R-o1", other=BH.ports["BH-o2"], allow_width_mismatch=True, allow_layer_mismatch=True)
        InPWG1stLbend.connect(port="St-L-o2", other=BH.ports["BH-o1"], allow_width_mismatch=True, allow_layer_mismatch=True)
        InPWG1stRbend.connect(port="St-R-o1", other=BH.ports["BH-o2"], allow_width_mismatch=True, allow_layer_mismatch=True)
        InPWG2ndL.connect(port="Trim-L-o2", other=InPWG1stLbend.ports["BendWG-L-o1"], allow_width_mismatch=True, allow_layer_mismatch=True)
        InPWG2ndR.connect(port="Trim-R-o2", other=InPWG1stRbend.ports["BendWG-R-o2"], allow_width_mismatch=True, allow_layer_mismatch=True)
        nViaA.connect(port="nVia-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pViaA.connect(port="pVia-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nMetalA.connect(port="nMetal-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pMetalA.connect(port="pMetal-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nPad1.connect(port="nPad1-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pPad1.connect(port="pPad1-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        # nPadVia.connect(port="nPadVia-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        # pPadVia.connect(port="pPadVia-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        
        if AbsSideType==1:#LeftSide
            InGaAsEtch_Lbend.connect(port="Bend-L-o2",other=InPWG_Lbend.ports["Taper-L-o1"],allow_width_mismatch=True,allow_layer_mismatch=True)
            SiOxWG_R.connect(port="TipR-root-o1", other=BH.ports["BH-o4"], allow_width_mismatch=True,allow_layer_mismatch=True)
        elif AbsSideType==2:#RightSide
            InGaAsEtch_Rbend.connect(port="Bend-R-o1",other=InPWG_Rbend.ports["Taper-R-o2"],allow_width_mismatch=True,allow_layer_mismatch=True)
            SiOxWG_L.connect(port="TipL-root-o2", other=BH.ports["BH-o3"], allow_width_mismatch=True,allow_layer_mismatch=True)
        elif AbsSideType==0:#No Absorption Region
            SiOxWG_L.connect(port="TipL-root-o2", other=InPWG_Lbend.ports["BH-o3"], allow_width_mismatch=True,allow_layer_mismatch=True)
            SiOxWG_R.connect(port="TipR-root-o1", other=BH.ports["BH-o4"], allow_width_mismatch=True,allow_layer_mismatch=True)
        else:
            pass
        
            
        
        PadPortsWidth=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]
        
        if Parameters[ID][Parameters["ParameterName"].index("PadType")]==0:
            
            if Parameters[ID][Parameters["ParameterName"].index("ProbeType")]==1: # for GSSG
                GnPad = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad2Ln")],layer=LAYER.PadMetal))
                GpPad = c.add_ref(BaseParts.pPad2(width=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad2Ln")],layer=LAYER.PadMetal))
                GnPadVia = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("nPadViaShift")],layer=LAYER.PadVia))
                GpPadVia = c.add_ref(BaseParts.pPadVia(width=Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("pPadViaShift")],layer=LAYER.PadVia))
                
                PadSpacer=Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]/2
                PadPortsWidth=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]
                
                GnPad_ports = [
                gf.Port(f"GnPad_{i}", center=[0,-(Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(i+0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2)],width=PadPortsWidth,orientation=270,port_type="electrical",layer=LAYER.PadMetal) 
                for i in range(2)
                ]
                GpPad_ports = [
                gf.Port(f"GpPad_{i}", center=[0,Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(i+0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2],width=PadPortsWidth,orientation=90,port_type="electrical",layer=LAYER.PadMetal) 
                for i in range(2)
                ]
                
                nPad2.connect(port="nPad2-e1", other=GnPad_ports[0])
                GnPad.connect(port="nPad2-e1", other=GnPad_ports[1])
                pPad2.connect(port="pPad2-e2", other=GpPad_ports[0])    
                GpPad.connect(port="pPad2-e2", other=GpPad_ports[1])
                
                gf.routing.route_quad(c,port2=nPad2.ports["nPad2-e1"],port1=nPad1.ports["nPad1-e2"],width1=None,width2=None,layer=LAYER.PadMetal)
                gf.routing.route_quad(c,port2=pPad2.ports["pPad2-e2"],port1=pPad1.ports["pPad1-e1"],width1=None,width2=None,layer=LAYER.PadMetal)
                
                GnPadVia.move((GnPad.center[0]-Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")]/2,GnPad.center[1]-Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")]/2))
                GpPadVia.move((GpPad.center[0]-Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")]/2,GpPad.center[1]-Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")]/2))
                c.add_ports(GnPad_ports)
                c.add_ports(GpPad_ports)
            else:
                GnPad_ports = [
                gf.Port("GnPad_0", center=[0,-(Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2)],width=PadPortsWidth,orientation=270,port_type="electrical",layer=LAYER.PadMetal),
                ]
                GpPad_ports = [
                gf.Port("GpPad_0", center=[0,Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2],width=PadPortsWidth,orientation=90,port_type="electrical",layer=LAYER.PadMetal),
                ]
                nPad2.connect(port="nPad2-e1", other=GnPad_ports[0])
                pPad2.connect(port="pPad2-e2", other=GpPad_ports[0])
                # nPad2.connect(port="nPad2-e1", other=nPad1.ports["nPad1-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
                # pPad2.connect(port="pPad2-e2", other=pPad1.ports["pPad1-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
                gf.routing.route_quad(c,port2=nPad2.ports["nPad2-e1"],port1=nPad1.ports["nPad1-e2"],width1=None,width2=None,layer=LAYER.PadMetal)
                gf.routing.route_quad(c,port2=pPad2.ports["pPad2-e2"],port1=pPad1.ports["pPad1-e1"],width1=None,width2=None,layer=LAYER.PadMetal)       
                
        elif Parameters[ID][Parameters["ParameterName"].index("PadType")]==1:
            nPad3 = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad2Ln")],layer=LAYER.PadMetal))
            pPad3 = c.add_ref(BaseParts.pPad2(width=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad2Ln")],layer=LAYER.PadMetal))
            nPadVia2 = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("nPadViaShift")],layer=LAYER.PadVia))
            pPadVia2 = c.add_ref(BaseParts.pPadVia(width=Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("pPadViaShift")],layer=LAYER.PadVia))
            
            PadSpacer=Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]/2
            PadPortsWidth=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]
            dx = (Parameters[ID][Parameters["ParameterName"].index("BHLn")]/2+120)
            
            if Parameters[ID][Parameters["ParameterName"].index("ProbeType")]==1: # for GSSG
                GnPadL = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad2Ln")],layer=LAYER.PadMetal))
                GpPadL = c.add_ref(BaseParts.pPad2(width=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad2Ln")],layer=LAYER.PadMetal))
                GnPadViaL = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("nPadViaShift")],layer=LAYER.PadVia))
                GpPadViaL = c.add_ref(BaseParts.pPadVia(width=Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("pPadViaShift")],layer=LAYER.PadVia))
                GnPadR = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad2Ln")],layer=LAYER.PadMetal))
                GpPadR = c.add_ref(BaseParts.pPad2(width=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad2Ln")],layer=LAYER.PadMetal))
                GnPadViaR = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("nPadViaShift")],layer=LAYER.PadVia))
                GpPadViaR = c.add_ref(BaseParts.pPadVia(width=Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("pPadViaShift")],layer=LAYER.PadVia))
                
                GnPadR_ports = [
                gf.Port(f"GnPadR_{i}", center=[dx,-(Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(i+0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2)],width=PadPortsWidth,orientation=270,port_type="electrical",layer=LAYER.PadMetal) 
                for i in range(2)
                ]
                GpPadR_ports = [
                gf.Port(f"GpPadR_{i}", center=[dx,Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(i+0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2],width=PadPortsWidth,orientation=90,port_type="electrical",layer=LAYER.PadMetal) 
                for i in range(2)
                ]
                GnPadL_ports = [
                gf.Port(f"GnPadL_{i}", center=[-dx,-(Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(i+0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2)],width=PadPortsWidth,orientation=270,port_type="electrical",layer=LAYER.PadMetal) 
                for i in range(2)
                ]
                GpPadL_ports = [
                gf.Port(f"GpPadL_{i}", center=[-dx,Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(i+0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2],width=PadPortsWidth,orientation=90,port_type="electrical",layer=LAYER.PadMetal) 
                for i in range(2)
                ]
                
                
                
                nPad2.connect(port="nPad2-e1", other=GnPadR_ports[0])
                pPad2.connect(port="pPad2-e2", other=GpPadR_ports[0])
                GnPadR.connect(port="nPad2-e1", other=GnPadR_ports[1])
                GpPadR.connect(port="pPad2-e2", other=GpPadR_ports[1])
                nPad3.connect(port="nPad2-e1", other=GnPadL_ports[0])
                pPad3.connect(port="pPad2-e2", other=GpPadL_ports[0])
                GnPadL.connect(port="nPad2-e1", other=GnPadL_ports[1])
                GpPadL.connect(port="pPad2-e2", other=GpPadL_ports[1])
                
                GnPadViaL.move((GnPadL.center[0]-Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")]/2,GnPadL.center[1]-Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")]/2))
                GnPadViaR.move((GnPadR.center[0]-Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")]/2,GnPadR.center[1]-Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")]/2))
                GpPadViaL.move((GpPadL.center[0]-Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")]/2,GpPadL.center[1]-Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")]/2))
                GpPadViaR.move((GpPadR.center[0]-Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")]/2,GpPadR.center[1]-Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")]/2))
               
                
            else:
                pPadR_ports = [
                    gf.Port(f"pPad_{i}", center=[dx,PadSpacer],width=PadPortsWidth,orientation=90*i,port_type="electrical",layer=LAYER.PadMetal) 
                    for i in range(4)
                    ]
                pPadL_ports = [
                    gf.Port(f"pPad_{i}", center=[-dx,PadSpacer],width=PadPortsWidth,orientation=90*i,port_type="electrical",layer=LAYER.PadMetal) 
                    for i in range(4)
                    ]
                
                nPadR_ports = [
                    gf.Port(f"nPad_{i}", center=[dx,-PadSpacer],width=PadPortsWidth,orientation=90*i,port_type="electrical",layer=LAYER.PadMetal)
                    for i in range(4)
                    ]
                nPadL_ports = [
                    gf.Port(f"nPad_{i}", center=[-dx,-PadSpacer],width=PadPortsWidth,orientation=90*i,port_type="electrical",layer=LAYER.PadMetal)
                    for i in range(4)
                    ]
                
                
                
                pPad2.connect(port="pPad2-e3", other=pPadR_ports[0])
                nPad2.connect(port="nPad2-e3", other=nPadR_ports[0])
                pPad3.connect(port="pPad2-e1", other=pPadL_ports[2])
                nPad3.connect(port="nPad2-e1", other=nPadL_ports[2])
            
            gf.routing.route_quad(c,port2=pPad2.ports["pPad2-e3"],port1=pPad1.ports["pPad1-e4"],width1=None,width2=None,layer=LAYER.PadMetal)
            gf.routing.route_quad(c,port2=nPad2.ports["nPad2-e3"],port1=nPad1.ports["nPad1-e4"],width1=None,width2=None,layer=LAYER.PadMetal)
            gf.routing.route_quad(c,port2=pPad3.ports["pPad2-e4"],port1=pPad1.ports["pPad1-e3"],width1=None,width2=None,layer=LAYER.PadMetal)
            gf.routing.route_quad(c,port2=nPad3.ports["nPad2-e4"],port1=nPad1.ports["nPad1-e3"],width1=None,width2=None,layer=LAYER.PadMetal)
                    
            nPadVia2.move((nPad3.center[0]-Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")]/2,nPad3.center[1]-Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")]/2))
            pPadVia2.move((pPad3.center[0]-Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")]/2,pPad3.center[1]-Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")]/2))
        
            
            
        
        nPadVia.move((nPad2.center[0]-Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")]/2,nPad2.center[1]-Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")]/2))
        pPadVia.move((pPad2.center[0]-Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")]/2,pPad2.center[1]-Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")]/2))
        
        #c.add_ports(SiOxWG_L.ports,prefix="Dev_L-")
        #c.add_ports(SiOxWG_R.ports,prefix="Dev_R-")
        #c.add_ports(nPad2.ports)
        #c.add_ports(pPad2.ports)
        
        #c.pprint_ports()
        #c.draw_ports()
        
        return c

    @gf.cell
    def LDchip(Parameters,ID): #Parameters変数はリストで定義。
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        c = gf.Component() #キャンパスを定義
        ##cross_sectionの定義が必要の場合はここで定義
        XS_SiOx=CrossSections.XS_SiOx(SiOxCoreWidth=Parameters[ID][Parameters["ParameterName"].index("SiOxCoreWd")],SiOxEtchWidth=Parameters[ID][Parameters["ParameterName"].index("SiOxEtchWd")],radius=Parameters[ID][Parameters["ParameterName"].index("SiOxBendRadius")],SiOxWG_Layer=LAYER.SiOxWG,SiOxEtch_Layer=LAYER.SiOxEtch)
        
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        BH = c.add_ref(BaseParts.BHetch(width=Parameters[ID][Parameters["ParameterName"].index("BHWd")],length=Parameters[ID][Parameters["ParameterName"].index("BHLn")],shift=0,layer=LAYER.BH)) #キャンパス内にBHを配置
        BHdummy1 = c.add_ref(BaseParts.BHdummy(width=Parameters[ID][Parameters["ParameterName"].index("BHDWdA")],length=Parameters[ID][Parameters["ParameterName"].index("BHDLnA")],spacer=Parameters[ID][Parameters["ParameterName"].index("BHDsp")],layer=LAYER.BHdmyA)) #キャンパス内にBHdummyを配置
        BHdummy2 = c.add_ref(BaseParts.BHdummy(width=Parameters[ID][Parameters["ParameterName"].index("BHDWdA")],length=Parameters[ID][Parameters["ParameterName"].index("BHDLnA")],spacer=Parameters[ID][Parameters["ParameterName"].index("BHDsp")],layer=LAYER.BHdmyA))
        nDpA = c.add_ref(BaseParts.nDpA(width=Parameters[ID][Parameters["ParameterName"].index("nDopeWd")],length=Parameters[ID][Parameters["ParameterName"].index("nDopeLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nDopeSp")],layer=LAYER.nDope)) 
        pDpA = c.add_ref(BaseParts.pDpA(width=Parameters[ID][Parameters["ParameterName"].index("pDopeWd")],length=Parameters[ID][Parameters["ParameterName"].index("pDopeLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pDopeSp")],layer=LAYER.pDope))
        InGaAs1 = c.add_ref(BaseParts.InGaAsEtch(width=Parameters[ID][Parameters["ParameterName"].index("pConWd")],length=Parameters[ID][Parameters["ParameterName"].index("pConLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pConSp")],layer=LAYER.InGaAs)) 
        InGaAs2 = c.add_ref(BaseParts.InGaAsEtch(width=Parameters[ID][Parameters["ParameterName"].index("pConWd")],length=Parameters[ID][Parameters["ParameterName"].index("pConLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pConSp")],layer=LAYER.InGaAs)) 
        
        Device1 = c.add_ref(BaseParts.Device(width=Parameters[ID][Parameters["ParameterName"].index("DevWd")],length=Parameters[ID][Parameters["ParameterName"].index("DevLn")],layer=LAYER.InPWG1st))
        Device2 = c.add_ref(BaseParts.Device(width=Parameters[ID][Parameters["ParameterName"].index("DevWd")],length=Parameters[ID][Parameters["ParameterName"].index("DevLn")],layer=LAYER.InPWG))
        InPWG_Lbend=c.create_vinst(BaseParts.InPWG(Type="L",St1Ln=Parameters[ID][Parameters["ParameterName"].index("St1Ln")],St1Wd=Parameters[ID][Parameters["ParameterName"].index("St1Wd")],TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TaperWd1=Parameters[ID][Parameters["ParameterName"].index("TaperWd1")],TaperWd2=Parameters[ID][Parameters["ParameterName"].index("TaperWd2")],St2Ln=Parameters[ID][Parameters["ParameterName"].index("St2Ln")],St2Wd=Parameters[ID][Parameters["ParameterName"].index("St2Wd")],St3Ln=Parameters[ID][Parameters["ParameterName"].index("St3Ln")],St3Wd=Parameters[ID][Parameters["ParameterName"].index("St3Wd")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],radius=Parameters[ID][Parameters["ParameterName"].index("WgBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgLAngle")],layer=LAYER.InPWG)) 
        InPWG_Rbend=c.create_vinst(BaseParts.InPWG(Type="R",St1Ln=Parameters[ID][Parameters["ParameterName"].index("St1Ln")],St1Wd=Parameters[ID][Parameters["ParameterName"].index("St1Wd")],TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TaperWd1=Parameters[ID][Parameters["ParameterName"].index("TaperWd1")],TaperWd2=Parameters[ID][Parameters["ParameterName"].index("TaperWd2")],St2Ln=Parameters[ID][Parameters["ParameterName"].index("St2Ln")],St2Wd=Parameters[ID][Parameters["ParameterName"].index("St2Wd")],St3Ln=Parameters[ID][Parameters["ParameterName"].index("St3Ln")],St3Wd=Parameters[ID][Parameters["ParameterName"].index("St3Wd")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],radius=Parameters[ID][Parameters["ParameterName"].index("WgBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgRAngle")],layer=LAYER.InPWG)) 
        InPWG1stLbend=c.create_vinst(BaseParts.InPWG1st(Type="L",St1Ln=Parameters[ID][Parameters["ParameterName"].index("St1Ln")],St1Wd=Parameters[ID][Parameters["ParameterName"].index("St1Wd")],TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TaperWd1=Parameters[ID][Parameters["ParameterName"].index("TaperWd1")],TaperWd2=Parameters[ID][Parameters["ParameterName"].index("TaperWd2")],St2Ln=Parameters[ID][Parameters["ParameterName"].index("St2Ln")],St2Wd=Parameters[ID][Parameters["ParameterName"].index("St2Wd")],St3Ln=Parameters[ID][Parameters["ParameterName"].index("St3Ln")],St3Wd=Parameters[ID][Parameters["ParameterName"].index("St3Wd")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipDLn=Parameters[ID][Parameters["ParameterName"].index("TipDLn")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],radius=Parameters[ID][Parameters["ParameterName"].index("WgBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgLAngle")],layer=LAYER.InPWG1st)) 
        InPWG1stRbend=c.create_vinst(BaseParts.InPWG1st(Type="R",St1Ln=Parameters[ID][Parameters["ParameterName"].index("St1Ln")],St1Wd=Parameters[ID][Parameters["ParameterName"].index("St1Wd")],TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TaperWd1=Parameters[ID][Parameters["ParameterName"].index("TaperWd1")],TaperWd2=Parameters[ID][Parameters["ParameterName"].index("TaperWd2")],St2Ln=Parameters[ID][Parameters["ParameterName"].index("St2Ln")],St2Wd=Parameters[ID][Parameters["ParameterName"].index("St2Wd")],St3Ln=Parameters[ID][Parameters["ParameterName"].index("St3Ln")],St3Wd=Parameters[ID][Parameters["ParameterName"].index("St3Wd")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipDLn=Parameters[ID][Parameters["ParameterName"].index("TipDLn")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],radius=Parameters[ID][Parameters["ParameterName"].index("WgBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgRAngle")],layer=LAYER.InPWG1st)) 
        InPWG2ndL = c.create_vinst(BaseParts.InPWG2nd(Type="L",TrimLn=Parameters[ID][Parameters["ParameterName"].index("TrimLn")],TrimWd=Parameters[ID][Parameters["ParameterName"].index("TrimWd")],TrimAddLn=Parameters[ID][Parameters["ParameterName"].index("TrimAddLn")],TrimAddWd=Parameters[ID][Parameters["ParameterName"].index("TrimAddWd")],TaperWd=Parameters[ID][Parameters["ParameterName"].index("TaperWd2")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],layer=LAYER.InPWG2nd))
        InPWG2ndR = c.create_vinst(BaseParts.InPWG2nd(Type="R",TrimLn=Parameters[ID][Parameters["ParameterName"].index("TrimLn")],TrimWd=Parameters[ID][Parameters["ParameterName"].index("TrimWd")],TrimAddLn=Parameters[ID][Parameters["ParameterName"].index("TrimAddLn")],TrimAddWd=Parameters[ID][Parameters["ParameterName"].index("TrimAddWd")],TaperWd=Parameters[ID][Parameters["ParameterName"].index("TaperWd2")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],layer=LAYER.InPWG2nd))
        
        nViaA = c.add_ref(BaseParts.nViaA(width=Parameters[ID][Parameters["ParameterName"].index("nViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nViaSp")],layer=LAYER.nVia)) 
        pViaA = c.add_ref(BaseParts.pViaA(width=Parameters[ID][Parameters["ParameterName"].index("pViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pViaSp")],layer=LAYER.pVia)) 
        nMetalA = c.add_ref(BaseParts.nMetalA(width=Parameters[ID][Parameters["ParameterName"].index("nMetalWd")],length=Parameters[ID][Parameters["ParameterName"].index("nMetalLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nMetalSp")],layer=LAYER.nMetal))
        pMetalA = c.add_ref(BaseParts.pMetalA(width=Parameters[ID][Parameters["ParameterName"].index("pMetalWd")],length=Parameters[ID][Parameters["ParameterName"].index("pMetalLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pMetalSp")],layer=LAYER.pMetal))
        nPad1 = c.add_ref(BaseParts.nPad1(width=Parameters[ID][Parameters["ParameterName"].index("nPad1Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad1Ln")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadSp")],layer=LAYER.PadMetal))
        pPad1 = c.add_ref(BaseParts.pPad1(width=Parameters[ID][Parameters["ParameterName"].index("pPad1Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad1Ln")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadSp")],layer=LAYER.PadMetal))
        nPad2 = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad2Ln")],layer=LAYER.PadMetal))
        pPad2 = c.add_ref(BaseParts.pPad2(width=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad2Ln")],layer=LAYER.PadMetal))
        nPad2Via = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("nPadViaShift")],layer=LAYER.PadVia))
        pPad2Via = c.add_ref(BaseParts.pPadVia(width=Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("pPadViaShift")],layer=LAYER.PadVia))
        
        AbsSideType=Parameters[ID][Parameters["ParameterName"].index("AbsSideType")]
        if AbsSideType==1:#LeftSide
            InGaAsEtch_Lbend=c.create_vinst(BaseParts.InGaAsEtch_Lbend(width=10,TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipDLn=Parameters[ID][Parameters["ParameterName"].index("TipDLn")],radius=Parameters[ID][Parameters["ParameterName"].index("SiOxBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgLAngle")],layer=LAYER.InGaAs))
            SiOxWG_R = c.create_vinst(BaseParts.SiOxWG_Tip(Type="R",TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],cross_section=XS_SiOx)) 
        elif AbsSideType==2:#RightSide
            InGaAsEtch_Rbend=c.create_vinst(BaseParts.InGaAsEtch_Rbend(width=10,TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipDLn=Parameters[ID][Parameters["ParameterName"].index("TipDLn")],radius=Parameters[ID][Parameters["ParameterName"].index("SiOxBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgRAngle")],layer=LAYER.InGaAs))
            SiOxWG_L = c.create_vinst(BaseParts.SiOxWG_Tip(Type="L",TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],cross_section=XS_SiOx)) 
        elif AbsSideType==0:#No Absorption Region
            SiOxWG_R = c.create_vinst(BaseParts.SiOxWG_Tip(Type="R",TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],cross_section=XS_SiOx))  
            SiOxWG_L = c.create_vinst(BaseParts.SiOxWG_Tip(Type="L",TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],cross_section=XS_SiOx)) 
        else:
            pass
        
        
        BH.move((-Parameters[ID][Parameters["ParameterName"].index("BHLn")]/2,-Parameters[ID][Parameters["ParameterName"].index("BHWd")]/2)) #Deviceを中央に
        
        ##各コンポーネント同士を接続
        BHdummy1.connect(port="BHdummy-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        BHdummy2.connect(port="BHdummy-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nDpA.connect(port="nDpA-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pDpA.connect(port="pDpA-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        InGaAs1.connect(port="InGaAs-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        InGaAs2.connect(port="InGaAs-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        Device1.connect(port="Device-e4", other=BH.ports["BH-e3"], allow_width_mismatch=True,allow_layer_mismatch=True)
        Device2.connect(port="Device-e4", other=BH.ports["BH-e3"], allow_width_mismatch=True,allow_layer_mismatch=True)
        InPWG_Lbend.connect(port="St-L-o2", other=BH.ports["BH-o1"], allow_width_mismatch=True, allow_layer_mismatch=True)
        InPWG_Rbend.connect(port="St-R-o1", other=BH.ports["BH-o2"], allow_width_mismatch=True, allow_layer_mismatch=True)
        InPWG1stLbend.connect(port="Taper-L-o2", other=BH.ports["BH-o1"], allow_width_mismatch=True, allow_layer_mismatch=True)
        InPWG1stRbend.connect(port="Taper-R-o1", other=BH.ports["BH-o2"], allow_width_mismatch=True, allow_layer_mismatch=True)
        InPWG2ndL.connect(port="Trim-L-o2", other=InPWG1stLbend.ports["Tip-L-o1"], allow_width_mismatch=True, allow_layer_mismatch=True)
        InPWG2ndR.connect(port="Trim-R-o2", other=InPWG1stRbend.ports["Tip-R-o2"], allow_width_mismatch=True, allow_layer_mismatch=True)
        nViaA.connect(port="nVia-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pViaA.connect(port="pVia-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nMetalA.connect(port="nMetal-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pMetalA.connect(port="pMetal-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nPad1.connect(port="nPad1-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pPad1.connect(port="pPad1-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        # nPadVia.connect(port="nPadVia-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        # pPadVia.connect(port="pPadVia-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        
        if AbsSideType==1:#LeftSide
            InGaAsEtch_Lbend.connect(port="Bend-L-o2",other=InPWG_Lbend.ports["Taper-L-o1"],allow_width_mismatch=True,allow_layer_mismatch=True)
            SiOxWG_R.connect(port="Tip-R-o1", other=InPWG_Rbend.ports["TipR-root-o2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        elif AbsSideType==2:#RightSide
            InGaAsEtch_Rbend.connect(port="Bend-R-o1",other=InPWG_Rbend.ports["Taper-R-o2"],allow_width_mismatch=True,allow_layer_mismatch=True)
            SiOxWG_L.connect(port="Tip-L-o2", other=InPWG_Lbend.ports["TipL-root-o1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        elif AbsSideType==0:#No Absorption Region
            SiOxWG_L.connect(port="Tip-L-o2", other=InPWG_Lbend.ports["TipL-root-o1"], allow_width_mismatch=True,allow_layer_mismatch=True)
            SiOxWG_R.connect(port="Tip-R-o1", other=InPWG_Rbend.ports["TipR-root-o2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        else:
            pass
        
            
        
        PadPortsWidth=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]
        
        if Parameters[ID][Parameters["ParameterName"].index("PadType")]==0: #Lumped-type 集中定数 型
            
            if Parameters[ID][Parameters["ParameterName"].index("ProbeType")]==1: # for GSSG
                GnPad = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("dPadWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadLn")],layer=LAYER.PadMetal))
                GpPad = c.add_ref(BaseParts.pPad2(width=Parameters[ID][Parameters["ParameterName"].index("dPadWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadLn")],layer=LAYER.PadMetal))
                GnPadVia = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("dPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("dPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("dPadViaShift")],layer=LAYER.PadVia))
                GpPadVia = c.add_ref(BaseParts.pPadVia(width=Parameters[ID][Parameters["ParameterName"].index("dPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("dPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("dPadViaShift")],layer=LAYER.PadVia))
                
                PadSpacer=Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]/2
                PadPortsWidth=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]
                
                GnPad_ports = [
                gf.Port(f"GnPad_{i}", center=[0,-(Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(i+0.5)-Parameters[ID][Parameters["ParameterName"].index("dPadWd")]/2)],width=PadPortsWidth,orientation=270,port_type="electrical",layer=LAYER.PadMetal) 
                for i in range(2)
                ]
                GpPad_ports = [
                gf.Port(f"GpPad_{i}", center=[0,Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(i+0.5)-Parameters[ID][Parameters["ParameterName"].index("dPadWd")]/2],width=PadPortsWidth,orientation=90,port_type="electrical",layer=LAYER.PadMetal) 
                for i in range(2)
                ]
                
                nPad2.connect(port="nPad2-e1", other=GnPad_ports[0])
                GnPad.connect(port="nPad2-e1", other=GnPad_ports[1])
                pPad2.connect(port="pPad2-e2", other=GpPad_ports[0])    
                GpPad.connect(port="pPad2-e2", other=GpPad_ports[1])
                
                gf.routing.route_quad(c,port2=nPad2.ports["nPad2-e1"],port1=nPad1.ports["nPad1-e2"],width1=None,width2=None,layer=LAYER.PadMetal)
                gf.routing.route_quad(c,port2=pPad2.ports["pPad2-e2"],port1=pPad1.ports["pPad1-e1"],width1=None,width2=None,layer=LAYER.PadMetal)
                
                GnPadVia.move((GnPad.center[0]-Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")]/2,GnPad.center[1]-Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")]/2))
                GpPadVia.move((GpPad.center[0]-Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")]/2,GpPad.center[1]-Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")]/2))
                c.add_ports(GnPad_ports)
                c.add_ports(GpPad_ports)
            elif Parameters[ID][Parameters["ParameterName"].index("ProbeType")]==0:
                GnPad_ports = [
                gf.Port("GnPad_0", center=[0,-(Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2)],width=PadPortsWidth,orientation=270,port_type="electrical",layer=LAYER.PadMetal),
                ]
                GpPad_ports = [
                gf.Port("GpPad_0", center=[0,Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2],width=PadPortsWidth,orientation=90,port_type="electrical",layer=LAYER.PadMetal),
                ]
                nPad2.connect(port="nPad2-e1", other=GnPad_ports[0])
                pPad2.connect(port="pPad2-e2", other=GpPad_ports[0])
                # nPad2.connect(port="nPad2-e1", other=nPad1.ports["nPad1-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
                # pPad2.connect(port="pPad2-e2", other=pPad1.ports["pPad1-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
                gf.routing.route_quad(c,port2=nPad2.ports["nPad2-e1"],port1=nPad1.ports["nPad1-e2"],width1=None,width2=None,layer=LAYER.PadMetal)
                gf.routing.route_quad(c,port2=pPad2.ports["pPad2-e2"],port1=pPad1.ports["pPad1-e1"],width1=None,width2=None,layer=LAYER.PadMetal)
            else:
                pass       
                
        elif Parameters[ID][Parameters["ParameterName"].index("PadType")]==1: #TWB-type 伝搬定数型
            nPad3 = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad2Ln")],layer=LAYER.PadMetal))
            pPad3 = c.add_ref(BaseParts.pPad2(width=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad2Ln")],layer=LAYER.PadMetal))
            nPad3Via = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("nPadViaShift")],layer=LAYER.PadVia))
            pPad3Via = c.add_ref(BaseParts.pPadVia(width=Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("pPadViaShift")],layer=LAYER.PadVia))
            
            PadAddLength=Parameters[ID][Parameters["ParameterName"].index("DevLn")]/2*0.5
            PadAdd_2_Length=Parameters[ID][Parameters["ParameterName"].index("PadAdd_2_Length")]
            PadAdd_2_Width2=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")]
            PadAdd_2_Width1=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")]
            
            pPad2Add_1=c.add_ref(gf.components.ramp(length=PadAddLength,width1=2,width2=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],layer=LAYER.PadMetal))
            nPad2Add_1=c.add_ref(gf.components.ramp(length=PadAddLength,width1=2,width2=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],layer=LAYER.PadMetal))
            pPad3Add_1=c.add_ref(gf.components.ramp(length=PadAddLength,width1=2,width2=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],layer=LAYER.PadMetal))
            nPad3Add_1=c.add_ref(gf.components.ramp(length=PadAddLength,width1=2,width2=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],layer=LAYER.PadMetal))
            pPad2Add_2=c.add_ref(gf.components.ramp(length=PadAdd_2_Length,width1=PadAdd_2_Width1,width2=PadAdd_2_Width2,layer=LAYER.PadMetal))
            nPad2Add_2=c.add_ref(gf.components.ramp(length=PadAdd_2_Length,width1=PadAdd_2_Width1,width2=PadAdd_2_Width2,layer=LAYER.PadMetal))
            pPad3Add_2=c.add_ref(gf.components.ramp(length=PadAdd_2_Length,width1=PadAdd_2_Width1,width2=PadAdd_2_Width2,layer=LAYER.PadMetal))
            nPad3Add_2=c.add_ref(gf.components.ramp(length=PadAdd_2_Length,width1=PadAdd_2_Width1,width2=PadAdd_2_Width2,layer=LAYER.PadMetal))
            
            PadSpacer=Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]/2
            PadPortsWidth=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]
            dx = (Parameters[ID][Parameters["ParameterName"].index("BHLn")]/2+Parameters[ID][Parameters["ParameterName"].index("PadDistance_X")])
            
            if Parameters[ID][Parameters["ParameterName"].index("ProbeType")]==1: # for GSSG
                GnPadL = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("dPadWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadLn")],layer=LAYER.PadMetal))
                GpPadL = c.add_ref(BaseParts.pPad2(width=Parameters[ID][Parameters["ParameterName"].index("dPadWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadLn")],layer=LAYER.PadMetal))
                GnPadViaL = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("dPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("nPadViaShift")],layer=LAYER.PadVia))
                GpPadViaL = c.add_ref(BaseParts.pPadVia(width=Parameters[ID][Parameters["ParameterName"].index("dPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("pPadViaShift")],layer=LAYER.PadVia))
                GnPadR = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("dPadWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadLn")],layer=LAYER.PadMetal))
                GpPadR = c.add_ref(BaseParts.pPad2(width=Parameters[ID][Parameters["ParameterName"].index("dPadWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadLn")],layer=LAYER.PadMetal))
                GnPadViaR = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("dPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("nPadViaShift")],layer=LAYER.PadVia))
                GpPadViaR = c.add_ref(BaseParts.pPadVia(width=Parameters[ID][Parameters["ParameterName"].index("dPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("pPadViaShift")],layer=LAYER.PadVia))
                
                
                GnPadR_ports = [
                gf.Port(f"GnPadR_{i}", center=[dx,-(Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(i+0.5)-Parameters[ID][Parameters["ParameterName"].index("dPadWd")]/2)],width=PadPortsWidth,orientation=270,port_type="electrical",layer=LAYER.PadMetal) 
                for i in range(2)
                ]
                GpPadR_ports = [
                gf.Port(f"GpPadR_{i}", center=[dx,Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(i+0.5)-Parameters[ID][Parameters["ParameterName"].index("dPadWd")]/2],width=PadPortsWidth,orientation=90,port_type="electrical",layer=LAYER.PadMetal) 
                for i in range(2)
                ]
                GnPadL_ports = [
                gf.Port(f"GnPadL_{i}", center=[-dx,-(Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(i+0.5)-Parameters[ID][Parameters["ParameterName"].index("dPadWd")]/2)],width=PadPortsWidth,orientation=270,port_type="electrical",layer=LAYER.PadMetal) 
                for i in range(2)
                ]
                GpPadL_ports = [
                gf.Port(f"GpPadL_{i}", center=[-dx,Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(i+0.5)-Parameters[ID][Parameters["ParameterName"].index("dPadWd")]/2],width=PadPortsWidth,orientation=90,port_type="electrical",layer=LAYER.PadMetal) 
                for i in range(2)
                ]
                
                
                
                nPad2.connect(port="nPad2-e1", other=GnPadR_ports[0])
                pPad2.connect(port="pPad2-e2", other=GpPadR_ports[0])
                GnPadR.connect(port="nPad2-e1", other=GnPadR_ports[1])
                GpPadR.connect(port="pPad2-e2", other=GpPadR_ports[1])
                nPad3.connect(port="nPad2-e1", other=GnPadL_ports[0])
                pPad3.connect(port="pPad2-e2", other=GpPadL_ports[0])
                GnPadL.connect(port="nPad2-e1", other=GnPadL_ports[1])
                GpPadL.connect(port="pPad2-e2", other=GpPadL_ports[1])
                
                GnPadViaL.move((GnPadL.center[0]-Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")]/2,GnPadL.center[1]-Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")]/2))
                GnPadViaR.move((GnPadR.center[0]-Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")]/2,GnPadR.center[1]-Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")]/2))
                GpPadViaL.move((GpPadL.center[0]-Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")]/2,GpPadL.center[1]-Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")]/2))
                GpPadViaR.move((GpPadR.center[0]-Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")]/2,GpPadR.center[1]-Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")]/2))
               
                
            else:
                pPadR_ports = [
                    gf.Port(f"pPad_{i}", center=[dx,PadSpacer],width=PadPortsWidth,orientation=90*i,port_type="electrical",layer=LAYER.PadMetal) 
                    for i in range(4)
                    ]
                pPadL_ports = [
                    gf.Port(f"pPad_{i}", center=[-dx,PadSpacer],width=PadPortsWidth,orientation=90*i,port_type="electrical",layer=LAYER.PadMetal) 
                    for i in range(4)
                    ]
                
                nPadR_ports = [
                    gf.Port(f"nPad_{i}", center=[dx,-PadSpacer],width=PadPortsWidth,orientation=90*i,port_type="electrical",layer=LAYER.PadMetal)
                    for i in range(4)
                    ]
                nPadL_ports = [
                    gf.Port(f"nPad_{i}", center=[-dx,-PadSpacer],width=PadPortsWidth,orientation=90*i,port_type="electrical",layer=LAYER.PadMetal)
                    for i in range(4)
                    ]
                
                
                
                pPad2.connect(port="pPad2-e3", other=pPadR_ports[0])
                nPad2.connect(port="nPad2-e3", other=nPadR_ports[0])
                pPad3.connect(port="pPad2-e1", other=pPadL_ports[2])
                nPad3.connect(port="nPad2-e1", other=nPadL_ports[2])
            
            gf.routing.route_quad(c,port2=pPad2.ports["pPad2-e3"],port1=pPad1.ports["pPad1-e4"],width1=None,width2=None,layer=LAYER.PadMetal)
            gf.routing.route_quad(c,port2=nPad2.ports["nPad2-e3"],port1=nPad1.ports["nPad1-e4"],width1=None,width2=None,layer=LAYER.PadMetal)
            gf.routing.route_quad(c,port2=pPad3.ports["pPad2-e4"],port1=pPad1.ports["pPad1-e3"],width1=None,width2=None,layer=LAYER.PadMetal)
            gf.routing.route_quad(c,port2=nPad3.ports["nPad2-e4"],port1=nPad1.ports["nPad1-e3"],width1=None,width2=None,layer=LAYER.PadMetal)
            
            pPad2Add_1.connect(port="o2",other=pPad2.ports["pPad2-e3"],allow_type_mismatch=True)
            nPad2Add_1.connect(port="o2",other=nPad2.ports["nPad2-e3"],allow_type_mismatch=True,mirror=True)
            pPad3Add_1.connect(port="o2",other=pPad3.ports["pPad2-e4"],allow_type_mismatch=True,mirror=True)
            nPad3Add_1.connect(port="o2",other=nPad3.ports["nPad2-e4"],allow_type_mismatch=True)
            pPad2Add_2.connect(port="o2",other=pPad2.ports["pPad2-e2"],allow_type_mismatch=True,mirror=True)
            nPad2Add_2.connect(port="o2",other=nPad2.ports["nPad2-e1"],allow_type_mismatch=True)
            pPad3Add_2.connect(port="o2",other=pPad3.ports["pPad2-e2"],allow_type_mismatch=True)
            nPad3Add_2.connect(port="o2",other=nPad3.ports["nPad2-e1"],allow_type_mismatch=True,mirror=True)
            
            
            
                 
            nPad3Via.move((nPad3.center[0]-Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")]/2,nPad3.center[1]-Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")]/2))
            pPad3Via.move((pPad3.center[0]-Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")]/2,pPad3.center[1]-Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")]/2))
        
            
            
        
        nPad2Via.move((nPad2.center[0]-Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")]/2,nPad2.center[1]-Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")]/2))
        pPad2Via.move((pPad2.center[0]-Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")]/2,pPad2.center[1]-Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")]/2))
        
        c.add_ports(SiOxWG_L.ports,prefix="Dev_L-")
        c.add_ports(SiOxWG_R.ports,prefix="Dev_R-")
        #c.add_ports(nPad2.ports)
        #c.add_ports(pPad2.ports)
        
        #c.pprint_ports()
        #c.draw_ports()
        
        return c


    @gf.cell
    def TEG_EL(Parameters,ID): #Parameters変数はリストで定義。
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        c = gf.Component() #キャンパスを定義
            
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        BH = c.add_ref(BaseParts.BHetch(width=Parameters[ID][Parameters["ParameterName"].index("BHWd")],length=Parameters[ID][Parameters["ParameterName"].index("BHLn")],shift=Parameters[ID][Parameters["ParameterName"].index("StLn")],layer=LAYER.BH)) #キャンパス内にBHを配置
        BHdummy1 = c.add_ref(BaseParts.BHdummy(width=Parameters[ID][Parameters["ParameterName"].index("BHDWdA")],length=Parameters[ID][Parameters["ParameterName"].index("BHDLnA")],spacer=Parameters[ID][Parameters["ParameterName"].index("BHDsp")],layer=LAYER.BHdmyA)) #キャンパス内にBHdummyを配置
        BHdummy2 = c.add_ref(BaseParts.BHdummy(width=Parameters[ID][Parameters["ParameterName"].index("BHDWdA")],length=Parameters[ID][Parameters["ParameterName"].index("BHDLnA")],spacer=Parameters[ID][Parameters["ParameterName"].index("BHDsp")],layer=LAYER.BHdmyA))
        nDpA = c.add_ref(BaseParts.nDpA(width=Parameters[ID][Parameters["ParameterName"].index("nDopeWd")],length=Parameters[ID][Parameters["ParameterName"].index("nDopeLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nDopeSp")],layer=LAYER.nDope)) 
        pDpA = c.add_ref(BaseParts.pDpA(width=Parameters[ID][Parameters["ParameterName"].index("pDopeWd")],length=Parameters[ID][Parameters["ParameterName"].index("pDopeLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pDopeSp")],layer=LAYER.pDope))
        InGaAs1 = c.add_ref(BaseParts.InGaAsEtch(width=Parameters[ID][Parameters["ParameterName"].index("pConWd")],length=Parameters[ID][Parameters["ParameterName"].index("pConLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pConSp")],layer=LAYER.InGaAs)) 
        InGaAs2 = c.add_ref(BaseParts.InGaAsEtch(width=Parameters[ID][Parameters["ParameterName"].index("pConWd")],length=Parameters[ID][Parameters["ParameterName"].index("pConLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pConSp")],layer=LAYER.InGaAs)) 
        Device1 = c.add_ref(BaseParts.Device(width=Parameters[ID][Parameters["ParameterName"].index("DevWd")],length=Parameters[ID][Parameters["ParameterName"].index("DevLn")],layer=LAYER.InPWG1st))
        Device2 = c.add_ref(BaseParts.Device(width=Parameters[ID][Parameters["ParameterName"].index("DevWd")],length=Parameters[ID][Parameters["ParameterName"].index("DevLn")],layer=LAYER.InPWG))
        nViaA = c.add_ref(BaseParts.nViaA(width=Parameters[ID][Parameters["ParameterName"].index("nViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nViaSp")],layer=LAYER.nVia)) 
        pViaA = c.add_ref(BaseParts.pViaA(width=Parameters[ID][Parameters["ParameterName"].index("pViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pViaSp")],layer=LAYER.pVia)) 
        nMetalA = c.add_ref(BaseParts.nMetalA(width=Parameters[ID][Parameters["ParameterName"].index("nMetalWd")],length=Parameters[ID][Parameters["ParameterName"].index("nMetalLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nMetalSp")],layer=LAYER.nMetal))
        pMetalA = c.add_ref(BaseParts.pMetalA(width=Parameters[ID][Parameters["ParameterName"].index("pMetalWd")],length=Parameters[ID][Parameters["ParameterName"].index("pMetalLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pMetalSp")],layer=LAYER.pMetal))
        nPad1 = c.add_ref(BaseParts.nPad1(width=Parameters[ID][Parameters["ParameterName"].index("nPad1Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad1Ln")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadSp")],layer=LAYER.PadMetal))
        pPad1 = c.add_ref(BaseParts.pPad1(width=Parameters[ID][Parameters["ParameterName"].index("pPad1Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad1Ln")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadSp")],layer=LAYER.PadMetal))
        nPad2 = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad2Ln")],layer=LAYER.PadMetal))
        pPad2 = c.add_ref(BaseParts.pPad2(width=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad2Ln")],layer=LAYER.PadMetal))
        nPadVia = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("nPadViaShift")],layer=LAYER.PadVia))
        pPadVia = c.add_ref(BaseParts.pPadVia(width=Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("pPadViaShift")],layer=LAYER.PadVia))
        
        BH.move((-Parameters[ID][Parameters["ParameterName"].index("BHLn")]/2,-Parameters[ID][Parameters["ParameterName"].index("BHWd")]/2)) #Deviceを中央に
        
        ##各コンポーネント同士を接続
        BHdummy1.connect(port="BHdummy-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        BHdummy2.connect(port="BHdummy-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nDpA.connect(port="nDpA-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pDpA.connect(port="pDpA-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        InGaAs1.connect(port="InGaAs-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        InGaAs2.connect(port="InGaAs-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        Device1.connect(port="Device-e4", other=BH.ports["BH-e3"], allow_width_mismatch=True,allow_layer_mismatch=True)
        Device2.connect(port="Device-e4", other=BH.ports["BH-e3"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nViaA.connect(port="nVia-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pViaA.connect(port="pVia-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nMetalA.connect(port="nMetal-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pMetalA.connect(port="pMetal-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nPad1.connect(port="nPad1-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pPad1.connect(port="pPad1-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        
        PadPortsWidth=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]
        GnPad_ports = [
        gf.Port("GnPad_0", center=[0,-(Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2)],width=PadPortsWidth,orientation=270,port_type="electrical",layer=LAYER.PadMetal),
        ]
        GpPad_ports = [
        gf.Port("GpPad_0", center=[0,Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2],width=PadPortsWidth,orientation=90,port_type="electrical",layer=LAYER.PadMetal),
        ]
        nPad2.connect(port="nPad2-e1", other=GnPad_ports[0])
        pPad2.connect(port="pPad2-e2", other=GpPad_ports[0])
        # nPad2.connect(port="nPad2-e1", other=nPad1.ports["nPad1-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        # pPad2.connect(port="pPad2-e2", other=pPad1.ports["pPad1-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        gf.routing.route_quad(c,port2=nPad2.ports["nPad2-e1"],port1=nPad1.ports["nPad1-e2"],width1=None,width2=None,layer=LAYER.PadMetal)
        gf.routing.route_quad(c,port2=pPad2.ports["pPad2-e2"],port1=pPad1.ports["pPad1-e1"],width1=None,width2=None,layer=LAYER.PadMetal)       
        
        nPadVia.move((nPad2.center[0]-Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")]/2,nPad2.center[1]-Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")]/2))
        pPadVia.move((pPad2.center[0]-Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")]/2,pPad2.center[1]-Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")]/2))
        
        c.add_ports(nPad2.ports)
        c.add_ports(pPad2.ports)
        
        #c.pprint_ports()
        #c.draw_ports()
        
        return c
    
    @gf.cell(check_ports=False)
    def TEG_InPWG(Parameters,ID): #Parameters変数はリストで定義。
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        c = gf.Component() #キャンパスを定義
        ##cross_sectionの定義が必要の場合はここで定義
        XS_SiOx=CrossSections.XS_SiOx(SiOxCoreWidth=Parameters[ID][Parameters["ParameterName"].index("SiOxCoreWd")],SiOxEtchWidth=Parameters[ID][Parameters["ParameterName"].index("SiOxEtchWd")],radius=Parameters[ID][Parameters["ParameterName"].index("SiOxBendRadius")],SiOxWG_Layer=LAYER.SiOxWG,SiOxEtch_Layer=LAYER.SiOxEtch)
        XS_InPWG=CrossSections.XS_InPWG(Width=Parameters[ID][Parameters["ParameterName"].index("WgWd")],radius=Parameters[ID][Parameters["ParameterName"].index("WgBendRadius")],InPWG_Layer=LAYER.InPWG,InPWG1stEtch_Layer=LAYER.InPWG1st)
        
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        #InPWG_St=c.create_vinst(gf.components.waveguides.straight(length=Parameters[ID][Parameters["ParameterName"].index("DevLn")],cross_section=XS_InPWG))
        InPWG_Lbend=c.create_vinst(BaseParts.InPWG(Type="L",St1Ln=Parameters[ID][Parameters["ParameterName"].index("St1Ln")],St1Wd=Parameters[ID][Parameters["ParameterName"].index("St1Wd")],TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TaperWd1=Parameters[ID][Parameters["ParameterName"].index("TaperWd1")],TaperWd2=Parameters[ID][Parameters["ParameterName"].index("TaperWd2")],St2Ln=Parameters[ID][Parameters["ParameterName"].index("St2Ln")],St2Wd=Parameters[ID][Parameters["ParameterName"].index("St2Wd")],St3Ln=Parameters[ID][Parameters["ParameterName"].index("St3Ln")],St3Wd=Parameters[ID][Parameters["ParameterName"].index("St3Wd")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],radius=Parameters[ID][Parameters["ParameterName"].index("WgBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgLAngle")],layer=LAYER.InPWG)) 
        InPWG_Rbend=c.create_vinst(BaseParts.InPWG(Type="R",St1Ln=Parameters[ID][Parameters["ParameterName"].index("St1Ln")],St1Wd=Parameters[ID][Parameters["ParameterName"].index("St1Wd")],TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TaperWd1=Parameters[ID][Parameters["ParameterName"].index("TaperWd1")],TaperWd2=Parameters[ID][Parameters["ParameterName"].index("TaperWd2")],St2Ln=Parameters[ID][Parameters["ParameterName"].index("St2Ln")],St2Wd=Parameters[ID][Parameters["ParameterName"].index("St2Wd")],St3Ln=Parameters[ID][Parameters["ParameterName"].index("St3Ln")],St3Wd=Parameters[ID][Parameters["ParameterName"].index("St3Wd")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],radius=Parameters[ID][Parameters["ParameterName"].index("WgBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgRAngle")],layer=LAYER.InPWG)) 
        InPWG1stLbend=c.create_vinst(BaseParts.InPWG1st(Type="L",St1Ln=Parameters[ID][Parameters["ParameterName"].index("St1Ln")],St1Wd=Parameters[ID][Parameters["ParameterName"].index("St1Wd")],TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TaperWd1=Parameters[ID][Parameters["ParameterName"].index("TaperWd1")],TaperWd2=Parameters[ID][Parameters["ParameterName"].index("TaperWd2")],St2Ln=Parameters[ID][Parameters["ParameterName"].index("St2Ln")],St2Wd=Parameters[ID][Parameters["ParameterName"].index("St2Wd")],St3Ln=Parameters[ID][Parameters["ParameterName"].index("St3Ln")],St3Wd=Parameters[ID][Parameters["ParameterName"].index("St3Wd")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipDLn=Parameters[ID][Parameters["ParameterName"].index("TipDLn")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],radius=Parameters[ID][Parameters["ParameterName"].index("WgBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgLAngle")],layer=LAYER.InPWG1st)) 
        InPWG1stRbend=c.create_vinst(BaseParts.InPWG1st(Type="R",St1Ln=Parameters[ID][Parameters["ParameterName"].index("St1Ln")],St1Wd=Parameters[ID][Parameters["ParameterName"].index("St1Wd")],TaperLn=Parameters[ID][Parameters["ParameterName"].index("TaperLn")],TaperWd1=Parameters[ID][Parameters["ParameterName"].index("TaperWd1")],TaperWd2=Parameters[ID][Parameters["ParameterName"].index("TaperWd2")],St2Ln=Parameters[ID][Parameters["ParameterName"].index("St2Ln")],St2Wd=Parameters[ID][Parameters["ParameterName"].index("St2Wd")],St3Ln=Parameters[ID][Parameters["ParameterName"].index("St3Ln")],St3Wd=Parameters[ID][Parameters["ParameterName"].index("St3Wd")],TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],TipDLn=Parameters[ID][Parameters["ParameterName"].index("TipDLn")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],radius=Parameters[ID][Parameters["ParameterName"].index("WgBendRadius")],BendAngle=Parameters[ID][Parameters["ParameterName"].index("BendWgRAngle")],layer=LAYER.InPWG1st)) 
        InPWG2ndL = c.create_vinst(BaseParts.InPWG2nd(Type="L",TrimLn=Parameters[ID][Parameters["ParameterName"].index("TrimLn")],TrimWd=Parameters[ID][Parameters["ParameterName"].index("TrimWd")],TrimAddLn=Parameters[ID][Parameters["ParameterName"].index("TrimAddLn")],TrimAddWd=Parameters[ID][Parameters["ParameterName"].index("TrimAddWd")],TaperWd=Parameters[ID][Parameters["ParameterName"].index("TaperWd2")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],layer=LAYER.InPWG2nd))
        InPWG2ndR = c.create_vinst(BaseParts.InPWG2nd(Type="R",TrimLn=Parameters[ID][Parameters["ParameterName"].index("TrimLn")],TrimWd=Parameters[ID][Parameters["ParameterName"].index("TrimWd")],TrimAddLn=Parameters[ID][Parameters["ParameterName"].index("TrimAddLn")],TrimAddWd=Parameters[ID][Parameters["ParameterName"].index("TrimAddWd")],TaperWd=Parameters[ID][Parameters["ParameterName"].index("TaperWd2")],TipWd=Parameters[ID][Parameters["ParameterName"].index("TipWd")],layer=LAYER.InPWG2nd))
             
        SiOxWG_R = c.create_vinst(BaseParts.SiOxWG_Tip(Type="R",TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],cross_section=XS_SiOx))  
        SiOxWG_L = c.create_vinst(BaseParts.SiOxWG_Tip(Type="L",TipLn=Parameters[ID][Parameters["ParameterName"].index("TipLn")],cross_section=XS_SiOx)) 
     
        Mid_ports = [
            gf.Port("Mid1_1", center=(Parameters[ID][Parameters["ParameterName"].index("Mid1X")],Parameters[ID][Parameters["ParameterName"].index("Mid1Y")]),width=Parameters[ID][Parameters["ParameterName"].index("WgWd")],orientation=0,layer=LAYER.InPWG),
            gf.Port("Mid1_3", center=(Parameters[ID][Parameters["ParameterName"].index("Mid1X")],Parameters[ID][Parameters["ParameterName"].index("Mid1Y")]),width=Parameters[ID][Parameters["ParameterName"].index("WgWd")],orientation=180,layer=LAYER.InPWG),
            gf.Port("Mid2_1", center=(Parameters[ID][Parameters["ParameterName"].index("Mid2X")],Parameters[ID][Parameters["ParameterName"].index("Mid2Y")]),width=Parameters[ID][Parameters["ParameterName"].index("WgWd")],orientation=0,layer=LAYER.InPWG),
            gf.Port("Mid2_3", center=(Parameters[ID][Parameters["ParameterName"].index("Mid2X")],Parameters[ID][Parameters["ParameterName"].index("Mid2Y")]),width=Parameters[ID][Parameters["ParameterName"].index("WgWd")],orientation=180,layer=LAYER.InPWG),
            gf.Port("Mid3_1", center=(Parameters[ID][Parameters["ParameterName"].index("Mid3X")],Parameters[ID][Parameters["ParameterName"].index("Mid3Y")]),width=Parameters[ID][Parameters["ParameterName"].index("WgWd")],orientation=0,layer=LAYER.InPWG),
            gf.Port("Mid3_3", center=(Parameters[ID][Parameters["ParameterName"].index("Mid3X")],Parameters[ID][Parameters["ParameterName"].index("Mid3Y")]),width=Parameters[ID][Parameters["ParameterName"].index("WgWd")],orientation=180,layer=LAYER.InPWG),
            gf.Port("Mid4_1", center=(Parameters[ID][Parameters["ParameterName"].index("Mid4X")],Parameters[ID][Parameters["ParameterName"].index("Mid4Y")]),width=Parameters[ID][Parameters["ParameterName"].index("WgWd")],orientation=0,layer=LAYER.InPWG),
            gf.Port("Mid4_3", center=(Parameters[ID][Parameters["ParameterName"].index("Mid4X")],Parameters[ID][Parameters["ParameterName"].index("Mid4Y")]),width=Parameters[ID][Parameters["ParameterName"].index("WgWd")],orientation=180,layer=LAYER.InPWG),
            
        ]
        IO_ports = [
            gf.Port("IOLeft_1", center=(Parameters[ID][Parameters["ParameterName"].index("IOLeftX")],Parameters[ID][Parameters["ParameterName"].index("IOLeftY")]),width=Parameters[ID][Parameters["ParameterName"].index("SiOxCoreWd")],orientation=0,layer=LAYER.SiOxWG),
            gf.Port("IORight_3", center=(Parameters[ID][Parameters["ParameterName"].index("IORightX")],Parameters[ID][Parameters["ParameterName"].index("IORightY")]),width=Parameters[ID][Parameters["ParameterName"].index("SiOxCoreWd")],orientation=180,layer=LAYER.SiOxWG),
        ] 
        
        ##各コンポーネント同士を接続
        
        InPWG_Lbend.connect(port="Tip-L-o1", other=Mid_ports[0], allow_width_mismatch=True, allow_layer_mismatch=True)
        InPWG1stLbend.connect(port="Taper-L-o2", other=InPWG_Lbend.ports["St-L-o1"], allow_width_mismatch=True, allow_layer_mismatch=True)
        InPWG2ndL.connect(port="Trim-L-o2", other=InPWG1stLbend.ports["Taper-L-o1"], allow_width_mismatch=True, allow_layer_mismatch=True)
        SiOxWG_L.connect(port="Tip-L-o2", other=InPWG_Lbend.ports["TipL-root-o1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        route1 = gf.routing.route_bundle_sbend(c,ports1=IO_ports[0:1],ports2=Mid_ports[0:1],cross_section=XS_SiOx)
            
        if Parameters[ID][Parameters["ParameterName"].index("Type")]==1:    
            InPWG_Rbend.connect(port="Tip-R-o2", other=Mid_ports[7], allow_width_mismatch=True, allow_layer_mismatch=True)
            InPWG1stRbend.connect(port="Taper-R-o1", other=InPWG_Rbend.ports["St-R-o2"], allow_width_mismatch=True, allow_layer_mismatch=True)
            InPWG2ndR.connect(port="Trim-R-o2", other=InPWG1stRbend.ports["Taper-R-o2"], allow_width_mismatch=True, allow_layer_mismatch=True)
            SiOxWG_R.connect(port="Tip-R-o1", other=InPWG_Rbend.ports["TipR-root-o2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        
            route2 = gf.routing.route_single(c,port1=Mid_ports[3],port2=InPWG_Lbend.ports["St-L-o2"],allow_width_mismatch=True,cross_section=XS_InPWG)
            route3 = gf.routing.route_bundle_sbend(c,ports1=Mid_ports[2:3],ports2=Mid_ports[4:5],cross_section=XS_InPWG)
            route4 = gf.routing.route_single(c,port1=InPWG_Rbend.ports["Tip-R-o1"],port2=Mid_ports[4],cross_section=XS_InPWG)
            
        else:
            InPWG_Rbend.connect(port="St-R-o2", other=Mid_ports[3], allow_width_mismatch=True, allow_layer_mismatch=True)
            InPWG1stRbend.connect(port="Taper-R-o1", other=InPWG_Rbend.ports["St-R-o2"], allow_width_mismatch=True, allow_layer_mismatch=True)
            InPWG2ndR.connect(port="Trim-R-o2", other=InPWG1stRbend.ports["Taper-R-o2"], allow_width_mismatch=True, allow_layer_mismatch=True)
            SiOxWG_R.connect(port="Tip-R-o1", other=InPWG_Rbend.ports["TipR-root-o2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        
            route2 = gf.routing.route_single(c,port1=InPWG_Lbend.ports["St-L-o1"],allow_width_mismatch=True,port2=Mid_ports[2],cross_section=XS_InPWG)
            route3 = gf.routing.route_single_sbend(c,port1=SiOxWG_R.ports["Tip-R-o2"],port2=Mid_ports[5],cross_section=XS_SiOx)
            route4 = gf.routing.route_bundle_sbend(c,ports1=Mid_ports[4:5],ports2=Mid_ports[7:8],allow_width_mismatch=True,allow_layer_mismatch=True,cross_section=XS_SiOx)
            
            
        
        route5 = gf.routing.route_bundle_sbend(c,ports2=IO_ports[1:2],ports1=Mid_ports[6:7],allow_width_mismatch=True,allow_layer_mismatch=True,cross_section=XS_SiOx)
        
        #c.add_ports(SiOxWG_L.ports,prefix="Dev_L-")
        #c.add_ports(SiOxWG_R.ports,prefix="Dev_R-")
        
        #c.add_ports(IO_ports)
        c.add_ports(Mid_ports)
        c.add_ports(InPWG_Lbend.ports)
        c.add_ports(InPWG_Rbend.ports)
        #c.add_ports(SiOxWG_R.ports)
        #c.pprint_ports()
        #c.draw_ports()
        
        return c
    
    @gf.cell
    def TEG_RP(Parameters,ID): #Parameters変数はリストで定義。
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        c = gf.Component() #キャンパスを定義
            
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        BH = c.add_ref(BaseParts.BHetch(width=Parameters[ID][Parameters["ParameterName"].index("BHWd")],length=Parameters[ID][Parameters["ParameterName"].index("BHLn")],shift=Parameters[ID][Parameters["ParameterName"].index("StLn")],layer=LAYER.pDope)) #キャンパス内にBHを配置
        nDpA = c.add_ref(BaseParts.nDpA(width=Parameters[ID][Parameters["ParameterName"].index("nDopeWd")],length=Parameters[ID][Parameters["ParameterName"].index("nDopeLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nDopeSp")],layer=LAYER.pDope)) 
        pDpA = c.add_ref(BaseParts.pDpA(width=Parameters[ID][Parameters["ParameterName"].index("pDopeWd")],length=Parameters[ID][Parameters["ParameterName"].index("pDopeLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pDopeSp")],layer=LAYER.pDope))
        InGaAs1 = c.add_ref(BaseParts.InGaAsEtch(width=Parameters[ID][Parameters["ParameterName"].index("pConWd")],length=Parameters[ID][Parameters["ParameterName"].index("pConLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pConSp")],layer=LAYER.InGaAs)) 
        InGaAs2 = c.add_ref(BaseParts.InGaAsEtch(width=Parameters[ID][Parameters["ParameterName"].index("pConWd")],length=Parameters[ID][Parameters["ParameterName"].index("pConLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pConSp")],layer=LAYER.InGaAs)) 
        Device1 = c.add_ref(BaseParts.Device(width=Parameters[ID][Parameters["ParameterName"].index("DevWd")],length=Parameters[ID][Parameters["ParameterName"].index("DevLn")],layer=LAYER.InPWG1st))
        Device2 = c.add_ref(BaseParts.Device(width=Parameters[ID][Parameters["ParameterName"].index("DevWd")],length=Parameters[ID][Parameters["ParameterName"].index("DevLn")],layer=LAYER.InPWG))
        nViaA = c.add_ref(BaseParts.nViaA(width=Parameters[ID][Parameters["ParameterName"].index("nViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nViaSp")],layer=LAYER.pVia)) 
        pViaA = c.add_ref(BaseParts.pViaA(width=Parameters[ID][Parameters["ParameterName"].index("pViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pViaSp")],layer=LAYER.pVia)) 
        nMetalA = c.add_ref(BaseParts.nMetalA(width=Parameters[ID][Parameters["ParameterName"].index("nMetalWd")],length=Parameters[ID][Parameters["ParameterName"].index("nMetalLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nMetalSp")],layer=LAYER.pMetal))
        pMetalA = c.add_ref(BaseParts.pMetalA(width=Parameters[ID][Parameters["ParameterName"].index("pMetalWd")],length=Parameters[ID][Parameters["ParameterName"].index("pMetalLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pMetalSp")],layer=LAYER.pMetal))
        nPad1 = c.add_ref(BaseParts.nPad1(width=Parameters[ID][Parameters["ParameterName"].index("nPad1Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad1Ln")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadSp")],layer=LAYER.PadMetal))
        pPad1 = c.add_ref(BaseParts.pPad1(width=Parameters[ID][Parameters["ParameterName"].index("pPad1Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad1Ln")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadSp")],layer=LAYER.PadMetal))
        nPad2 = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad2Ln")],layer=LAYER.PadMetal))
        pPad2 = c.add_ref(BaseParts.pPad2(width=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad2Ln")],layer=LAYER.PadMetal))
        nPadVia = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("nPadViaShift")],layer=LAYER.PadVia))
        pPadVia = c.add_ref(BaseParts.pPadVia(width=Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("pPadViaShift")],layer=LAYER.PadVia))
        
        BH.move((-Parameters[ID][Parameters["ParameterName"].index("BHLn")]/2,-Parameters[ID][Parameters["ParameterName"].index("BHWd")]/2)) #Deviceを中央に
        
        ##各コンポーネント同士を接続
        nDpA.connect(port="nDpA-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pDpA.connect(port="pDpA-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        InGaAs1.connect(port="InGaAs-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        InGaAs2.connect(port="InGaAs-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        Device1.connect(port="Device-e4", other=BH.ports["BH-e3"], allow_width_mismatch=True,allow_layer_mismatch=True)
        Device2.connect(port="Device-e4", other=BH.ports["BH-e3"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nViaA.connect(port="nVia-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pViaA.connect(port="pVia-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nMetalA.connect(port="nMetal-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pMetalA.connect(port="pMetal-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nPad1.connect(port="nPad1-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pPad1.connect(port="pPad1-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        
        PadPortsWidth=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]
        GnPad_ports = [
        gf.Port("GnPad_0", center=[0,-(Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2)],width=PadPortsWidth,orientation=270,port_type="electrical",layer=LAYER.PadMetal),
        ]
        GpPad_ports = [
        gf.Port("GpPad_0", center=[0,Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2],width=PadPortsWidth,orientation=90,port_type="electrical",layer=LAYER.PadMetal),
        ]
        nPad2.connect(port="nPad2-e1", other=GnPad_ports[0])
        pPad2.connect(port="pPad2-e2", other=GpPad_ports[0])
        # nPad2.connect(port="nPad2-e1", other=nPad1.ports["nPad1-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        # pPad2.connect(port="pPad2-e2", other=pPad1.ports["pPad1-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        gf.routing.route_quad(c,port2=nPad2.ports["nPad2-e1"],port1=nPad1.ports["nPad1-e2"],width1=None,width2=None,layer=LAYER.PadMetal)
        gf.routing.route_quad(c,port2=pPad2.ports["pPad2-e2"],port1=pPad1.ports["pPad1-e1"],width1=None,width2=None,layer=LAYER.PadMetal)       
        
        nPadVia.move((nPad2.center[0]-Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")]/2,nPad2.center[1]-Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")]/2))
        pPadVia.move((pPad2.center[0]-Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")]/2,pPad2.center[1]-Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")]/2))
        
        c.add_ports(nPad2.ports)
        c.add_ports(pPad2.ports)
        
        #c.pprint_ports()
        #c.draw_ports()
        
        return c
    
    @gf.cell
    def TEG_RN(Parameters,ID): #Parameters変数はリストで定義。
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        c = gf.Component() #キャンパスを定義
            
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        BH = c.add_ref(BaseParts.BHetch(width=Parameters[ID][Parameters["ParameterName"].index("BHWd")],length=Parameters[ID][Parameters["ParameterName"].index("BHLn")],shift=Parameters[ID][Parameters["ParameterName"].index("StLn")],layer=LAYER.nDope)) #キャンパス内にBHを配置
        nDpA = c.add_ref(BaseParts.nDpA(width=Parameters[ID][Parameters["ParameterName"].index("nDopeWd")],length=Parameters[ID][Parameters["ParameterName"].index("nDopeLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nDopeSp")],layer=LAYER.nDope)) 
        pDpA = c.add_ref(BaseParts.pDpA(width=Parameters[ID][Parameters["ParameterName"].index("pDopeWd")],length=Parameters[ID][Parameters["ParameterName"].index("pDopeLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pDopeSp")],layer=LAYER.nDope))
        InGaAs1 = c.add_ref(BaseParts.InGaAsEtch(width=Parameters[ID][Parameters["ParameterName"].index("pConWd")],length=Parameters[ID][Parameters["ParameterName"].index("pConLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pConSp")],layer=LAYER.InGaAs)) 
        InGaAs2 = c.add_ref(BaseParts.InGaAsEtch(width=Parameters[ID][Parameters["ParameterName"].index("pConWd")],length=Parameters[ID][Parameters["ParameterName"].index("pConLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pConSp")],layer=LAYER.InGaAs)) 
        Device1 = c.add_ref(BaseParts.Device(width=Parameters[ID][Parameters["ParameterName"].index("DevWd")],length=Parameters[ID][Parameters["ParameterName"].index("DevLn")],layer=LAYER.InPWG1st))
        Device2 = c.add_ref(BaseParts.Device(width=Parameters[ID][Parameters["ParameterName"].index("DevWd")],length=Parameters[ID][Parameters["ParameterName"].index("DevLn")],layer=LAYER.InPWG))
        nViaA = c.add_ref(BaseParts.nViaA(width=Parameters[ID][Parameters["ParameterName"].index("nViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nViaSp")],layer=LAYER.nVia)) 
        pViaA = c.add_ref(BaseParts.pViaA(width=Parameters[ID][Parameters["ParameterName"].index("pViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pViaSp")],layer=LAYER.nVia)) 
        nMetalA = c.add_ref(BaseParts.nMetalA(width=Parameters[ID][Parameters["ParameterName"].index("nMetalWd")],length=Parameters[ID][Parameters["ParameterName"].index("nMetalLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nMetalSp")],layer=LAYER.nMetal))
        pMetalA = c.add_ref(BaseParts.pMetalA(width=Parameters[ID][Parameters["ParameterName"].index("pMetalWd")],length=Parameters[ID][Parameters["ParameterName"].index("pMetalLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pMetalSp")],layer=LAYER.nMetal))
        nPad1 = c.add_ref(BaseParts.nPad1(width=Parameters[ID][Parameters["ParameterName"].index("nPad1Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad1Ln")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadSp")],layer=LAYER.PadMetal))
        pPad1 = c.add_ref(BaseParts.pPad1(width=Parameters[ID][Parameters["ParameterName"].index("pPad1Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad1Ln")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadSp")],layer=LAYER.PadMetal))
        nPad2 = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("nPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("nPad2Ln")],layer=LAYER.PadMetal))
        pPad2 = c.add_ref(BaseParts.pPad2(width=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")],length=Parameters[ID][Parameters["ParameterName"].index("pPad2Ln")],layer=LAYER.PadMetal))
        nPadVia = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("nPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("nPadViaShift")],layer=LAYER.PadVia))
        pPadVia = c.add_ref(BaseParts.pPadVia(width=Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("pPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("pPadViaShift")],layer=LAYER.PadVia))
        
        BH.move((-Parameters[ID][Parameters["ParameterName"].index("BHLn")]/2,-Parameters[ID][Parameters["ParameterName"].index("BHWd")]/2)) #Deviceを中央に
        
        ##各コンポーネント同士を接続
        nDpA.connect(port="nDpA-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pDpA.connect(port="pDpA-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        InGaAs1.connect(port="InGaAs-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        InGaAs2.connect(port="InGaAs-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        Device1.connect(port="Device-e4", other=BH.ports["BH-e3"], allow_width_mismatch=True,allow_layer_mismatch=True)
        Device2.connect(port="Device-e4", other=BH.ports["BH-e3"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nViaA.connect(port="nVia-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pViaA.connect(port="pVia-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nMetalA.connect(port="nMetal-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pMetalA.connect(port="pMetal-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        nPad1.connect(port="nPad1-e1", other=BH.ports["BH-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        pPad1.connect(port="pPad1-e2", other=BH.ports["BH-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        
        PadPortsWidth=Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]
        GnPad_ports = [
        gf.Port("GnPad_0", center=[0,-(Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2)],width=PadPortsWidth,orientation=270,port_type="electrical",layer=LAYER.PadMetal),
        ]
        GpPad_ports = [
        gf.Port("GpPad_0", center=[0,Parameters[ID][Parameters["ParameterName"].index("PadDistance_Y")]*(0.5)-Parameters[ID][Parameters["ParameterName"].index("pPad2Wd")]/2],width=PadPortsWidth,orientation=90,port_type="electrical",layer=LAYER.PadMetal),
        ]
        nPad2.connect(port="nPad2-e1", other=GnPad_ports[0])
        pPad2.connect(port="pPad2-e2", other=GpPad_ports[0])
        # nPad2.connect(port="nPad2-e1", other=nPad1.ports["nPad1-e2"], allow_width_mismatch=True,allow_layer_mismatch=True)
        # pPad2.connect(port="pPad2-e2", other=pPad1.ports["pPad1-e1"], allow_width_mismatch=True,allow_layer_mismatch=True)
        gf.routing.route_quad(c,port2=nPad2.ports["nPad2-e1"],port1=nPad1.ports["nPad1-e2"],width1=None,width2=None,layer=LAYER.PadMetal)
        gf.routing.route_quad(c,port2=pPad2.ports["pPad2-e2"],port1=pPad1.ports["pPad1-e1"],width1=None,width2=None,layer=LAYER.PadMetal)       
        
        nPadVia.move((nPad2.center[0]-Parameters[ID][Parameters["ParameterName"].index("nPadViaLn")]/2,nPad2.center[1]-Parameters[ID][Parameters["ParameterName"].index("nPadViaWd")]/2))
        pPadVia.move((pPad2.center[0]-Parameters[ID][Parameters["ParameterName"].index("pPadViaLn")]/2,pPad2.center[1]-Parameters[ID][Parameters["ParameterName"].index("pPadViaWd")]/2))
        
        c.add_ports(nPad2.ports)
        c.add_ports(pPad2.ports)
        
        #c.pprint_ports()
        #c.draw_ports()
        
        return c
    @gf.cell
    def DummyPad(Parameters,ID): #Parameters変数はリストで定義。
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        c = gf.Component() #キャンパスを定義
            
        ##各コンポーネント(EAchipを構成している部品）を作成し、各所望のレイヤーと紐づけ
        nPad2 = c.add_ref(BaseParts.nPad2(width=Parameters[ID][Parameters["ParameterName"].index("dPadWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadLn")],layer=LAYER.PadMetal))
        nPadVia = c.add_ref(BaseParts.nPadVia(width=Parameters[ID][Parameters["ParameterName"].index("dPadViaWd")],length=Parameters[ID][Parameters["ParameterName"].index("dPadViaLn")],spacer=Parameters[ID][Parameters["ParameterName"].index("dPadViaSp")],shift=Parameters[ID][Parameters["ParameterName"].index("dPadViaShift")],layer=LAYER.PadVia))
        
        dx=1/2*(Parameters[ID][Parameters["ParameterName"].index("dPadWd")]-Parameters[ID][Parameters["ParameterName"].index("dPadViaWd")])
        dy=1/2*(Parameters[ID][Parameters["ParameterName"].index("dPadLn")]-Parameters[ID][Parameters["ParameterName"].index("dPadViaLn")])
        nPadVia.movex(dx)
        nPadVia.movey(dy)
        
        c.move([-Parameters[ID][Parameters["ParameterName"].index("dPadWd")]/2,-Parameters[ID][Parameters["ParameterName"].index("dPadLn")]/2])
        
        return c




    
# TestCode
# from Layers import LAYER
# import pandas as pd
# FilePath=r"C:\Users\251383\Desktop\PythonPrgrm\Parameters.csv"
# df=pd.DataFrame(pd.read_csv(filepath_or_buffer=FilePath))
# df=df.to_dict(orient="list")
# c=gf.Component()
# c1 = c.add_ref(Devices.LDchip(df,"L200C"))
# c.show()

# from Layers import LAYER
# import pandas as pd
# FilePath=r"C:\Users\251383\Desktop\PythonPrgrm\Parameters.csv"
# df=pd.DataFrame(pd.read_csv(filepath_or_buffer=FilePath))
# df=df.to_dict(orient="list")
# c=gf.Component()
# c1 = c.add_ref(Devices.DummyPad(df,"L200A-GS"))
# c.show()

from Layers import LAYER
import pandas as pd
FilePath=r"C:\Users\251383\Desktop\PythonPrgrm\TEG_InPWGParam.csv"
df=pd.DataFrame(pd.read_csv(filepath_or_buffer=FilePath))
df=df.to_dict(orient="list")
c=gf.Component()
c1 = c.add_ref(Devices.TEG_InPWG(df,"InPWG07L1424"))
        
c.add_ports(c1)
c.pprint_ports()
c.draw_ports()
c.show()

# from Layers import LAYER
# import pandas as pd
# FilePath=r"C:\Users\251383\Desktop\PythonPrgrm\Parameters.csv"
# df=pd.DataFrame(pd.read_csv(filepath_or_buffer=FilePath))
# df=df.to_dict(orient="list")
# c=gf.Component()
# c1 = c.add_ref(BaseParts.InGaAsEtch_Lbend(width=10,TipLn=200,radius=250,BendAngle=20,layer=LAYER.TEST))
# c.show()