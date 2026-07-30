def test_import_suite_nodes():
    import sys
    sys.path.insert(0, '.')
    import suite_nodes

    # basic smoke assertions
    assert hasattr(suite_nodes, 'NODE_DIR')
    assert hasattr(suite_nodes, 'EXTENSION_PREFIX')
    # ensure a few expected functions exist
    assert callable(getattr(suite_nodes, '_get_checkpoint_list', None))
