#include <vector>
#include <map>
#include <iostream>

using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
/*
This is breadth-first search.
- I used visited to maintain the levels,
  but I can do that better by fixing the queue
  length at the start of the loop.

  The visited is more for graph structures, where a node
  can be pointed to be multiple nodes. In that case,
  if a node is already *visited*, there already exists a path
  that is less than or equal to that distance.

*/
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr) return vector<vector<int>>{};

        vector<vector<int>> log;

        deque<TreeNode*> q;

        visited.insert(root);
        q.push_back(root);
        while (!q.empty()) {

            vector<int> vals;
            while (!q.empty() && visited.find(q.front()) != visited.end()) {
                TreeNode* node = q.front();
                q.pop_front();

                cout << node->val << endl;
                vals.push_back(node->val);
                if (node->left != nullptr) q.push_back(node->left);
                if (node->right != nullptr) q.push_back(node->right);
            }
            log.push_back(vals);

            for (auto n : q) {
                visited.insert(n);
            }
        }


        return log;
    }
};
