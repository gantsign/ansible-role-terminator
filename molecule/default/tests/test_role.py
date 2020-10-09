def test_terminator(host):
    assert host.run('which terminator').rc == 0
