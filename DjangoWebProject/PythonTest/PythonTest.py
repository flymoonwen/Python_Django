# encoding: UTF-8
import re
 
# ��������ʽ�����Pattern����
pattern = re.compile(r'ab')
 
# ʹ��Patternƥ���ı������ƥ�������޷�ƥ��ʱ������None
match = pattern.match('abbbc')
 
if match:
    # ʹ��Match��÷�����Ϣ
    print(match.group());
 
### ��� ###
# hello