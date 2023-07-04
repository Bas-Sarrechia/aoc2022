class Tree:
    def __init__(self, height: int):
        self.height = height
        self.visible = False
        self.scenic_score = 0

    def score(self, left_trees: [], right_trees: [], top_trees: [], bottom_trees: []):
        if self.visible:
            left_score = 0
            right_score = 0
            top_score = 0
            bottom_score = 0
            if (len(left_trees) == 0 or len(right_trees) == 0 or len(bottom_trees) == 0 or len(top_trees) == 0):
                return
            for idx in range(len(left_trees)):
                if self.height > left_trees[::-1][idx].height:
                    left_score += 1
                if left_trees[::-1][idx].height >= self.height:
                    left_score += 1
                    break
            for idx in range(len(right_trees)):
                if self.height > right_trees[idx].height:
                    right_score += 1
                if right_trees[idx].height >= self.height:
                    right_score += 1
                    break
            for idx in range(len(top_trees)):
                if self.height > top_trees[::-1][idx].height:
                    top_score += 1
                if top_trees[::-1][idx].height >= self.height:
                    top_score += 1
                    break
            for idx in range(len(bottom_trees)):
                if self.height > bottom_trees[idx].height:
                    bottom_score += 1
                if bottom_trees[idx].height >= self.height:
                    bottom_score += 1
                    break
            self.scenic_score = left_score * right_score * top_score * bottom_score

    def is_visible(self, left_trees: [], right_trees: [], top_trees: [], bottom_trees: []):
        if len(left_trees) == 0 or len(top_trees) == 0 or len(right_trees) == 0 or len(bottom_trees) == 0:
            self.visible = True
            return
        if self.height > max([tree.height for tree in left_trees]):
            self.visible = True
            return
        if self.height > max([tree.height for tree in right_trees]):
            self.visible = True
            return
        if self.height > max([tree.height for tree in top_trees]):
            self.visible = True
            return
        if self.height > max([tree.height for tree in bottom_trees]):
            self.visible = True
            return


with open('day8.data', 'r') as file:
    data = file.read()
    grid_split = data.split('\n')
    grid = [[Tree(int(tree)) for tree in trees] for trees in grid_split]

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            row_element = grid[row]
            tree = row_element[col]
            left = row_element[:col:]
            right = row_element[col + 1::]
            col_element = [el[col] for el in grid]
            top = col_element[:row:]
            bottom = col_element[row + 1::]
            tree.is_visible(left, right, top, bottom)
            tree.score(left, right, top, bottom)
    visibility_grid = [[item.visible for item in sub] for sub in grid]
    score_grid = [[item.scenic_score for item in sub] for sub in grid]
    print(sum(sum(visibility_grid, [])))
    print(max(sum(score_grid, [])))
