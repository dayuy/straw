import getpass
import os
import queue

### 广度优先搜索：在给定路径下，搜索文件或子目录，子目录需要进一步搜索其下的文件和子目录，直到没有更多的子目录
# param path: 给定目录的路径
def bfs_dir(path):
  if not os.path.isdir(path):
    return
  que = queue.Queue()
  visited = set()
  for p in os.listdir(path):
    bfs_path = path + os.sep + p
    if os.path.isdir(bfs_path):
      que.put(bfs_path)
      visited.add(bfs_path)
      print('文件夹\t', bfs_path)
    else:
      print('文件夹\t', bfs_path)
    
  while not que.empty():
    cur_path = que.get()
    if len(os.listdir(cur_path)) == 0:
      continue
    for p in os.listdir(cur_path):
      bfs_path = cur_path + os.sep + p
      if bfs_path in visited:
        continue
      if os.path.isdir(bfs_path):
        que.put(bfs_path)
        visited.add(bfs_path)
        print('文件夹\t', bfs_path)
      else:
        print('文件\t', bfs_path)

if __name__ == '__main__':
  dir_path = ''
  user = getpass.getuser()
  if os.name == 'posix':
    dir_path = '/Users/' + user + '/Desktop/GeekTime/MathematicProgrammer'
  elif os.name == 'nt':
    dir_path = '\\Users\\' + user + '\\Desktop\\GeekTime\\MathematicProgrammer'
  print('dir_path', dir_path, os.path.isdir(dir_path))
  bfs_dir(dir_path)