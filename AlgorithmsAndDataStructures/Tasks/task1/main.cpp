#include <iostream>
#include <vector>
using namespace std;

class Node
{
public:
    int mother;
    int first_son;
    int last_son;
    int brother;
    int in_time;
    int out_time;

    explicit Node(int mother) {
        this->mother = mother;
        this->first_son = 0;
        this->last_son = 0;
        this->brother = 0;
        this->in_time = 0;
        this->out_time = 0;
    }

    Node(){;}

};
class Tree {
    private:
        int q;
        Node root;
        int number_of_nodes;
        Node* table_of_nodes;

    public:

        Tree(int number_of_nodes, int questions) {
            this->q = questions;
            root = Node(0);
            root.out_time = number_of_nodes;
            this->number_of_nodes = number_of_nodes;
            this->table_of_nodes = new Node[number_of_nodes + 1];
            this->table_of_nodes[1] = root;
            this->fill_tab();
            this->dfs2();
        }

        ~Tree() {
            delete[] table_of_nodes;
        }

        void addNode(int index, const Node& newNode) {
            table_of_nodes[index] = newNode;
        }

        [[nodiscard]] int getNumberOfNodes() const {
            return number_of_nodes;
        }

        Node& getNode(int index) {
            return table_of_nodes[index];
        }

    void fill_tab(){
        for (int i = 2; i <= getNumberOfNodes(); i++){
            Node pom = Node(0);
            addNode(i,pom);
        }

        for(int i = 2; i <= getNumberOfNodes(); i++){
            int mother_index;
            cin >> mother_index;
            table_of_nodes[i].mother = mother_index;
            if (table_of_nodes[mother_index].first_son == 0){
                table_of_nodes[mother_index].first_son = i;
                table_of_nodes[mother_index].last_son = i;
            }
            else{
                int brother_ind = table_of_nodes[mother_index].last_son;
                table_of_nodes[brother_ind].brother = i;
                table_of_nodes[mother_index].last_son = i;
            }
        }
    }

    void dfs2()
    {
        int time = 0;
        Node* actual_node = &getNode(1);
        while (time < getNumberOfNodes()){

            if (actual_node->first_son != 0){
                time++;
                int son = actual_node->first_son;
                actual_node->first_son = 0;
                actual_node = &getNode(son);
                actual_node->in_time = time;
            }
            else if (actual_node->brother != 0){

                int brother = actual_node->brother;
                actual_node->out_time = time;
                actual_node->brother = 0;
                actual_node = &getNode(brother);
                time++;
                actual_node->in_time = time;
            }
            else if (actual_node->mother != 0){
                int mother = actual_node->mother;
                actual_node->mother = 0;
                actual_node->out_time = time;
                actual_node = &getNode(mother);
            }
            else{
                break;
            }
        }
    }

    void answer_questions(){
        int n1, n2;
        for (int i = 0; i < q - 1; i++){

            cin >> n1 >> n2;
            if (getNode(n1).in_time < getNode(n2).in_time
            && getNode(n1).out_time >= getNode(n2).out_time){
                cout << "TAK"<<endl;
            }
            else{
                cout << "NIE"<<endl;
            }
        }
        cin >> n1 >> n2;

        if (getNode(n1).in_time < getNode(n2).in_time
        && getNode(n1).out_time >= getNode(n2).out_time){
            cout << "TAK";
        }
        else{
            cout << "NIE";
        }
    }

};

void execute_task() {
    int n, q;
    cin >> n >>q;
    Tree tree(n, q);
    tree.answer_questions();
}

int main() {
    execute_task();
    return 0;
}
