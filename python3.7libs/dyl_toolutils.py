import hou


def buildAttribNameMenu(node, input_num=0, attribClass='point'):
    try:
        node_input = node.inputs()[input_num]
        geo = node_input.geometry()
        if attribClass == 'point':
            attribname = geo.pointAttribs()
        elif attribClass == 'prim':
            attribname = geo.primAttribs()
        elif attribClass == 'vertex':
            attribname = geo.vertexAttribs()
        elif attribClass == 'detail':
            attribname = geo.globalAttribs()
        else:
            return []

        if attribname is None:
            return []

        menu = []
        for i in attribname:
            name = i.name()
            menu += [name]
            menu += [name]
    except:
        return []

    return menu


def buildGroupNameMenu(node, input_num=0, group='point'):
    try:
        node_input = node.inputs()[input_num]
        geo = node_input.geometry()
        if group == 'point':
            groupname = geo.pointGroups()
        elif group == 'prim':
            groupname = geo.primGroups()
        elif group == 'vertex':
            groupname = geo.vertexGroups()
        elif group == 'detail':
            groupname = geo.globalGroups()
        else:
            return []

        if groupname is None:
            return []

        menu = []
        for i in groupname:
            name = i.name()
            menu += [name]
            menu += [name]
    except:
        return []

    return menu


def buildAttribValMenu(node, input_num=0, attribClass='point', attribName=''):
    try:
        node_input = node.inputs()[input_num]
        geo = node_input.geometry()
        if attribClass == 'point':
            attribVal = geo.pointStringAttribValues(attribName)
        elif attribClass == 'prim':
            attribVal = geo.primStringAttribValues(attribName)
        elif attribClass == 'vertex':
            attribVal = geo.vertexStringAttribValues(attribName)
        else:
            return []

        if attribVal is None:
            return []
        menu = []
        for i in attribVal:
            menu.append(i)
            menu.append(i)

    except:
        return []

    return menu
