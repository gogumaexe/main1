import os
os.makedirs('parent_dir/child_dir', exist_ok=True)

files = os.listdir('parent_dir')
print(files)

import glob
txt_files = glob.glob('*.txt')
print(txt_files)