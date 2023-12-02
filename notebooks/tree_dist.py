# %%
import networkx
import obonet

# %%
onto_path = "http://purl.obolibrary.org/obo/cl/cl-basic.obo"
graph = obonet.read_obo(onto_path)
id_to_name = {id_: data.get('name') for id_, data in graph.nodes(data=True)}
name_to_id = {data['name']: id_  for id_, data in graph.nodes(data=True) if 'name' in data}

# %%
graph = graph.reverse()

# %%
nodes = list(graph.nodes)

# %%
i = "CL:0000000"
k = "CL:0000118"
lca = networkx.lowest_common_ancestor(graph, i,k)
i_dist = networkx.shortest_path_length(graph, lca, i)
k_dist = networkx.shortest_path_length(graph, lca, k)
print(k_dist)

# %%
for k in graph.nodes:
    print(type(k))
    break

# %%
def calc_distance(input_tuple,):
    graph, i = input_tuple
    res = {}
    for k in graph.nodes:
        try:
            lca = networkx.lowest_common_ancestor(graph, i, k)
            if lca:
                i_dist = networkx.shortest_path_length(graph, lca, i)
                k_dist = networkx.shortest_path_length(graph, lca, k)
                res[k] = i_dist + k_dist
        except:
            pass
    print("node: ", i, "finishing")
    return i, res


# %%
import multiprocessing as mp

pool = mp.Pool(mp.cpu_count())

nodes = list(graph.nodes)

# nodes = nodes[100:120]


results = pool.map(calc_distance, [[graph, i] for i in nodes])

# %%


# %%
res_dict = {}
for i, res in results:
    res_dict[i] = res

# %%
# dump to json
import json
with open('lca_distances.json', 'w') as fp:
    json.dump(res_dict, fp)


