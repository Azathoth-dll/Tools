import os

def Trans(file, output_dir, isSubFile, doKeepSubPath):
        try:
            print("Processing {}".format({file}))
            _input = file
            _output = output_dir + file[:-4] + ".mp3"
            print("Input: [{}]".format(_input))
            if isSubFile:
                if doKeepSubPath:
                    subFileDir = os.path.dirname(_input)
                    if not os.path.exists(output_dir + subFileDir):
                        os.mkdir(output_dir + subFileDir)
                else:
                    _output = output_dir + os.path.basename(_input)[:-4] + ".mp3"

            print("Output: [{}]".format(_output))
            if not os.path.exists(_output):
                os.system('ffmpeg -i "{}" -q:a 0 -map a "{}"'.format(file, _output))
        except:
            print("Process {} with exception".format({file}))

def __main__():
    # 获取当前脚本路径
    current_path = os.path.dirname(__file__)
    print("Start process files in directory [{}]".format(current_path))

    # 寻找output文件夹、否则创建文件夹
    output_dir = current_path + "\\output\\"
    print("Output files will be saved in directory [{}]".format(output_dir))

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # 询问用户是否需要保留子文件路径
    keepSubPath = ""
    doKeepSubPath = True

    while True:
        keepSubPath = input("Keep sub-file path? press y/Y to agree and n/N to disagree")
        if keepSubPath == "y" or keepSubPath == "Y":
            doKeepSubPath = True
            break
        elif keepSubPath == "n" or keepSubPath == "N":
            doKeepSubPath = False
            break


    # 获取当前路径及子路径下所有视频文件
    all_files_and_dir = os.listdir(current_path)
    for file in all_files_and_dir:
        if os.path.isfile(file) and file.endswith('.mp4') or file.endswith('.MP4'):
            Trans(file, output_dir, False, False)
        elif os.path.isdir(file):
            for _path in os.listdir(".\\" + file):
                _file = file + "\\" + _path
                if os.path.isfile(_file) and _file.endswith('.mp4') or _file.endswith('.MP4'):
                    Trans(_file, output_dir, True, doKeepSubPath)

    a = input("Do Task mp4 -> mp3 finish")

__main__()
