**数组**由于是紧凑连续存储,可以随机访问，通过索引快速找到对应元素，而且相对节约存储空间。但正因为连续存储，内存空间必须一次性分配够，所以说数组如果要扩容，需要重新分配一块更大的空间，再把数据全部复制过去，时间复杂度 O(N)；而且你如果想在数组中间进行插入和删除，每次必须搬移后面的所有数据以保持连续，时间复杂度 O(N)。

**链表**因为元素不连续，而是靠指针指向下一个元素的位置，所以不存在数组的扩容问题；如果知道某一元素的前驱和后驱，操作指针即可删除该元素或者插入新元素，时间复杂度 O(1)。但是正因为存储空间不连续，你无法根据一个索引算出对应元素的地址，所以不能随机访问；而且由于每个元素必须存储指向前后元素位置的指针，会消耗相对更多的储存空间

只能用于元素有序的情况

Redis, LevelDB

Reference: 

<https://www.zhihu.com/question/20202931>

<https://redisbook.readthedocs.io/en/latest/internal-datastruct/skiplist.html>

<https://leetcode-cn.com/problems/lru-cache/>

![Screen Shot 2021-02-08 at 11.35.47 PM.png](resources/61300B500036CA62D86588E08E3313D4.png)

![Screen Shot 2021-02-08 at 11.36.12 PM.png](resources/5E47FA25C66D51C48BF849834E0D4BB0.png)