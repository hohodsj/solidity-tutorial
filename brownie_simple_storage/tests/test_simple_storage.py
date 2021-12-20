from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expect = 0
    # Assert
    assert starting_value == expect


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    simple_storage.store(15)
    new_value = simple_storage.retrieve()
    expect = 15
    # Assert
    assert new_value == expect
