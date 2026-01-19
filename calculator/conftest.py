import sys
from pathlib import Path

# 이 파일의 경로의 부모를 root로 함
# 이 파일의 경로의 부모는 바로 이 파일이 속한 디렉토리임
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))