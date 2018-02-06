from csi7.download_local_agent import downloadLocalAgent
from stat import *
from unittest import TestCase

class TestCsi7Execution(TestCase):
    def test_clickondownloadlink(self):
        first = downloadLocalAgent.test_download(None)
    def test_downloadthefile(self):
         second = downloadLocalAgent.test_downloadversion(None)
    def test_getfilesize(self):
         third = downloadLocalAgent.test_downloadFileLocation(None)

