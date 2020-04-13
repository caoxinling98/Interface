import pytest
import os
if __name__ == '__main__':
    pytest.main(['-s','--alluredir','./report/xml'])
    os.system('allure generate report/xml/ -o report/html --clean')