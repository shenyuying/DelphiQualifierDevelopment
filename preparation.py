#!/usr/bin/python
# encoding=utf8

import os

def getLines(var_configfile):
    getLines_configfile = var_configfile
    f = open(getLines_configfile, "r")
    lines = f.readlines()
    return lines

configFile = 'verification_dev.txt'
sourcePath = "qualifier/"
destPath = "/home/ubuntu/"

lines = getLines(configFile)
for line in lines:
    line = line.strip()
    # print(line)
    val = line.split(',')
    ipAddress = val[2]
    packageName = val[3]
    tDirectory = val[4]
    pathList = [sourcePath,packageName]
    head = ''
    for path in pathList:
        head = os.path.join(head,path)
    print "head is %s" % head
    if os.path.isfile(head):
        command_line = 'scp {var_sourcePath}{var_packageName} ubuntu@{var_ipAddress}:{var_destPath}'
        formatedcmd = command_line.format(var_sourcePath=sourcePath, var_packageName=packageName, var_ipAddress=ipAddress, var_destPath=destPath)
        print "formatedcmd is %s" % formatedcmd