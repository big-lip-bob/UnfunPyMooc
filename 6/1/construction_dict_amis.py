def construction_dict_amis(connexions):
    amis = {}
    for (ami1, ami2) in connexions:
        amis[ami1] = amis.get(ami1, set()) | {ami2}
        amis[ami2] = amis.get(ami2, set())
    return amis