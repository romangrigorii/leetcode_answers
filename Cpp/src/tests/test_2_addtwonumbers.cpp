#include <gtest/gtest.h>
#include "../headers.hpp"
#include "helpers.hpp"
#include <vector>
#include <map>

using namespace::std;


TEST(TestSuite, AddTwoNumbers) { 
    Helpers<int> helpers;
    std::vector<int> vec1 = {2,4,3};
    std::vector<int> vec2 = {5,6,4};
    std::vector<int> vec_out = {7,0,8};
    ListNode * node1 = vecToLN(vec1);
    ListNode * node2 = vecToLN(vec2);
    auto node_res = addTwoNumbers(node1, node2);
    auto node_exp = vecToLN(vec_out);
    helpers.COMPARE_LN(node_res, node_exp);
}