import logging

logging.basicConfig(
    level=logging.ERROR,  # 设置日志输出格式
    filemode="w",  # 文件的写入格式，w为重新写入文件，默认是追加
    format="%(asctime)s - %(name)s - %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s",  # 日志输出的格式
    # -8表示占位符，让输出左对齐，输出长度都为8位
    datefmt="%Y-%m-%d %H:%M:%S",  # 时间输出的格式
)
