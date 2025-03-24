#include <gtest/gtest.h>
#include <vector>
#include <map>
#include "helpers.hpp"
#include <algorithm>

bool comp(int a, int b) {
    return a > b;
}

template <typename T>
void Helpers<T>::printThis(T val){
    std::cout << val << std::endl;
}

template <typename T>
void Helpers<T>::COMPARE_VECS(std::vector<T>& vec1, std::vector<T>& vec2){
    EXPECT_EQ(vec1.size(), vec2.size());
    sort(vec1.begin(), vec1.end(), comp);
    sort(vec2.begin(), vec2.end(), comp);
    for (int i = 0; i<vec1.size(); i++){
        EXPECT_EQ(vec1[i], vec2[i]);
    }
}

template class Helpers<int>;