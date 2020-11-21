import cv2


class VideoCamera(object):

    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def mainframe(self):
        cd = self.os.getcwd()

        file_path = self.os.path.join(cd,"static/file.txt")

        print("File path is",file_path)

        f = open(file_path,"w")

        vid=cv2.VideoCapture(0)

        vid.set(3,640)

        vid.set(4,480)

        readcode=[]

        while True:

            success,read=self.vid.read()

            codes=self.decode(read)

            for code in codes:

                data = code.data.decode("utf-8")

                print(code)

                print(data)

                # create array of a polygon dimensions

                f.write(data)

                f.write("\n")

                p1 = self.num.array([code.polygon], self.num.int32)

                p1 = p1.reshape((-1 ,1 ,2))

                cv2.polylines(read, [p1], True, (255 ,0 , 0) ,2)

                # take rect attribute
                p2=code.rect

                # put text over a qrcode during scanning
                font = cv2.FONT_HERSHEY_PLAIN

                cv2.putText(read, data , (p2[0], p2[1]), font , 0.9, (255, 0, 0), 2)

                readcode.append(data)

            cv2.imshow("SCAN",read)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


        f.close()

        # vid.release()
        # cv2.destroyAllWindows()

        ret, jpeg = cv2.imencode('.jpg', vid)

        return jpeg.tobytes()





def gen(camera):
    while True:
        frame = camera.mainframe()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
