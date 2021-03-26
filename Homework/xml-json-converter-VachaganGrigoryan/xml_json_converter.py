import json
import argparse
from uuid import uuid4
from pathlib import Path
from typing import Union, Any, List


class Node:

    def __init__(self, name: str, value: str = None, parent=None, metadata: dict = None, children: list = None):
        if parent is not None:
            parent.children.append(self)
        self.name = name
        self.value = value
        self.parent = parent
        self.metadata = metadata or {}
        self.children = children or []

    def add_child(self, node):
        if not isinstance(node, Node):
            raise TypeError(f"tree root type {type(node)} is not supported: Expected type <class 'Node'>")

        self.children.append(node)

    def __str__(self):
        return f'{self.name} --> {self.value}'


class Tree:

    def __init__(self, root: Node, tree_type: str):
        if not isinstance(root, Node):
            raise TypeError(f"tree root type {type(root)} is not supported: Expected type <class 'Node'>")

        if tree_type not in {'xml', 'json'}:
            raise TypeError(f"tree_type type '{tree_type}' is incorrect: Expected type 'xml' or 'json'")

        self.root = root
        self.tree_type = tree_type

    def xml_to_json(self):
        def _gen_json(node: Node):
            if node.value and not node.children:
                return node.value
            node_len = len(node.children)
            if node_len == 1 or any([node.children[i - 1].name != node.children[i].name for i in range(node_len)]):
                return {child.name: _gen_json(child) for child in node.children}
            return [_gen_json(child) for child in node.children]

        return _gen_json(self.root)

    def json_to_xml(self):
        def _gen_xml(node: Node, tab: int):
            metadata_xml = "".join([f' {k}="{v}"' for k, v in node.metadata.items()])
            if node.value and not node.children:
                return f"<{node.name}{metadata_xml}>{node.value}</{node.name}>"
            return f"<{node.name}{metadata_xml}>{'    ' * tab}{_add_children(node.children, tab)}\n{'    ' * (tab - 1)}</{node.name}>"

        def _add_children(children: List[Node], tab: int):
            children_xml = ''
            for child in children:
                children_xml = f"{children_xml}\n{'    ' * tab}{_gen_xml(child, tab + 1)}"
            return children_xml

        return _gen_xml(self.root, 1)

    def write(self, path: str):
        with open(Path(path), mode='w') as file:
            file.write(self.result())

    def result(self):
        if self.tree_type == 'json':
            return self.json_to_xml()
        else:
            return json.dumps(self.xml_to_json(), indent=4)

    @classmethod
    def build_tree(cls, data: Union[str, dict, list]):
        def json__build_node(root: Node, name: str, value: Any, metadata: dict = None):
            node = Node(name, value, parent=root, metadata=metadata)
            if isinstance(value, (list, dict)):
                json__build_nodes(value, node)

        def json__build_nodes(data: Union[list, dict], root: Node):
            if isinstance(data, list):
                for data_element in data:
                    json__build_node(root, 'item', data_element, {'id': uuid4().time_low})
            else:
                for name, value in data.items():
                    json__build_node(root, name, value)

        def xml__build_nodes(data: Union[list, dict], root: Node):
            for tag in data.split(">")[1:]:
                if "</" in tag:
                    value = tag.split("</")[0].strip()
                    if value:
                        root.value = value
                    root = root.parent
                elif "<" in tag:
                    name = tag.strip().replace("<", "").split(" ", 1)
                    root = Node(name[0], parent=root)

        root = Node('data')

        if isinstance(data, str):
            tree_type = 'xml'
            xml__build_nodes(data, root)
        elif isinstance(data, (dict, list)):
            tree_type = 'json'
            json__build_nodes(data, root)
        else:
            raise TypeError(f"data type {type(data)} is incorrect: Expected type <xml as 'str'> or <json as 'dict'>")

        return cls(root, tree_type)


