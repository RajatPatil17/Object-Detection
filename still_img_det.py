import cv2
classNames=[]
classFile= 'coco.names'
thres =0.5

with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/300)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


img = cv2.imread("german shepherd.jpeg")
classIds, confs, bbox = net.detect(img, confThreshold=thres)    
    
if len(classIds) !=0:
    for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
        cv2.rectangle(img, box, color=(0,255,0), thickness=3)
        cv2.putText(img, classNames[classId-1].upper(),(box[0]+10, box[1]+30),
        cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

cv2.imshow("output",img)
cv2.waitKey(0)
