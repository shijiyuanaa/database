import abc
import time

ORDER = 3


class BPlusTree:

    def __init__(self):
        self.size = ORDER
        self.root = self.LeafNode(self)

    def search(self, key):
        return self.root.get_value(key)

    def insert(self, key, value):
        self.root.insert(key, value)

    def delete(self, key):
        self.root.delete(key)

    class Node(metaclass=abc.ABCMeta):
        def __init__(self, tree):
            self.keys = []
            self.tree = tree

        @abc.abstractmethod
        def get_value(self, key):
            pass

        @abc.abstractmethod
        def insert(self, key, value):
            pass

        @abc.abstractmethod
        def delete(self, key):
            pass

        @abc.abstractmethod
        def merge(self, bro_node):
            pass

        @abc.abstractmethod
        def split(self):
            pass

        @abc.abstractmethod
        def get_first_leaf_key(self):
            pass

        @abc.abstractmethod
        def is_over_flow(self):
            pass

        @abc.abstractmethod
        def is_under_flow(self):
            pass

    # 非叶结点
    class InternalNode(Node):

        def __init__(self, tree):
            super().__init__(tree)
            self.children = []

        def get_value(self, key):
            return self.get_child(key).get_value(key)

        def get_first_leaf_key(self):
            return self.children[0].get_first_leaf_key()

        def is_over_flow(self):
            return len(self.keys) > ORDER

        def is_under_flow(self):
            return len(self.children) < (ORDER + 1) / 2

        def get_child_left_bro(self, key):  # 返回key对应子结点的左兄弟结点
            i = self.search_index(key)
            if i == 0:
                return None  # 无左兄弟返回None
            return self.children[i - 1]

        def get_child_right_bro(self, key):  # 返回key对应子结点的右兄弟
            i = self.search_index(key)
            if i == ORDER:
                return None  # 无右兄弟返回None
            return self.children[i + 1]

        def insert(self, key, value):
            child = self.get_child(key)
            child.insert(key, value)  # 递归,最终插入到叶结点
            if child.is_over_flow():  # 若已满，需分裂
                split_node = child.split()
                self.insert_child(split_node.get_first_leaf_key(), split_node)  # 分裂出的结点作为child插入到非叶结点
            if self.tree.root.is_over_flow():  # 若根节点已满则分裂(最后一步判断)
                split_node = self.split()
                new_root = BPlusTree.InternalNode(self.tree)
                new_root.keys.append(split_node.get_first_leaf_key())
                new_root.children.append(self)
                new_root.children.append(split_node)
                self.tree.root = new_root

        def delete(self, key):
            child = self.get_child(key)
            child.delete(key)
            if child.is_under_flow():  # 指针少于规定数目，需合并
                left_bro = self.get_child_left_bro(key)
                right_bro = self.get_child_right_bro(key)
                if left_bro:  # 优先向左合并
                    left_bro.merge(child)
                    self.delete_child(key)  # 将被合并的结点删除
                    if left_bro.is_over_flow():  # 若溢出则还需分裂
                        split_node = left_bro.split()
                        self.insert_child(split_node.get_first_leaf_key(), split_node)
                else:  # 没有左兄弟，向右合并
                    child.merge(right_bro)
                    self.delete_child(key)
                    if child.is_over_flow():
                        split_node = child.split()
                        self.insert_child(split_node.get_first_leaf_key(), split_node)

        # 找到对应子结点, (非叶结点一定能找到)
        def get_child(self, key):
            i = self.search_index(key)
            return self.children[i]

        # 分裂当前节点 返回分裂出的新结点
        def split(self):
            new_node = BPlusTree.InternalNode(self.tree)
            _from = len(self.keys) // 2 + 1  # 从中间分裂  //为向下取整
            _to = len(self.keys)
            new_node.keys.extend(self.keys[_from:_to])
            new_node.children.extend(self.children[_from:_to + 1])

            self.keys = self.keys[:_from-1]
            self.children = self.children[:_from]

            return new_node

        # 合并当前节点和bro_node
        def merge(self, bro_node):
            self.keys.append(bro_node.get_first_leaf_key())
            self.keys.extend(bro_node.keys)
            self.children.extend(bro_node.children)

        # 在children中插入子结点
        def insert_child(self, key, child):
            i = self.search_index(key)
            if i < len(self.keys) and self.keys[i] == key:   # key已存在
                self.children.insert(i, child)
            else:
                self.keys.insert(i, key)
                self.children.insert(i+1, child)

        def delete_child(self, key):
            i = self.search_index(key)
            if self.keys[i-1] == key:
                del self.keys[i-1]
                del self.children[i]

        # 获得key对应于keys中的下标
        def search_index(self, key):
            i = 0
            for k in self.keys:
                if k > key:
                    break
                i += 1
            return i

    # 叶结点
    class LeafNode(Node):

        def __init__(self, tree):
            super().__init__(tree)
            self.values = []
            self.next = None   # 指向下一个叶结点

        def insert(self, key, value):
            index = self.search_index(key)
            if index < len(self.keys) and self.keys[index] == key:
                self.values.insert(index, value)
            else:
                self.keys.insert(index, key)
                self.values.insert(index, value)
            if self.tree.root.is_over_flow():  # 第一次分裂
                split_node = self.split()
                new_root = BPlusTree.InternalNode(self.tree)
                new_root.keys.append(split_node.get_first_leaf_key())
                new_root.children.append(self)
                new_root.children.append(split_node)
                self.tree.root = new_root

        def delete(self, key):
            index = self.search_index(key) - 1
            if self.keys[index] == key:
                del self.keys[index]
                del self.values[index]

        def merge(self, bro_node):
            self.keys.extend(bro_node.keys)
            self.values.extend(bro_node.values)
            self.next = bro_node.next

        def split(self):
            new_node = BPlusTree.LeafNode(self.tree)
            _from = (len(self.keys) + 1) // 2
            _to = len(self.keys)
            new_node.keys.extend(self.keys[_from:_to])
            new_node.values.extend(self.values[_from:_to])

            self.keys = self.keys[:_from]
            self.values = self.values[:_from]

            new_node.next = self.next
            self.next = new_node
            return new_node

        def get_first_leaf_key(self):
            return self.keys[0]

        def is_over_flow(self):
            return len(self.values) > ORDER

        def is_under_flow(self):
            return len(self.values) < ORDER / 2

        def get_value(self, key):
            index = self.search_index(key) - 1
            if self.keys[index] == key:
                return self.values[index]
            else:
                return None

        def search_index(self, key):
            index = 0
            for k in self.keys:
                if k > key:
                    break
                index += 1
            return index


