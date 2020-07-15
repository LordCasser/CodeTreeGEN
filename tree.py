#####
#Author: LordCasser
#Date: 2020-07-15 09:18:01
#LastEditTime: 2020-07-15 16:44:35
#LastEditors: LordCasser
#Description: 
#####

class Node(object):
    def __init__(self,value,level):
        self.value = value
        self.childNodes = None
        self.level = int(level)
        # self.parentNode = parent
    def addChildNode(self,node):
        if self.childNodes == None:
            self.childNodes = [node]
        else:
            self.childNodes.append(node)
class Tree(object):
    def __init__(self,file):
        with open(file) as f :
            self.content = f.readlines()
            self.root = []
    def parser(self):
        currentNode = None
        currentNodeParentStack = []
        currentHead = '- '
        for line in self.content:
            currentHeadLen = len(currentHead)
            if (line.split('- ')[0]+'- ')[-currentHeadLen:] == currentHead: 
                if  (line.split('- ')[0]+'- ')[:-currentHeadLen] == '  ':#下一个是分支
                    newNode = Node(line[currentHeadLen+2:],(currentHeadLen+2)/2)
                    currentNode.addChildNode(newNode)

                    currentNodeParent = currentNode
                    currentNode = newNode
                    currentNodeParentStack.append(currentNodeParent)
                    currentHead = '  '+currentHead 
                else: #下一个是平级
                    
                    if currentNodeParentStack != []:
                        currentNodeParent = currentNodeParentStack[-1]
                        currentNode  = currentNodeParent
                        newNode = Node(line[currentHeadLen:],currentHeadLen/2)
                        currentNode.addChildNode(newNode)
                        currentNode = newNode
                    else:
                        
                        currentHead = '- '
                        currentHeadLen = 2
                        currentNodeParent = None
                        newNode = Node(line[currentHeadLen:],1)
                        currentNode = newNode
                        self.root.append(newNode)
                        

            else: #下一个是更高层 
                popcounter =(currentHeadLen / 2) - len((line.split('- ')[0]+'- '))/2
                if popcounter >0:
                    for i in range(int(popcounter)):
                        if currentNodeParentStack != []:
                            currentNodeParentStack.pop()
                            currentHead = currentHead[2:]
                            
                if currentNodeParentStack == []: #最高节点
                    currentHead = '- '
                    currentHeadLen = 2
                    currentNodeParent = None
                    newNode = Node(line[currentHeadLen:],1)
                    currentNode = newNode
                    self.root.append(newNode)
                    
                else:
                    currentHeadLen = len(currentHead)
                    newNode = Node(line[currentHeadLen:],currentHeadLen/2)
                    currentNode.addChildNode(newNode)
                    currentNode = newNode

            
                    
    def printer(self):
        self.result = []
        for i in self.root:
            self.looper(i)
        with open('out.txt','w') as r:
            r.writelines(self.result)
    def looper(self,node:Node):
        payload = (node.level-1)*'│   '+ '+----' + node.value
        self.result.append(payload)
        if node.childNodes != None:
            for i in node.childNodes:
                self.looper(i)
        
    #     try:
    #         for i in range(len(node.childNodes)):
    #             if i == (len(node.childNodes)-1): #当当前节点不是其平级的最后一个节点时
    #                 payload = (node.level-1)*'│   '+ '├── ' + node.value    
    #             else:
    #                 payload = (node.level-1)*'│   '+ '└── ' + node.value 
    #             self.result.append(payload)
    #     except:
    #         pass
        
            
        

if __name__ == "__main__":
    t = Tree('1.md')
    t.parser()
    t.printer()
    