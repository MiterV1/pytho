#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pip3 install ExifRead

"""
import os
import re
import shutil
import time
import logging
import exifread

import tkinter
from tkinter import filedialog
from tkinter import messagebox

class Application(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def OnOpenBtn(self):
        askdirectoryVal = filedialog.askdirectory()
        self.entryShow.delete('0', 'end')
        self.entryShow.insert('0', askdirectoryVal)

    def OnStartBtn(self):
        directoryVal = self.entryShow.get().replace('/', '\\')
        pictures = self.__walkDir(directoryVal)
        picsDateInfo = self.__getPicsExifInfo(pictures)
        self.__moveFiles(directoryVal, picsDateInfo)
        tkinter.messagebox.showinfo("Message", "OK!!!")

    def createWidgets(self):
        self.textPath = tkinter.Label(self, text="path：")
        self.textPath.grid(row=0, column=0)

        self.entryShow = tkinter.Entry(self, width='50')
        self.entryShow.grid(row=0, column=1, columnspan=2)

        self.btnOpen = tkinter.Button(self, text="open", width='10', command=self.OnOpenBtn)
        self.btnOpen.grid(row=0, column=3)

        self.btnStart = tkinter.Button(self, text="start", width='10', command=self.OnStartBtn)
        self.btnStart.grid(row=1, column=3)

        radioSetVal = [("YYYY/MM", 1), ("YYYY/MM/DD", 2)]
        self.radioBtnVal = tkinter.IntVar()
        self.radioBtnVal.set(1)
        for txt, val in radioSetVal:
            tkinter.Radiobutton(self, text=txt, value=val, variable=self.radioBtnVal).grid(row=1, column=val)

    def __walkDir(self, directory):
        '''
        walking directory to find out pictures
        :param directory:
        :return: list of pictures with full directry and filename
        '''
        pictures = []
        reJpgs = '.+\.jpg$'
        rePngs = '.+\.png$'

        for root, _, files in os.walk(directory):
            for name in files:
                if re.match(reJpgs, name, re.IGNORECASE) is not None or \
                        re.match(rePngs, name, re.IGNORECASE) is not None:
                    file = os.path.join(root.replace('/', '\\'), name)
                    pictures.append(file)
                    logging.info('collecting file: {}'.format(file))

        return pictures

    def __getPicsExifInfo(self, files):
        '''
        read out exif information in specific file
        :param files: filename list
        :return: dict of date information
        '''
        picsDateInfo = {}

        for picture in files:
            # Read exif date information
            with open(picture, 'rb') as fd:
                pictureDate = ""
                pictureExifInfo = exifread.process_file(fd)
                try:
                    if pictureExifInfo.__contains__('EXIF DateTimeOriginal'):
                        tempStr = pictureExifInfo['EXIF DateTimeOriginal']
                        pictureDate = str(tempStr).replace(':', '-')[:10]
                    elif pictureExifInfo.__contains__('EXIF DateTimeDigitized'):
                        tempStr = pictureExifInfo['EXIF DateTimeDigitized']
                        pictureDate = str(tempStr).replace(':', '-')[:10]
                    else:
                        logging.info('No EXIF DateTimeOriginal: {}'.format(picture))
                except:
                    logging.warnning("Can't do exif.process {}".format(picture))

            # A picture hasn't date information, so according to file time
            # to set up a date to it
            if pictureDate == '':
                tc = time.localtime(os.path.getctime(picture))
                pictureDate = time.strftime('%Y-%m-%d', tc)

            # set up dict { date : [filename] }
            if not picsDateInfo.__contains__(pictureDate):
                picsDateInfo[pictureDate] = [picture]
            else:
                picsDateInfo[pictureDate].append(picture)

            logging.info('classifying file: {}'.format(picture))

        return picsDateInfo

    def __moveFiles(self, rootDir, picsDateInfo):
        '''
        do move files
        :param rootDir: root directory that user choosen
        :param picsDateInfo: dict of date information
        '''
        for k, v in picsDateInfo.items():
            YYYY = k[:4]
            MM = k[:7]
            DD = k

            if self.radioBtnVal.get() == 1:
                # radioBtnVal is ("YYYY/MM", 1)
                directory = os.path.join(rootDir, YYYY, MM)
            else:
                # radioBtnVal is ("YYYY/MM/DD", 2)
                directory = os.path.join(rootDir, YYYY, MM, DD)

            if not os.path.exists(directory):
                os.makedirs(directory)

            for f in v:
                newDir = os.path.join(directory, os.path.basename(f))
                if not f == newDir:
                    shutil.move(f, newDir)
                    logging.info('moving file: {}'.format(newDir))


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("Pictures Classifier")
    root.resizable(0, 0)

    logging.basicConfig(filename="do.log", level=logging.INFO, filemode='w',
                        format="%(asctime)s:%(levelname)s:%(message)s")

    app = Application(master=root)
    app.mainloop()
