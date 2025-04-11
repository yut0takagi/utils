import pikepdf
import itertools
import sys

class pdf_tools:
    def __init__(self,save_dir):
        self.save_dir = save_dir

    def open_secret_file(file_path,new_file_path,password):
        pdf = pikepdf.open(file_path, password=password)
        pdf_unlock = pikepdf.new()
        pdf_unlock.pages.extend(pdf.pages)
        pdf_unlock.save(pdf_nolock)

    def serch_password(file_path):
        characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        count = 0
        while True:
            count += 1
            print("count:",count)
            for password in itertools.product(characters,repeat=count):
                try:
                    #パスワードの文字を結合
                    password = ''.join( password )
                    open_secret_file(file_path,new_file_path,password)
                except:
                    pass
                else:
                    print('パスワードは' + password + 'でした。')
                    #処理終了
                    break

    def all_file_serch_password(dir_path):
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            serch_password(file_path)