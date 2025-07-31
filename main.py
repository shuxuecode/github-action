
import os
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

url = os.getenv('INPUT_TARGET_URL')

def check_url(url):
    try:
        response = urlopen(url, timeout=5)
        print(f"✅ 网址可访问 | 状态码: {response.getcode()}")
        return True
    except HTTPError as e:
        print(f"❌ HTTP 错误: {e.code} - {e.reason}")
    except URLError as e:
        print(f"❌ URL 错误: {e.reason}")
    except Exception as e:
        print(f"❌ 未知错误: {e}")
    return False



if __name__ == "__main__":
    check_url(url)
