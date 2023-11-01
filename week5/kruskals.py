def Kruskal(Wlist):
    (edges, component, TE) = ([], {}, [])
    for u in Wlist.keys():
        edges.extend([d,u,v] for (v,d) in Wlist[u])
        component[u] = u
    edges.sort()

    for (d,u,v) in edges:
        if component[u] != component[v]:
            TE.append([u, v])
            c = component[u]
            for v in Wlist.keys():
                if component[v] == c:
                    component[w] = component[v]

    return TE