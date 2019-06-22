import cv2
from datetime import datetime


def capture_camera(mirror=True, size=None):
    """Capture video from camera"""
    # カメラをキャプチャする
    cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号

    # retは画像を取得成功フラグ
    ret, frame = cap.read()

    # 鏡のように映るか否か
    if mirror is True:
        frame = frame[:,::-1]

    # フレームをリサイズ
    # sizeは例えば(800, 600)
    if size is not None and len(size) == 2:
        frame = cv2.resize(frame, size)

    # フレームを表示する
    # cv2.imshow('camera capture', frame)
    date = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = "./img/" + date + ".png"
    cv2.imwrite(path, frame)  # ファイル保存

    # キャプチャを解放する
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_camera()
