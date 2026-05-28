from MyMath import myArea, myvolume, mycondition

def test_myArea():
    assert myArea("rectangle", 5, 4, 0, 0) == 20
    assert myArea("square", 3, 0, 0, 0) == 9

def test_myvolume():
    assert myvolume("cube", 3, 0, 0, 0) == 27
    assert myvolume("cuboid", 2, 3, 4, 0) == 24

def test_mycondition():
    # Проверяем теорему Пифагора
    assert mycondition("Pythagorean Triplet Checker", 3, 4, 5, 0) == 1
    assert mycondition("Pythagorean Triplet Checker", 1, 2, 3, 0) == 2