def run():
    parser = argparse.ArgumentParser(description='This command convert from json data type to xml and vice versa.')
    parser.add_argument('path_to_data', type=str, help='path to file to be converted')
    parser.add_argument('path_to_convert', type=str, nargs='?', help='path to file to be saved converted data')
    parser.add_argument('-m', '--mode', type=str, required=False, default='output', choices={'output', 'path'})
    args = parser.parse_args()

    if args.mode == 'path' and args.path_to_convert is None:
        parser.error("the following arguments are required: path_to_convert")

    with open(Path(str(args.path_to_data)), 'r') as data_file:
        data = json.loads(data_file.read()) if 'json' in args.path_to_data else data_file.read()
        build_tree = Tree.build_tree(data)
        if args.mode == 'path':
            build_tree.write(str(args.path_to_convert))
        else:
            print(build_tree.result())


if __name__ == '__main__':
    run()

    # We should have nodes as follow because json don't have root we can create
    # root = Node('data')
    # node_1 = Node('data_1', parent=root, value=1)
    # node_2 = Node('data_2', parent=root)
    # # for list we creating sub nodes with metadata id
    # sub_node2_1 = Node('data_2_sub', parent=node_2, metadata={'id': 0}, value=1)
    # sub_node2_2 = Node('data_2_sub', parent=node_2, metadata={'id': 1}, value=4)
    # sub_node2_3 = Node('data_2_sub', parent=node_2, metadata={'id': 2}, value=5)
    # node_3 = Node('data_3', parent=root)
    # sub_node3_1 = Node('sub_d_1', parent=node_3, value=3)
    # sub_node3_2 = Node('sub_d_2', parent=node_3, value=5)
    #
    # # to create Tree we should do
    # tree = Tree(root, tree_type='xml')
    # print(tree.json_to_xml())
    # print(json.dumps(tree.xml_to_json(), indent=4))
    #
    # data = {
    #     "data_1": 2,
    #     "data_2": [2, 4],
    #     "data_3": {
    #         "data_4": {
    #             "d41": "String1",
    #             "d42": 154
    #         },
    #         "data_5": 123
    #     }
    # }
    #
    # build_tree = Tree.build_tree(data)
    # print(build_tree.json_to_xml())
    # print(json.dumps(build_tree.xml_to_json(), indent=4))
    #
    # data = '''<data>
    #     <data_1> 2 </data_1>
    #     <data_2>
    #         <data_2_sub id = 1> 2 </data_2_sub>
    #         <data_2_sub id = 2> 4 </data_2_sub>
    #     </data_2>
    #     <data_3>
    #         <data_4>
    #             <d41> String1 </d41>
    #             <d42> 154 </d42>
    #         </data_4>
    #         <data_5> 123 </data_5>
    #     </data_3>
    # </data>'''
    # #
    # build_tree = Tree.build_tree(data)
    # print(build_tree.json_to_xml())
    # print(json.dumps(build_tree.xml_to_json(), indent=4))
    #
    #
    # data = {
    #     'data_1': 1,
    #     'data_2': [1, 2, 5],
    #     'data_3': {
    #         'sub_d_1': 3,
    #         'sub_d_2': 5
    #     }
    # }
    #
    # build_tree = Tree.build_tree(data)
    # print(build_tree.json_to_xml())
    # print(json.dumps(build_tree.xml_to_json(), indent=4))
    #
    # data = '''    <data>
    #     <data_1> 1 </data_1>
    #     <data_2>
    #         <data_2_sub id = 0>1</data_2_sub>
    #         <data_2_sub id = 1> 2 </data_2_sub>
    #         <data_2_sub id = 2> 5 </data_2_sub>
    #     </data_2>
    #     <data_3>
    #         <sub_d_1> 3 </sub_d_1>
    #         <sub_d_2> 5 </sub_d_2>
    #     </data_3>
    # </data>'''
    #
    # build_tree = Tree.build_tree(data)
    # print(build_tree.json_to_xml())
    # print(json.dumps(build_tree.xml_to_json(), indent=4))
