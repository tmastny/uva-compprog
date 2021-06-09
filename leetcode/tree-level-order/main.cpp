#include <vector>
#include <map>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr) return vector<vector<int>>{};

        vector<vector<int>> log;
        deque<TreeNode*> q;

        q.push_back(root);
        while (!q.empty()) {

            vector<int> vals;
            int n = q.size();
            for (int i = 0; i < n; i++) {
                TreeNode* node = q.front();
                q.pop_front();

                vals.push_back(node->val);
                if (node->left != nullptr) q.push_back(node->left);
                if (node->right != nullptr) q.push_back(node->right);
            }

            log.push_back(vals);
        }


        return log;
    }
};
