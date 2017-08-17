# -*-encoding:utf-8-*-
import os
import time


class Log:
    LOG_PATH = "./Log/log.txt"
    CHATLOG = "./Log/chat.txt"

    def __init__(self):
        if not os.path.exists("./Log/"):
            os.mkdir("./Log/")

        if not os.path.exists(self.LOG_PATH):
            with open(self.LOG_PATH, "w") as fw:
                pass

    def WriteLog(self, e):
        with open(self.LOG_PATH, "a") as fw:
            msg_error = "ERROR:{0}time: {1}{0}lineno: {2}{0}errorinfo: {3}{4}".format(
                "\n",
                time.ctime(),
                e.__traceback__.tb_lineno,
                e.args[0],
                "\n\n\n"
            )
            fw.write(msg_error)
    
    def WriteChat(self, msg_time,msg_from,msg_group,msg_type,msg_content,msg_url):
        if not msg_type == "Note":
            with open(self.CHATLOG, "a") as fc:
                msg_chat = "Message:{0}Time: {1}{0}Who: {2}{0}Group: {3}{0}Type: {4}{0}Content: {5}{0}Url: {6}{0}{0}".format(
                    "\n",
                    msg_time,
                    msg_from,
                    msg_group,
                    msg_type,
                    msg_content,
                    msg_url
                )
                fc.write(msg_chat)
