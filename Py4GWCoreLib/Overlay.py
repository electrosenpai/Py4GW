import PyOverlay
from typing import Tuple
from .Py4GWcorelib import Utils

class Overlay:
    def __init__(self):
        self.overlay_instance = PyOverlay.Overlay()

    def IsMouseClicked(self):
        return self.overlay_instance.IsMouseClicked(0)

    def GetMouseCoords(self) -> Tuple[float, float]:
        mouse_point = self.overlay_instance.GetMouseCoords()
        return mouse_point.x, mouse_point.y

    def GetMouseWorldPos(self):
        world_pos = self.overlay_instance.GetMouseWorldPos()
        return world_pos.x, world_pos.y, world_pos.z

    @staticmethod
    def WorldToScreen(x,y,z=0.0):
        if z == 0.0:
            z = Overlay.FindZ(x, y)

        screen_pos = PyOverlay.Overlay().WorldToScreen(x, y, z)
        return screen_pos.x, screen_pos.y

    @staticmethod
    def FindZ (x, y, z=0):
        """Find The altitude of the ground at the given x,y coordinates based on Pathing Maps"""
        return PyOverlay.Overlay().FindZ(x, y, z)

    def RefreshDrawList(self):
        self.overlay_instance.RefreshDrawList()

    def BeginDraw(self, name: str = "", x: int = 0, y: int = 0, width: int = 0, height: int = 0) -> None:
        if not name:
            self.overlay_instance.BeginDraw()
        elif width > 0 and height > 0:
            self.overlay_instance.BeginDraw(name, x, y, width, height)
        else:
            self.overlay_instance.BeginDraw(name)

    def EndDraw(self):
        self.overlay_instance.EndDraw()

    def DrawLine(self, x1, y1, x2, y2, color=0xFFFFFFFF, thickness=1.0):
        pos1 = PyOverlay.Point2D(Utils.SafeInt(x1), Utils.SafeInt(y1))
        pos2 = PyOverlay.Point2D(Utils.SafeInt(x2), Utils.SafeInt(y2))
        self.overlay_instance.DrawLine(pos1, pos2, color, thickness)  # Pass color and thickness

    def DrawLine3D(self, x1, y1, z1, x2, y2, z2, color=0xFFFFFFFF, thickness=1.0):
        pos1 = PyOverlay.Point3D(x1, y1, z1)
        pos2 = PyOverlay.Point3D(x2, y2, z2)
        self.overlay_instance.DrawLine3D(pos1, pos2, color, thickness)
        
    def DrawTriangle(self, x1, y1, x2, y2, x3, y3, color=0xFFFFFFFF, thickness=1.0):
        p1 = PyOverlay.Point2D(Utils.SafeInt(x1), Utils.SafeInt(y1))
        p2 = PyOverlay.Point2D(Utils.SafeInt(x2), Utils.SafeInt(y2))
        p3 = PyOverlay.Point2D(Utils.SafeInt(x3), Utils.SafeInt(y3))
        self.overlay_instance.DrawTriangle(p1, p2, p3, color, thickness)
        
    def DrawTriangle3D(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, color=0xFFFFFFFF, thickness=1.0):
        p1 = PyOverlay.Point3D(x1, y1, z1)
        p2 = PyOverlay.Point3D(x2, y2, z2)
        p3 = PyOverlay.Point3D(x3, y3, z3)
        self.overlay_instance.DrawTriangle3D(p1, p2, p3, color, thickness)
        
    def DrawTriangleFilled(self, x1, y1, x2, y2, x3, y3, color=0xFFFFFFFF):
        p1 = PyOverlay.Point2D(Utils.SafeInt(x1), Utils.SafeInt(y1))
        p2 = PyOverlay.Point2D(Utils.SafeInt(x2), Utils.SafeInt(y2))
        p3 = PyOverlay.Point2D(Utils.SafeInt(x3), Utils.SafeInt(y3))
        self.overlay_instance.DrawTriangleFilled(p1, p2, p3, color)
        
    def DrawTriangleFilled3D(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, color=0xFFFFFFFF):
        p1 = PyOverlay.Point3D(x1, y1, z1)
        p2 = PyOverlay.Point3D(x2, y2, z2)
        p3 = PyOverlay.Point3D(x3, y3, z3)
        self.overlay_instance.DrawTriangleFilled3D(p1, p2, p3, color)
     
    def DrawQuad(self, x1, y1, x2, y2, x3, y3, x4, y4, color=0xFFFFFFFF, thickness=1.0):
        p1 = PyOverlay.Point2D(Utils.SafeInt(x1), Utils.SafeInt(y1))
        p2 = PyOverlay.Point2D(Utils.SafeInt(x2), Utils.SafeInt(y2))
        p3 = PyOverlay.Point2D(Utils.SafeInt(x3), Utils.SafeInt(y3))
        p4 = PyOverlay.Point2D(Utils.SafeInt(x4), Utils.SafeInt(y4))
        self.overlay_instance.DrawQuad(p1, p2, p3, p4, color, thickness)   
    
    def DrawQuad3D(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, color=0xFFFFFFFF, thickness=1.0):
        p1 = PyOverlay.Point3D(x1, y1, z1)
        p2 = PyOverlay.Point3D(x2, y2, z2)
        p3 = PyOverlay.Point3D(x3, y3, z3)
        p4 = PyOverlay.Point3D(x4, y4, z4)
        self.overlay_instance.DrawQuad3D(p1, p2, p3, p4, color, thickness)
        
    def DrawQuadFilled(self, x1, y1, x2, y2, x3, y3, x4, y4, color=0xFFFFFFFF):
        p1 = PyOverlay.Point2D(Utils.SafeInt(x1), Utils.SafeInt(y1))
        p2 = PyOverlay.Point2D(Utils.SafeInt(x2), Utils.SafeInt(y2))
        p3 = PyOverlay.Point2D(Utils.SafeInt(x3), Utils.SafeInt(y3))
        p4 = PyOverlay.Point2D(Utils.SafeInt(x4), Utils.SafeInt(y4))
        self.overlay_instance.DrawQuadFilled(p1, p2, p3, p4, color)
        
    def DrawQuadFilled3D(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, color=0xFFFFFFFF):
        p1 = PyOverlay.Point3D(x1, y1, z1)
        p2 = PyOverlay.Point3D(x2, y2, z2)
        p3 = PyOverlay.Point3D(x3, y3, z3)
        p4 = PyOverlay.Point3D(x4, y4, z4)
        self.overlay_instance.DrawQuadFilled3D(p1, p2, p3, p4, color)

    def DrawPoly(self, center_x, center_y, radius, color=0xFFFFFFFF, numsegments =32, thickness=1.0):
        center = PyOverlay.Point2D(Utils.SafeInt(center_x), Utils.SafeInt(center_y))
        self.overlay_instance.DrawPoly(center, radius, color, numsegments, thickness)

    def DrawPoly3D(self, center_x, center_y, center_z, radius, color=0xFFFFFFFF,numsegments =32, thickness=1.0, autoz = True ):
        center = PyOverlay.Point3D(center_x, center_y, center_z)
        self.overlay_instance.DrawPoly3D(center, radius, color, numsegments, thickness)
        
    def DrawPolyFilled(self, center_x, center_y, radius, color=0xFFFFFFFF, numsegments =32):
        center = PyOverlay.Point2D(Utils.SafeInt(center_x), Utils.SafeInt(center_y))
        self.overlay_instance.DrawPolyFilled(center, radius, color, numsegments)
        
    def DrawPolyFilled3D(self, center_x, center_y, center_z, radius, color=0xFFFFFFFF,numsegments =32):
        center = PyOverlay.Point3D(center_x, center_y, center_z)
        self.overlay_instance.DrawPolyFilled3D(center, radius, color, numsegments)
        
    def DrawCubeOutline(self, x, y, z, size, color=0xFFFFFFFF):
        center = PyOverlay.Point3D(x, y, z)
        self.overlay_instance.DrawCubeOutline(center, size, color)
        
    def DrawCubeFilled(self, x, y, z, size, color=0xFFFFFFFF):
        center = PyOverlay.Point3D(x, y, z)
        self.overlay_instance.DrawCubeFilled(center, size, color)

    def DrawText(self, x, y, text, color=0xFFFFFFFF, centered = True, scale=1.0):
        pos = PyOverlay.Point2D(Utils.SafeInt(x), Utils.SafeInt(y))
        self.overlay_instance.DrawText(pos, text, color, centered, scale)

    def DrawText3D(self, x, y, z, text, color=0xFFFFFFFF, autoZ= True, centered = True, scale=1.0):
        pos = PyOverlay.Point3D(x, y, z)
        self.overlay_instance.DrawText3D(pos, text, color, autoZ, centered,scale)

    def GetDisplaySize(self):
        return self.overlay_instance.GetDisplaySize()
        
    def PushClipRect(self, x, y, x2, y2):
        self.overlay_instance.PushClipRect(x, y, x2, y2)
        
    def PopClipRect(self):
        self.overlay_instance.PopClipRect()

    