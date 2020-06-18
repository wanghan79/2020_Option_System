/*
    使用 PV 信号量互斥同步解决如下问题：
    桌上有一个空盘，最多允许存放 N 只水果。
    爸爸可向盘中放一个苹果或者放一个桔子。
    儿子专等吃盘中的桔子，女儿专等吃盘子中的苹果。
    试用 PV 操作实现爸爸、儿子、女儿三个并发进程的同步
*/
// 不妨设盘子的大小为 N，初始盘子为空
Semaphore s_empty = N；// 表示盘子是否为空，初始值为 N
Semaphore s_orange = 0; // 表示当前盘子中的桔子数量，初始值为 0
Semaphore s_apple = 0; // 表示当前盘子中的苹果数量，初始值为 0
// 显然保证 s_empty + s_orange + s_apple 恒等于 N
Semaphore mutex = 1; // 缓冲区互斥信号量
void Father() {
    while(true) {
        Fruit f = Buy_Fruit();
        P(s_empty);
        P(mutex);
        Put_On_Plate(f);
        V(mutex);
        if(f == orange) {
            V(s_orange);
        } else {
            V(s_apple);
        }
    }
}
void Son() {
    while(true) {
        P(s_orange);
        P(mutex);
        Get_Orange_From_Plate();
        V(mutex);
        V(s_empty);
        Eat_Orange();
    }
}
void Daughter() {
    while(true) {
        P(s_apple);
        P(mutex);
        Get_Apple_From_Plate();
        V(mutex);
        V(s_empty);
        Eat_Apple();
    }
}