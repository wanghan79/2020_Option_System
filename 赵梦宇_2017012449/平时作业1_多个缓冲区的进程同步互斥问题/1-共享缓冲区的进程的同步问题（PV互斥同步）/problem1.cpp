/*
    使用 PV 信号量互斥同步解决如下问题：
    设某计算进程 CP 和 打印进程 IOP 共用一个大小为 N 的缓冲区 T
    CP 进程负责不断地计算数据并送入缓冲区 T 中
    IOP 进程负责不断地从缓冲区 T 中取出数据去打印
*/
// 不妨设缓冲区 T 的大小为 N，初始缓冲区为空
Semaphore s_empty = N；// 表示缓冲区是否为空，初始值为 N
Semaphore s_full = 0; // 表示缓冲区是否为满，初始值为 0
// 显然保证 s_empty + s_full 恒等于 N
Semaphore mutex = 1; // 缓冲区互斥信号量
void Computing_Process() {
    while(Computing_Finish() == false) {
        Compute();
        P(s_empty);
        P(mutex);
        Send_To_Buffer();
        V(mutex);
        V(s_full);
    }
}
void Input_Output_Process() {
    while(Output_Finish() == false) {
        P(s_full);
        P(mutex);
        Get_From_Buffer();
        V(mutex);
        V(s_empty);
        Output();
    }
}