
class Node:
    incoming_edge:int=0
    outgoing_edge:int=0

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        node_data = dict()
        for match in matches:
            if node_data.get(match[0],-1)!=-1:
                c = node_data[match[0]]
                c.outgoing_edge = c.outgoing_edge + 1
            else:
                a = Node()
                a.outgoing_edge = 1
                node_data[match[0]] = a

            if node_data.get(match[1],-1)!=-1:
                c = node_data[match[1]]
                c.incoming_edge = c.incoming_edge + 1
            else:
                b = Node()
                b.incoming_edge = 1
                node_data[match[1]] = b

        no_loss, one_loss = [],[]
        for node,data in node_data.items():
            if data.incoming_edge==0:
                no_loss.append(node)
            if data.incoming_edge==1:
                one_loss.append(node)
            
        return [sorted(no_loss),sorted(one_loss)]
            