def build_tree_from_file():
    a = time.time()
    b_plus_tree = BPlusTree()
    test_search = []

    with open('data', 'rb') as f:
        while True:
            chunk = f.read(4)
            if not chunk:
                break
            key = int.from_bytes(chunk, byteorder='big')
            value = f.read(12).decode(encoding='utf-8')
            b_plus_tree.insert(key, value)

    b = time.time()
    print('建树用时:' + str(b - a) + 's')

    with open('data', 'rb') as f:
        for i in range(100):
            tmp = f.read(4)
            test_search.append(int.from_bytes(tmp, byteorder='big'))  # 待查询列表 100个
            f.read(12)  # skip values

    c = time.time()
    for s in test_search:
        b_plus_tree.search(s)
    d = time.time()
    avg = (d - c) / 100
    print('平均查询用时' + str(avg) + 's')


def test_function():
    b_plus_tree = BPlusTree()
    print('测试功能')
    while True:
        print('1.查找 2.插入 3.删除 0.退出')
        func = input()
        if func == '1':
            print('请输入查询的key')
            key = int(input())
            print(b_plus_tree.search(key))
        elif func == '2':
            print('请输入key value')
            tmp = input().split()
            key = int(tmp[0])
            value = tmp[1]
            b_plus_tree.insert(key, value)
        elif func == '3':
            print('请输入删除的key')
            key = int(input())
            b_plus_tree.delete(key)
        elif func == '0':
            break


if __name__ == '__main__':

    build_tree_from_file()   # 从文件建立B+树索引
    # test_function()  # 测试三种功能







