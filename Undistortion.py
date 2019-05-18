import numpy as np
import cv2
import glob

# load calig file
mtx = np.loadtxt('./rms.csv', delimiter=',')
print(mtx)

# load dist file
dist = np.loadtxt('./K.csv', delimiter=',')
print(dist)

img = cv2.imread('./img/IMG_8033.JPG')
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calib_result.png',dst)

"""
# undistort
mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)

# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.png',dst)
"""