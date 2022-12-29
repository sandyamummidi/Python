import pytest

@pytest.mark.parametrize('a,b,c',[(1,2,3)])
def test_functionAdd(a,b,c):
    assert a+b==c
@pytest.mark.parametrize("str1,str2,str3",[("abchcl,def,abchcldef")])
def test_functionAdd1(str1,str2,str3):
    assert str1+str2==str3