from distutils.core import setup

setup(
      name = "nicosearch.py",
      py_modules = ["nicosearch"],
      scripts = ["debify.py"],
      version = "0.0.1",
      # ここのから選ぶ？ http://pypi.python.org/pypi?:action=list_classifiers 「License ::」を検索。
      license = "LGPL",
      # これも同上
      platforms = ['POSIX', 'Windows'],
      # このモジュールは何をするか一言
      description = "pack a set of files into a .deb file with minimal fuss.",
      author = "karasuyamatengu",
      author_email = "karasuyamatengu@じーめーる.com",
      url = "https://github.com/tengu/debify",
      keywords = ["debian", "package"],
      # できるだけ該当するクラシファイアお入れておくといい。
      # このクラシファイアは勝手に入力しないで該当するものをここから見付けてくる http://pypi.python.org/pypi?:action=browse
      classifiers = [
                     "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
                     # 対象とするOS。「Operating System :: POSIX」など
                     "Operating System :: POSIX :: Linux",
                     "Programming Language :: Python",
                     # プロジェクトのステータス。本番で磨き抜かれたものでなければ'3 - Alpha'、'4 -Beta'などとしておくのが無難だ。
                     "Development Status :: 4 - Beta",
                     # 稼動環境： 端末、ウェブ、デーモン、X11など
                     "Environment :: Console",
                     # 対象ユーザ
                     "Intended Audience :: Developers",
                     "Topic :: Utilities",
                     "Topic :: Software Development",
                     ],
      # 複数行の説明
      long_description = """\
          debify: pack a set of files into a .deb file with minimal fuss.
          ...
          ...
          """
      )
