# Last updated: 7/12/2025, 11:47:37 PM
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_cook = {s:True for s in supplies}
        recipe_index = {r:i for i, r in enumerate(recipes)}

        def dfs(r):
            if r in can_cook:
                return can_cook[r]
            if r not in recipe_index:
                return False

            can_cook[r] = False
            for nei in ingredients[recipe_index[r]]:
                if not dfs(nei):
                    return False
            can_cook[r] = True
            return can_cook[r]
        

        return [r for r in recipes if dfs(r)]