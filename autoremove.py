# -*- coding: UTF-8 -*-
from qbittorrent import Client
import time

class my_qBittorrent(object):
    def __init__(self,username,password):
        self.torrentHash = []
        self.torrentData = []
        self.client = Client('http://')
        self.client.login(username, password)
        self.getTorrentInfo()
        self.getTorrentSeedTime()
    
    def getTorrentInfo(self):
        self.torrents = self.client.torrents(filter = 'completed')
        for torrent in self.torrents:
            self.torrentHash.append(torrent['hash'])
        return
        
    def getTorrentSeedTime(self):
        for torrentHash in self.torrentHash:
            torrentDict = {'hash':torrentHash,'info':self.client.get_torrent(torrentHash)}
            self.torrentData.append(torrentDict)
        return
    
    def deleteTorrentPerm(self,torrentHash):
        self.client.delete_permanently(torrentHash)
        return
    
    def getSingleTorrentInfo(self,torrentHash):
        torrentDict = {'hash':torrentHash,'info':self.client.get_torrent(torrentHash)}
        return torrentDict
    
    def seedTimeFilter(self,torrentHash,seedTime=1):
        seedTimeConv = seedTime*3600
        torrentInfo = self.getSingleTorrentInfo(torrentHash)
        seedingTime = torrentInfo['info']['seeding_time']
        if seedingTime > seedTimeConv:
            return True
        return False
    
    def trackerFilter(self,torrentHash,tracker = None):
        #add the tracker exception
        if tracker:
            rawInfo = self.client.get_torrent_trackers(torrentHash)
            torrentTracker = rawInfo[0]['url']
            if torrentTracker.find(tracker):
                return True
        return False
    
    def addedTimeFilter(self,torrentHash,addedTime = 1):
        #default day
        torrentInfo = self.getSingleTorrentInfo(torrentHash)
        addedTimeConv = addedTime*24*3600
        timeElapsed = torrentInfo['info']['time_elapsed']
        if timeElapsed > addedTimeConv:
            return True
        return False
    
    def integratedFilter(self,torrentHash):
        
        
        
testClient = my_qBittorrent('','')
testClient.Filter(seedTime=1)        
            
        
        