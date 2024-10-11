INF = 1<<60
MOD = int(1e9)+7
endl = '\n'

class SegmentTree:
    def __init__(self,data,func): #func là hàm giữa 2 phần tử
        self.data = [0]+data
        self.n = len(data)
        self.st = [INF] * (4*self.n)
        self.lazy = [0] * (4*self.n)
        self.func = func
        self.build()

    def build(self):
        stack = [(1,1,self.n)]
        while stack:
            if isinstance(stack[-1],tuple):
                idx,l,r = stack.pop()
                if l == r:
                    self.st[idx] = self.data[l]
                    continue

                stack.append(idx)
                mid = l+r>>1

                stack.append((idx*2,l,mid))
                stack.append((idx*2+1,mid+1,r))
            else:
                idx = stack.pop()
                self.st[idx] = self.func(self.st[idx*2], self.st[idx*2+1])

    def push(self,idx):
        if self.lazy[idx]:
            self.lazy[idx*2] += self.lazy[idx]
            self.lazy[idx*2+1] += self.lazy[idx]
            self.st[idx*2] += self.lazy[idx]
            self.st[idx*2+1] += self.lazy[idx]
            self.lazy[idx] = 0

    def updatePoint(self,pos,val):
        stack = [(1,1,self.n)]
        while stack:
            if isinstance(stack[-1],tuple):
                idx,l,r = stack.pop()

                if l == r:
                    self.st[idx] = val
                    continue

                stack.append(idx)
                mid = l+r>>1
                if l  <= pos <= mid:
                    stack.append((idx*2,l,mid))
                if mid+1 <= pos <= r:
                    stack.append((idx*2+1,mid+1,r))
            else:
                idx = stack.pop()
                self.st[idx] = self.func(self.st[idx*2],self.st[idx*2+1])

    def updateRange(self,u,v,val):
        stack = [(1,1,self.n)]
        while stack:
            if isinstance(stack[-1],tuple):
                idx,l,r = stack.pop()
                if u <= l and r <= v:
                    self.st[idx] += val
                    self.lazy[idx] += val
                    continue
                
                self.push(idx)
                stack.append(idx)
                mid = l+r>>1
                if not (mid < u or l>v):
                    stack.append((idx*2,l,mid))
                if not (r < u or mid+1>v):
                    stack.append((idx*2+1,mid+1,r))
            else:
                idx = stack.pop()
                self.st[idx] = self.func(self.st[idx*2],self.st[idx*2+1])
                
    def getRange(self,u,v):
        stack = [(1,1,self.n)]
        ans = INF ### ans lấy dựa theo hàm func
        while stack:
            idx,l,r = stack.pop()
            if u <= l and r <= v:
                ans = self.func(ans,self.st[idx])
                continue

            self.push(idx)
            mid = l+r>>1
            if not (mid < u or l > v): stack.append((idx*2,l,mid))
            if not (r < u or mid + 1 > v): stack.append((idx*2+1,mid+1,r))
        
        return ans