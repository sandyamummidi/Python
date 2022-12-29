import pytest
@pytest.mark.parametrize("str1,str2,str3",[("abchcl,def,abchcldef")])
def test_functionAdd1(str1,str2,str3):
    assert str1+str2==str3