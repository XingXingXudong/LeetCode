#include <iostream>
#include <vector>

using namespace std
;

class MyCircularQueue {
private:
    vector<int> data;
    int head, tail, length;
    bool flag;
public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k) {
        length = k;
        data = vector<int>(k);
        head = tail = -1;
        flag = true;
    }

    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value) {
        if (! isFull()) {
            tail = (tail + 1) % length;
            if (tail == 0) {
                flag = false;
            }
            data[tail] = value;
            return true;
        } else {
            return false;
        }
    }

    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue() {
        if (! isEmpty()){
            head = (head + 1) % length;
            if (head == 0) {
                flag = true;
            }
            return true;
        } else {
            return false;
        }
    }

    /** Get the front item from the queue. */
    int Front() {
        if (isEmpty()) {
            return -1;
        }
        return data[head+1];
    }

    /** Get the last item from the queue. */
    int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return data[tail];
    }

    /** Checks whether the circular queue is empty or not. */
    bool isEmpty() {
        if ((head == -1 && tail == -1) || (flag && (head == tail))){
            return true;
        } else {
            return false;
        }
    }

    /** Checks whether the circular queue is full or not. */
    bool isFull() {
        if (head == -1 && tail == length-1) {
            return true;
        } else if (!flag && (head==tail)) {
            return true;
        } else {
            return false;
        }
    }
};

class MyCircularQueue1 {
private:
    vector<int> v;
    int start = 0, len = 0;

public:
    MyCircularQueue1(int k): v(k) {}

    bool enQueue(int value) {
        if (isFull()) {
            return false;
        }
        v[(start+len++) % v.size()] = value;
        return true;
    }

    bool deQueue() {
        if (isEmpty()) {
            return false;
        }
        start = (start + 1) % v.size();
        --len;
        return true;
    }

    int Front() {
        if (isEmpty()) {
            return -1;
        }
        return v[start];
    }

    int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return v[(start + len - 1) % v.size()];
    }

    bool isFull() {
        return len == v.size();
    }

    bool isEmpty() {
        return !len;
    }


};

int main() {
    std::cout << "Hello, World!" << std::endl;
    //Your MyCircularQueue object will be instantiated and called as such:
    MyCircularQueue1* obj = new MyCircularQueue1(3);
    bool param_1 = obj->enQueue(1);
    cout << param_1 << endl;
    param_1 = obj->enQueue(2);
    cout << param_1 << endl;
    param_1 = obj->enQueue(3);
    cout << param_1 << endl;
    param_1 = obj->enQueue(4);
    cout << param_1 << endl;
    int param_4 = obj->Rear();
    cout << param_4 << endl;
    param_1 = obj->isFull();
    cout << param_1 << endl;
    bool param_2 = obj->deQueue();
    cout << param_2 << endl;
//    int param_3 = obj->Front();
//    cout << param_3 << endl;
    param_1 = obj->enQueue(4);
    cout << param_1 << endl;
    param_4 = obj->Rear();
    cout << param_4 << endl;
    return 0;
}