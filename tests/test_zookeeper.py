'''
File: test_zookeeper.py
Description: This python script tests the zookeeper class
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from zookeeper import Zookeeper
from mammal import Mammal
from enclosure import Enclosure

def test_zookeeper_duties():
    zk = Zookeeper("Brian", 123)
    assert zk.perform_duties() == "Brian is feeding animals and cleaning"

def test_feed_animal():
    zk = Zookeeper("Brian", 123)
    lion = Mammal("John", "Lion", 7, "meat")
    result = zk.feed_animal(lion)
    assert result == lion.eat()

def test_clean_enclosure():
    zk = Zookeeper("Brian", 123)
    enc = Enclosure(200, "savannah", 90, ["Lion"], "savannah")
    zk.clean_enclosure(enc)
    assert enc.cleanliness == 100
