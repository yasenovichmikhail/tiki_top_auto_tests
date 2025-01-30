import pytest
import time
from mimesis import Person
from mimesis import Gender
from mimesis import Text
import random
import string as s


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
