#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/2/20
# @Author  : chujian521
# @File    : logger.py

import os
import sys
sys.path.append(r"..") 
import logging
import functools

from utils.ansistrm import ColorizingStreamHandler
from config import LOGGER_LEVEL

logger_initialized = {}

#参考paddleocr的日志模块: https://github.com/PaddlePaddle/PaddleOCR

@functools.lru_cache()
def get_logger(name='root', log_file=None, log_level=10):
    """Initialize and get a logger by name.
    If the logger has not been initialized, this method will initialize the
    logger by adding one or two handlers, otherwise the initialized logger will
    be directly returned. During initialization, a StreamHandler will always be
    added. If `log_file` is specified a FileHandler will also be added.
    Args:
        name (str): Logger name.
        log_file (str | None): The log filename. If specified, a FileHandler
            will be added to the logger.
        log_level (int): The logger level. Note that only the process of
            rank 0 is affected, and other processes will set the level to
            "Error" thus be silent most of the time.
    Returns:
        logging.Logger: The expected logger.
    """
    log_level = LOGGER_LEVEL
    logger = logging.getLogger(name)
    if name in logger_initialized:
        return logger
    for logger_name in logger_initialized:
        if name.startswith(logger_name):
            return logger

    formatter = logging.Formatter(
        '[%(asctime)s] %(name)s %(levelname)s: %(message)s',
        datefmt="%Y/%m/%d %H:%M:%S")

    stream_handler = ColorizingStreamHandler(sys.stdout)
    stream_handler.level_map[logging.getLevelName("*")] = (None, "cyan", False)
    stream_handler.level_map[logging.getLevelName("+")] = (None, "green", False)
    stream_handler.level_map[logging.getLevelName("-")] = (None, "red", False)
    stream_handler.level_map[logging.getLevelName("!")] = (None, "yellow", False)

    #stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    if log_file is not None:
        log_file_folder = os.path.split(log_file)[0]
        os.makedirs(log_file_folder, exist_ok=True)
        file_handler = logging.FileHandler(log_file, 'a')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        logger.setLevel(log_level)
        
    logger_initialized[name] = True
    return logger