import cv2,time

def Capture():
    static_frame = None
    video = cv2.VideoCapture(0)
    while True:
        check,frame1 = video.read()        
        #time.sleep(3)
        #frame = cv2.resize(frame,(1080,720))
        frame = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
        frame = cv2.GaussianBlur(frame,(21,21),0)
        if static_frame is None:
            static_frame = frame
        
        diff = cv2.absdiff(static_frame,frame)
        thr_diff = cv2.threshold(diff,30,255,cv2.THRESH_BINARY)[1]
        thr_diff = cv2.dilate(thr_diff,None ,iterations=2)
        (cnts,_) = cv2.findContours(thr_diff.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for cont in cnts:
            if cv2.contourArea(cont)<5000:
                continue
            else:

                (x,y,w,h) = cv2.boundingRect(cont)
                frame1 = cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),3)

        """cv2.imshow("capturing",frame)
        cv2.imshow("diff",diff)
        cv2.imshow("Thres",thr_diff)"""
        cv2.imshow("Color",frame1)
        q = cv2.waitKey(1)
        
        if q == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()