import time


def partition(arr, low, high):
    i = low-1
    pivot = arr[high][0]
    for j in range(low, high):
        if arr[j][0] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


# 快排
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


# 划分为小文件并排序
def split_file():

    with open('data', 'rb') as fr:
        for i in range(block_number):
            tmp = []
            for j in range(int(part_file_size/16)):  # 每个记录16字节
                attr_a = fr.read(4)
                attr_b = fr.read(12)
                tmp.append((attr_a, attr_b))
            quick_sort(tmp, 0, len(tmp)-1)
            with open(prefix+str(i), 'wb') as fw:
                for item in tmp:
                    fw.write(item[0])
                    fw.write(item[1])


# 找到待排序块中最小的块的下表
def get_min(in_buffer):
    min_key = 0xFFFFFFFF.to_bytes(4, byteorder='big')
    index = -1
    for i in range(len(in_buffer)):
        if len(in_buffer[i]) > 0:  # 在还没读完的文件块中找最小的key
            tmp = in_buffer[i][:4]
            if tmp <= min_key:
                index = i
                min_key = tmp
    return index


def merge_sort():
    file_list = []   # 保存文件指针
    in_buffer = []   # 模拟输入缓冲区
    out_buffer = b''  # 保存字节型记录，模拟输出缓冲区
    for i in range(block_number):
        file_list.append(open((prefix + str(i)), 'rb'))  # 依次打开待归并文件
    with open('merge_sort/result', 'wb') as fw:
        for fr in file_list:
            in_buffer.append(fr.read(page_size))   # 保存从每个子集合中读的块
        while True:    # 进行归并排序
            index = get_min(in_buffer)   # 找到最小key值
            if index == -1:  # 说明所有文件都已读完，终止排序
                fw.write(out_buffer)
                break
            key_value = in_buffer[index][:16]  # 取最小key对应的记录
            in_buffer[index] = in_buffer[index][16:]  # 从输入缓冲区中删除
            out_buffer += key_value   # 放到输出缓冲区
            if len(out_buffer) >= page_size:  # 若输出缓冲区已有一个页大小，则输出到文件
                fw.write(out_buffer)
                out_buffer = b''   # 输出缓冲区清空
            if len(in_buffer[index]) == 0:  # 若一个文件的文件块已排序完
                page = file_list[index].read(page_size)
                if len(page) > 0:  # 若该文件还有剩余，则再读一个pagesize
                    in_buffer[index] = page
                else:  # 否则说明该文件已读完，不处理
                    pass

    for i in range(block_number):
        file_list[i].close()   # 关闭文件


if __name__ == '__main__':
    memory_size = 1024 * 1024  # 内存大小
    page_size = 4096  # 内存页大小
    # page_number = memory_size / page_size = 256页 1M内存有256页 子集合数<256 且每个子集合小于1024*1024B即可
    file_size = 16 * (10 ** 6)
    block_number = 16
    part_file_size = int(file_size / block_number)
    prefix = 'merge_sort/part_'

    '''
    文件大小为 16 * 10^6 B
    分为16个子集合，每个子集合 10^6B < 1MB, 且 16 < 256
    '''
    a = time.time()
    split_file()
    b = time.time()
    print('第一趟用时 ' + str(b-a) + 's')

    merge_sort()
    c = time.time()
    print('第二趟用时 ' + str(c-a) + 's')
