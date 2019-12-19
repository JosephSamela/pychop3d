import pytest
import trimesh
import numpy as np
import copy

from pychop3d import bsp
from pychop3d import constants
from pychop3d import utils


def test_expand_node(mesh):
    print()
    tree = bsp.BSPTree(mesh)
    node = tree.nodes[0]
    extents = node.part.bounding_box_oriented.primitive.extents
    normal = trimesh.unitize(np.random.rand(3))
    planes = node.get_planes(normal, extents.min()/10)
    plane = planes[np.random.randint(0, len(planes))]
    tree = tree.expand_node(plane, node)


def test_different_from(mesh):
    print()
    tree = bsp.BSPTree(mesh)
    root = tree.nodes[0]
    extents = root.part.bounding_box_oriented.primitive.extents
    normal = trimesh.unitize(np.random.rand(3))
    planes = root.get_planes(normal, extents.min() / 10)
    plane = planes[np.random.randint(0, len(planes))]
    base_node = copy.deepcopy(root)
    base_node.split(plane)

    # smaller origin offset, should not be different
    test_node = copy.deepcopy(root)
    origin = plane[0] + trimesh.unitize(np.random.rand(3)) * .095 * np.sqrt(np.sum(constants.PRINTER_EXTENTS ** 2))
    test_plane = (origin, plane[1])
    test_node.split(test_plane)
    assert not base_node.different_from(test_node)

    # larger origin offset, should be different
    test_node = copy.deepcopy(root)
    origin = plane[0] + trimesh.unitize(np.random.rand(3)) * .15 * np.sqrt(np.sum(constants.PRINTER_EXTENTS ** 2))
    test_plane = (origin, plane[1])
    test_node.split(test_plane)
    assert base_node.different_from(test_node)

    # smaller angle difference, should not be different
    test_node = copy.deepcopy(root)
    random_vector = trimesh.unitize(np.random.rand(3))
    axis = np.cross(random_vector, plane[1])
    rotation = trimesh.transformations.rotation_matrix(np.pi / 11, axis)
    normal = trimesh.transform_points(plane[1][None, :], rotation)[0]
    test_plane = (plane[0], normal)
    test_node.split(test_plane)
    assert not base_node.different_from(test_node)

    # larger angle difference, should be different
    test_node = copy.deepcopy(root)
    random_vector = trimesh.unitize(np.random.rand(3))
    axis = np.cross(random_vector, plane[1])
    rotation = trimesh.transformations.rotation_matrix(np.pi / 9, axis)
    normal = trimesh.transform_points(plane[1][None, :], rotation)[0]
    test_plane = (plane[0], normal)
    test_node.split(test_plane)
    assert base_node.different_from(test_node)


def test_copy(mesh):
    mesh = copy.deepcopy(mesh)
    for i in range(10000):
        mesh = copy.deepcopy(mesh)

    tree = bsp.BSPTree(mesh)
    node = tree.nodes[0]
    for i in range(10000):
        node = copy.deepcopy(node)

    for i in range(10000):
        tree = copy.deepcopy(tree)