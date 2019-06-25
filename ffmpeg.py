import subprocess


def conv_mp4_mp3(mp4_file, mp3_file):
    try:
        ffmpeg_cmd = "ffmpeg -y -i {} -ab 192 {}".format(mp4_file, mp3_file)
        res = subprocess.check_call(ffmpeg_cmd.split())
        return res
    except Exception as e:
        print("Error.", e)


if __name__ == "__main__":
    conv_mp4_mp3("/home/bosq/Desktop/20190624210621_voice_1561379777.mp4", "./20190624210621_voice_1561379777.mp3")
