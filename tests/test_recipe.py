from blob_effect import LoadInfo, Recipe, ResizeInfo


def test_recipe_assigns_ids_and_links_targets():
    load = LoadInfo(input_path="/tmp/does-not-exist.png")
    resize = ResizeInfo(width=10, height=10)

    recipe = Recipe(load, resize)

    assert load.id is not None
    assert resize.id is not None
    assert load.id != resize.id
    assert resize.target == load.id
    assert recipe.last_id == resize.id


def test_recipe_first_info_has_no_target():
    load = LoadInfo(input_path="/tmp/does-not-exist.png")

    Recipe(load)

    assert load.target is None
    assert load.uuid_target is None


def test_recipe_content_returns_ordered_mapping():
    load = LoadInfo(input_path="/tmp/does-not-exist.png")
    resize = ResizeInfo(width=10, height=10)

    recipe = Recipe(load, resize)

    content = recipe.content()
    assert list(content.keys()) == [load.id, resize.id]


def test_recipe_export_returns_one_entry_per_info():
    load = LoadInfo(input_path="/tmp/does-not-exist.png")
    resize = ResizeInfo(width=10, height=10)

    recipe = Recipe(load, resize)

    exported = recipe.export()
    assert len(exported) == 2
    assert {e["TASK"] for e in exported} == {"LoadImage", "Resize"}
