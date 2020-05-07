/*
    使用 PV 信号量互斥同步解决如下问题：
    有 N 个哲学家，他们的生活方式是交替地进行思考和进餐
    哲学家们共用一张圆桌，分别坐在周围的 N 张椅子上，在圆桌上有 N 个碗和五支筷子
    平时哲学家进行思考，饥饿时便试图取其左、右最靠近他的筷子，只有在他拿到两支筷子时才能进餐
    该哲学家进餐完毕后，放下左右两只筷子又继续思考。
*/
class Monitor { // 根据问题创建管程
private:
    // 注意： 哲学家 id 依次为 [0, N - 1]
    Philosopher_State state[N]; // 哲学家的状态有 Thinking, Eating, Hungry, 初始值为 Thinking
    Semaphore mutex; // 互斥信号量，初始值为 1
    Semaphore s[N]; // 每个哲学家一个信号量，初始值为 0
    Monitor() { // 构造函数，负责整个管程的初始化工作
        for(int i = 0; i < N; ++i) {
            state[i] = Thinking;
            s[i] = 0;
        }
        mutex = 1;
    }
    // 测试序号为 x 的哲学家能否进餐，当且仅当哲学家 x 为饥饿状态且他的左右邻居都没有占用筷子（即不是进餐状态）
    bool Can_Eat(int x) {
        if(state[x] == Hungry && state[Left_Neighbor(x)] != Eating && state[Right_Neighbor(x)] != Eating) {
            return true; 
        }   
        return false;
    }
    // 令哲学家 x 进餐
    void Eat(int x) {
        state[x] = Eating;
        // 成功进餐，该哲学家不必进入等待队列
        V(s[x]); 
    }
public:
    // 根据需求，外界只需要使用管程中的下面两个函数
    // 其他成员变量与成员函数使用 private 保护起来

    void Try_To_Eat(int x) {   
        // 该哲学家进入饥饿状态
        state[x] = Hungry;
        // 如果该哲学家可以进餐
        P(mutex);
        if(Can_Eat(x)) { 
            // 则令他进餐
            Eat(x);
        } 
        V(mutex);   
        // 如果不能成功进餐，则进入等待队列排队
        P(s[x]); 
    }   
    void Eating_Finish(int x){   
        // 进餐完毕，转为思考状态
        state[x] = Thinking;
        P(mutex);
        // 如果该哲学家的右邻居能够进餐
        if(Can_Eat(Left_Neighbor(x))) { 
            // 则令他进餐
            Eat(Left_Neighbor(x));
        }
        // 如果该哲学家的右邻居能够进餐
        if(Can_Eat(Right_Neighbor(x))) { 
            // 则令他进餐
            Eat(Right_Neighbor(x));
        }
        V(mutex);   
    }

} M;
void Philosopher(int id) {
    while(true) {
        Think(id);
        M.Try_To_Eat(id);
        // 该哲学家进餐（注意，该函数不是 Monitor 中的 Eat 函数）
        Eat(id);
        M.Eating_Finish(id);
    }
}
