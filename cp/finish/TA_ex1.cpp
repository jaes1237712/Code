#include <iostream>
#include <array>
#include <vector>
#include <cmath>
// used[7] = [0,0,...,0], seq[7] = [8,8,8...,8]
int n = 7;
int new_branch(std::vector<bool> used, std::vector<int> seq){
    int sum = 0;
    bool flag = 1; // record if used = [1,1,1...,1]
    int len = used.size();
    for(int i=0;i<len;i++){
        if(used[i])
            continue;
        flag = 0;
        std::vector<bool> used_copy = used;
        used_copy[i] = 1;
        std::vector<int> seq_copy =  seq;
        seq_copy.push_back(i);
        sum += new_branch(used_copy,seq_copy);
    }   
    if(flag){
        for(int i=0;i<len;i++){
            std::cout << seq[i] <<" ";
            sum += std::pow(-1, i+seq[i]+1)*(i+seq[i]+1);
        }
        std::cout << '\n' << sum << '\n';
    }
    return sum;
    // std::vector<int> seq = {1,2,3};
    // int sum = 0;
    // for(int i=0;i<3;i++){
    //     sum += std::pow(-1, i+seq[i])*(i+seq[i]);
    // }
    // std::cout << sum <<'\n';
}

int main(){
    std::vector<bool> used(7,0);
    std::vector<int> seq(0);
    std::cout << new_branch(used,seq) << '\n';
}