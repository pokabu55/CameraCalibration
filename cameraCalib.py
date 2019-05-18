import numpy as np
import cv2
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# 水平方向の交点数
horCpNum = 10
# 垂直方向の交点数
verCpNum = 7

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((horCpNum*verCpNum,3), np.float32)
objp[:,:2] = np.mgrid[0:verCpNum,0:horCpNum].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('./data/*.JPG')
imgIndex = 0

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    found, corners = cv2.findChessboardCorners(gray, (horCpNum,verCpNum),None)

    # If found, add object points, image points (after refining them)
    if found == True:
        print("{0}:finding corners : success.".format(imgIndex))
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (horCpNum,verCpNum), corners2, found)

        print('corners shape:', corners.shape)
        width = img.shape[1]
        height = img.shape[0]
        resized_img = cv2.resize(img,dsize=(width//4, height//4))
        cv2.imshow('img',resized_img)
        cv2.waitKey(500)
    else:
        print("{0}:finding corners : failed.".format(imgIndex))

    imgIndex += 1

cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

print('reprojection error:\n', ret) # 交点検出に成功した場合は True、そうでない場合は False
print('camera matrix:\n', mtx)      # カメラ行列 (内部パラメータ)
print('distortion:\n', dist)        # 歪み係数 (内部パラメータ)
print('rvecs:\n', rvecs[0].shape)   # 回転ベクトル (外部パラメータ)
print('tvecs:\n', tvecs[0].shape)   # 平行移動成分 (外部パラメータ)

# 計算結果を保存
np.savetxt("rms.csv", mtx, delimiter =',',fmt="%0.14f")
np.savetxt("K.csv", dist, delimiter =',',fmt="%0.14f")