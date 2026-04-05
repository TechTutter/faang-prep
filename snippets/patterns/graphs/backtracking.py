def all_paths(graph, node, target, path, result):
    path.append(node)
    if node == target:
        result.append(list(path))
    else:
        for neighbor in graph[node]:
            if neighbor not in path:  # avoid revisiting within current path
                all_paths(graph, neighbor, target, path, result)
    path.pop()  # backtrack — unlike DFS, visited is unmarked on exit
