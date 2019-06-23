import cv2
from datetime import datetime


CAP_DIR = "./img/"


def capture_camera(file_path, size=None):
    cap = cv2.VideoCapture(0)#-1)  # カメラのデバイス番号
    cap.read()  # 初回のキャプチャは失敗する.
    ret, frame = cap.read()  # retは画像を取得成功フラグ

    # 鏡のように映るか否か
    # if mirror is True:
    #     frame = frame[:, ::-1]

    # フレームをリサイズ
    # sizeは例えば(800, 600)
    if size is not None and len(size) == 2:
        frame = cv2.resize(frame, size)

    # フレームを表示する
    # cv2.imshow('camera capture', frame)
    cv2.imwrite(file_path, frame)  # ファイル保存

    # キャプチャを解放する
    cap.release()
    cv2.destroyAllWindows()

    record_capture(file_path)


def record_capture(cap_file_path):
    cap_list_path = CAP_DIR+"cap.list"

    with open(cap_list_path, mode='a') as f:
        f.write(cap_file_path+"\n")


if __name__ == "__main__":
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = CAP_DIR + date + ".png"
    capture_camera(file_path)
