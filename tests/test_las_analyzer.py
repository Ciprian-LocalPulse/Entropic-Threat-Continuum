from simulation.las_analyzer import LASLayer, LayeredAnonymityStack


def test_las_detects_weakest_layer():
    stack = LayeredAnonymityStack(
        [
            LASLayer("Physical", 0.9, 0.9, 0.9),
            LASLayer("Routing", 0.4, 0.8, 0.8),
        ]
    )
    assert stack.weakest_layer().name == "Routing"
    assert stack.compromise_path(threshold=0.5)
