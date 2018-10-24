class FileSystem(object):

    def __init__(self):
        self.fs = {}
    
    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        curr = self.fs
        frags = path_split(path)
        for frag in frags:
            if frag not in curr:
                curr[frag] = {}
            curr = curr[frag]
            if type(curr) == unicode:
                return [frags[-1]]
        return sorted(curr.keys())

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        curr = self.fs
        frags = path_split(path)
        for frag in frags:
            if frag not in curr:
                curr[frag] = {}
            curr = curr[frag]
        

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        curr = self.fs
        frags = path_split(filePath)
        for frag in frags[:-1]:
            if frag not in curr:
                curr[frag] = {}
            curr = curr[frag]
        file_name = frags[-1]
        if file_name not in curr:
            curr[file_name] = ''
        curr[file_name] += content
        

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        curr = self.fs
        frags = path_split(filePath)
        for frag in frags[:-1]:
            if frag not in curr:
                curr[frag] = {}
            curr = curr[frag]
        file_name = frags[-1]
        return curr[file_name]

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
