import functions
import pytest


ENV = 'prod'

def is_jira_123_closed():
    return False  # йдемо в  джиру і якщо статус != Done, closed то повертає False

@pytest.mark.triangle_feature
class TestTriangleNegative:

    @pytest.mark.skipif(ENV != 'DEV', reason='Not delivered on prod yet')
    def test_triangle_area_not_number(self):

        with pytest.raises(ValueError):
            functions.triangle_area('0',0,0)

    @pytest.mark.skipif(not is_jira_123_closed(), reason='JIRA-123, known issue')
    def test_triangle_area_0(self):

        with pytest.raises(ValueError):
            functions.triangle_area(0,0,0)

    @pytest.mark.skip(reason='know issue, JIRA-124')
    def test_triangle_area_111(self):

        with pytest.raises(ValueError):
            functions.triangle_area(1,1,1)


