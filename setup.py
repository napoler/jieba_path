from setuptools import find_packages, setup
setup(
    name='jieba_path',
    version='0.0.1.1',
    description='结巴分词预处理目录下的文档',
    author='author',  # 作者
    author_email='napoler2008@gmail.com',
    url='https://github.com/napoler/jieba_path',
    # packages=find_packages(),
    packages=['jieba_path'],  # 这里是所有代码所在的文件夹名称
    install_requires=['jieba'])