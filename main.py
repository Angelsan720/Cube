import cv2
import numpy as np

colors = {
    'red'       :[135,  74,  81],
    'blue'      :[147, 183, 217],
    'green'     :[ 42, 165,  25],
    'orange'    :[232, 125,  13],
    'yellow'    :[255, 232, 159],
    'white'     :[234, 231, 240],
    'black'     :[ 28,  26,  29],
    1           :[135,  74,  81],
    2           :[147, 183, 217],
    3           :[ 42, 165,  25],
    4           :[232, 125,  13],
    5           :[255, 232, 159],
    6           :[234, 231, 240],
}

class Cube:
    def __init__(self, size=3, corder = [520,440]) -> None:
        self.size = size
        self.side1 = []
        self.side2 = []
        self.side3 = []
        self.side4 = []
        self.side5 = []
        self.side6 = []
        self.DrawCorner = corder
        #           side6
        #   side2   side3   side4   side5
        #           side1

    def initialize(self, monoColor = 0):
        self.side1 = []
        self.side2 = []
        self.side3 = []
        self.side4 = []
        self.side5 = []
        self.side6 = []
        for i in range(self.size):
            self.side1.append([])
            self.side2.append([])
            self.side3.append([])
            self.side4.append([])
            self.side5.append([])
            self.side6.append([])
            
            for j in range(self.size):
                if monoColor:
                    self.side1[-1].append(colors['white'])
                    self.side2[-1].append(colors['white'])
                    self.side3[-1].append(colors['white'])
                    self.side4[-1].append(colors['white'])
                    self.side5[-1].append(colors['white'])
                    self.side6[-1].append(colors['white'])
                else:
                    self.side1[-1].append(colors['white'])
                    self.side2[-1].append(colors['green'])
                    self.side3[-1].append(colors['blue'])
                    self.side4[-1].append(colors['red'])
                    self.side5[-1].append(colors['yellow'])
                    self.side6[-1].append(colors['orange'])
        return self
    def Draw(self):
        DrawMagicSquares(self)

cam_port = 0
cam = cv2.VideoCapture(cam_port)
cv2.namedWindow('Cube')
cv2.namedWindow('Main')
obj = Cube(3)
obj = obj.initialize()
def DrawCubeTup(img, tup, corner1, corner2, overlay = False):
    x1, y1 = corner1
    x2, y2 = corner2
    yLen = y2-y1
    xLen = x2-x1
    yStep = yLen//len(tup)
    xStep = xLen//len(tup[0])
    
    for index, row in enumerate(tup):
        for index2, color in enumerate(row):
            img = DrawSquare(img,
                            color=color, 
                            corner1=(x1 + (xStep * index    ), y1 + (yStep * index2    )),
                            corner2=(x1 + (xStep * (index+1)), y1 + (yStep * (index2+1))),
                            infill=False,
                            thickness=3)
    
    
    
    
    return img

def DrawMagicSquares(cube:Cube):
    
    img = np.zeros((800,1000,3))
    tup = cube.side1
    img = DrawCubeTup(img, tup, (300,500),(500,700))
    tup = cube.side2
    img = DrawCubeTup(img, tup, (100,300),(300,500))
    tup = cube.side3
    img = DrawCubeTup(img, tup, (300,300),(500,500))
    tup = cube.side4
    img = DrawCubeTup(img, tup, (500,300),(700,500))
    tup = cube.side5
    img = DrawCubeTup(img, tup, (700,300),(900,500))
    tup = cube.side6
    img = DrawCubeTup(img, tup, (300,100),(500,300))
    
    return img
   
    
def DrawSquare(img, color, corner1, corner2, thickness=3, isClosed=True, infill=False):
    x1,y1 = corner1
    x2,y2 = corner2
    pts = np.array([
        [x1,y1],
        [x2,y1],
        [x2,y2],
        [x1,y2],
    ])
    pts = pts.reshape((-1, 1, 2))
    return DrawPolygon(img, color, pts, thickness=thickness, isClosed=isClosed, inFill=infill)
def DrawPolygon(img, color, pts, thickness=3, isClosed=True, inFill=False):
    if inFill:
        img = cv2.fillPoly(img, [pts], color)
    else:
        img = cv2.polylines(img, [pts],isClosed, color, thickness)
    return img

    

while True:
    result, image = cam.read()
    image_to_display = image
    green = [0,255,0]
    red = [255,0,0]
    blue = [0,0,255]
    purple = [255,0,255]
    #image_to_display = DrawSquare(image_to_display,color = colors['green'], corner1=[120,40], corner2=[520,440], thickness=3)
    #img = DrawMagicSquares(obj)
  
    key = cv2.waitKey(0)
    if key == 27:
        break
    if key == 32:
        pass#getCoords(image)
