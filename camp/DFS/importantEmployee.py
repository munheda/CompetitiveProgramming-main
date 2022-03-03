"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
        

"""
from collections import defaultdict


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emp_dict= defaultdict(Employee)
        for emp in employees:
            emp_dict[emp.id] = emp
        
            
            
        def dfs(id):
            
            current=emp_dict[id].importance
            
            if not emp_dict[id].subordinates:
                return emp_dict[id].importance
            
            else:
                for sub in emp_dict[id].subordinates:
                    current += dfs(sub) 
                
                return current
        
        return dfs(id)
            
            
            
            
            
        
    
            