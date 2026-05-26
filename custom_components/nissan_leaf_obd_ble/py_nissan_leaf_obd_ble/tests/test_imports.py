"""Basic smoke tests for py-nissan-leaf-obd-ble."""

import importlib

from py_nissan_leaf_obd_ble.OBDCommand import OBDCommand


def test_package_imports():
    pkg = importlib.import_module("py_nissan_leaf_obd_ble")
    assert hasattr(pkg, "NissanLeafObdBleApiClient")
    assert hasattr(pkg, "OBD")
    assert hasattr(pkg, "ELM327")
    assert hasattr(pkg, "OBDStatus")


def test_obdcommand_rev_header():
    command = OBDCommand(
        "test",
        "Test command",
        b"0123",
        4,
        lambda messages: None,
        header=b"797",
        rev_header=b"7A7",
    )

    assert command.rev_header == b"7A7"
    clone = command.clone()
    assert clone.rev_header == b"7A7"
    assert clone == command

