import pytest
from main import calculate_pressure
def test_logic():
    # اختبار حسابي بسيط للتأكد من أن المعادلة تعمل
    # إذا كانت T=0 مئوي (273.15 كلفن)، n=1, V=10, R=0.0821
    # P = (1 * 0.0821 * 273.15) / 10 = 2.24256
    val = calculate_pressure(0) 
    assert val == pytest.approx(2.24256, rel=1e-2)