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
class Solution {
public:       
    bool isSymmetric(TreeNode* root) { 
        return dfs(root->left,root->right);
    }
    
    
    
    
    bool dfs(TreeNode* Node1, TreeNode* Node2){
            
        
        
            if (Node1 == NULL){
                return Node2 == NULL;
            }
            
            if (Node2 == NULL){
                return Node1== NULL;
            }
            
            if (Node1->val != Node2->val){
                
                return false;
            }
            
            
            
            return dfs(Node1->left, Node2->right) && dfs(Node1->right, Node2->left);
        }
        
};